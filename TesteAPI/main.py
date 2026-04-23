from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id' = 1,
        'titulo' = 'O senhor dos aneis',
        'autor' = 'J.R.R Tolkien'
    },
    {
        'id' = 2,
        'titulo' = 'Harry Potter',
        'autor' = 'J.K Howling'
    },
    {
        'id' = 3,
        'titulo' = 'James Clear',
        'autor' = 'Hábitos Atômicos'
    }
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id():
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


app.run(port=5000,host='localhost',debug=True)