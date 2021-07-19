from flask_restful import Resource

lista_habilidades=['Pyhon', 'Java', 'Flask', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
