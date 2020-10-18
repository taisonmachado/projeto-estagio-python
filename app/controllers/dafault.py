from flask import render_template
from app import app

from app.models.acess import Acess

@app.route('/')
def index():
    url = "https://www.acordacidade.com.br/"
    acess = Acess(url) #Cria o objeto de acesso a página passando a url no construtor.
    return render_template('index.html', acess=acess)