from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    #textoMensagem': fields.List(fields.String(), required=True, description= "Frase em inglês a ser classificada")})
    'Como esta se sentindo?': fields.List(fields.String(), required=True, description= "Sentimento pessoal no momento")})