from flask import Flask
from validate_docbr import CPF, CNPJ



app = Flask("My App")

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return "<h1>Produtos</h1>"


@app.route("/servicos")
def servicos():
    return "<h1>Nossos Serviços</h1>"

@app.route("/gerar-cpf")
def gerarCPF():
    cpf = CPF()

    return f"<h1>CPF: {cpf.generate(True)}</h1>"


@app.route("/gerar-cnpj")
def gerarCNPJ():
    cnpj = CNPJ()

    return f"<h1>CNPJ: {cnpj.generate(True)}</h1>"

app.run()