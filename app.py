import math
from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi untuk menghitung probabilitas Poisson dan menampilkan langkah-langkah
def poisson_probability(lmbda, k):
    # Langkah 1: Hitung λ^k
    lambda_k = lmbda ** k
    
    # Langkah 2: Hitung e^(-λ)
    exp_neg_lambda = math.exp(-lmbda)
    
    # Langkah 3: Hitung k! (faktorial k)
    k_factorial = math.factorial(k)
    
    # Langkah 4: Hitung probabilitas Poisson
    probability = (lambda_k * exp_neg_lambda) / k_factorial
    
    # Menyusun rumus dan langkah-langkah perhitungan
    steps = {
        'lambda_k': f'λ^k = {lmbda}^{k} = {lambda_k}',
        'exp_neg_lambda': f'e^(-λ) = e^(-{lmbda}) = {exp_neg_lambda}',
        'k_factorial': f'k! = {k}! = {k_factorial}',
        'probability': f'P(X = {k}) = λ^k * e^(-λ) / k! = {lambda_k} * {exp_neg_lambda} / {k_factorial} = {probability}'
    }
    
    return probability, steps

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Mengambil input dari form
        lmbda = float(request.form['lambda'])  # Rata-rata barang masuk (λ)
        k = int(request.form['k'])  # Jumlah barang yang diinginkan (k)
        
        # Menghitung probabilitas Poisson dan langkah-langkah perhitungan
        probability, steps = poisson_probability(lmbda, k)
        
        # Mengirimkan hasil dan langkah-langkah perhitungan ke halaman web
        return render_template('index.html', probability=probability, steps=steps, lmbda=lmbda, k=k)
    
    return render_template('index.html', probability=None, steps=None)

if __name__ == '__main__':
    app.run(debug=True)
