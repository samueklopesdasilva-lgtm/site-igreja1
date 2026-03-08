from flask import Flask, render_template
import random

app = Flask(__name__)

versiculos = [
"Tudo posso naquele que me fortalece. - Filipenses 4:13",
"O Senhor é meu pastor e nada me faltará. - Salmos 23:1",
"Se Deus é por nós, quem será contra nós? - Romanos 8:31",
"Buscai primeiro o reino de Deus. - Mateus 6:33",
"No mundo tereis aflição, mas tende bom ânimo; eu venci o mundo. - João 16:33"
]

@app.route("/")
def home():
    versiculo = random.choice(versiculos)
    return render_template("index.html", versiculo=versiculo)

@app.route("/cultos")
def cultos():
    return render_template("cultos.html")

app.run(host="192.168.0.25", port=5000,debug=True)