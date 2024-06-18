from flask import Flask, render_template
from validate_docbr import CPF, CNPJ



app = Flask("My App")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome": "Spray", "descricao": "Spray capilar para cabelo", "imagem": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcTOGhZcS1QofGa5igCqmBoX35fdOQF-0rgpGNyUqKnLl4Ix7U4C_6ZQs7s9J176vzB3lxG1MVj1B-GiuHZ3XUJNTodvFKRTHo6azSxlfl20U_2lszrlnveELEJuL4JLMCKrFQER3g&usqp=CAc"},
        {"nome": "Saw Palmetto", "descricao": "Saw Palmetto para Queda Capilar", "imagem": "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcQdFNvDzcBjo9eNzpoocPFoXJNqt_qYOa9mc0JtYhDp-E0HwM0nBtXvSG1zak7NSZ3OvksgzveY34gO4UAEIZ964Zg52u8y5hZa90RG59-jk6_96iTHmdeOBw2GTMJtH_k12ULNjpQ&usqp=CAc"},
        {"nome": "MinoxidiI", "descricao": "MinoxidiI Tópico para Queda Capilar ", "imagem": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSHsqcxCAzYBKWywG3AVoUJf4gdOEqlKLi3tninlTwV7uVYD9YW-bYxAbN9tFqf8staimGeTmxf5VJPLXiNDVIfzBncA_k54A2CYOEP2dzV8mfxZrBpoyb84Su_UlLNqrKGmb42U2I&usqp=CAc"}
    ]

    return render_template("produtos.html", produtos = lista_produtos)


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