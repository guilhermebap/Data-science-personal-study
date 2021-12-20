from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
import pickle
from sklearn.linear_model import LinearRegression

with open('modelo_preco', 'rb') as f:
    modelo = pickle.load(f)

colunas = ['tamanho', 'ano', 'garagem']

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'guilherme'
app.config['BASIC_AUTH_PASSWORD'] = 'alura'

basicauth = BasicAuth(app)

@app.route('/')
def home():
    return 'Minha primeira API'

@app.route('/sentimento/<frase>')
@basicauth.required
def sentimento(frase):
    tb = TextBlob(frase)
    #tb_en = tb.translate(to='en')
    #polaridade = tb_en.sentiment.polarity
    #return f'Polaridade: {polaridade}'
    return tb

@app.route('/cotacao/', methods=['POST'])
@basicauth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])

app.run(debug=True)