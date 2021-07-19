from flask import Flask, jsonify,request
import json

app = Flask(__name__)

tarefa = [
    {
    'id':'0',
    'responsavel':'rafael',
    'tarefa':'Desenvolvedor método GET',
    'status':'concluido'
    },
    {
    'id':'1',
    'responsavel':'joao',
    'tarefa':'Desenvolvedor método POST',
    'status':'pendente' }
]

@app.route('/tarefas/<int:id>/', methods=['GET' , 'DELETE', 'PUT'])
def tarefas(id):
    if request.method == 'GET':
        try:
            response = tarefa[id]
        except IndexError:
            mensagem = 'Tarefa {} não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o admnistrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        tarefa[id]['status'] = 'concluido'
        mensagem = 'Alteração feita com Sucesso'
        response = {'status': 'Concluido', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'DELETE':
        tarefa.pop(id)
        return jsonify({'status': 'sucesso' , 'mensagem': 'excluido'})

@app.route('/tarefas/', methods =['POST','GET'])
def listar_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefa)
        dados['id'] = posicao
        tarefa.append(dados)
        return jsonify(tarefa[posicao])
    elif request.method == 'GET':
        return jsonify(tarefa)

if __name__ == '__main__':
    app.run(debug=True)