import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import random as rd


class MotivacionalService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_MOTIVE)
        self.load_model()

    def load_model(self):
        """"
        Carrega o modelo VADER a ser usado
        """
        logger.debug(mensagens.FIM_LOAD_MOTIVE)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_MOTIVE)
        start_time = time.time()

        response_motive = self.buscar_motivacao(texts['Como esta se sentindo?'])

        logger.debug(mensagens.FIM_MOTIVE)
        logger.debug(f"Motivado em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['Como esta se sentindo?'])
        df_response['motive'] = response_motive

        df_response = df_response.drop(columns=['Como esta se sentindo?'])

        response = {
                     "listaClassificacoes": json.loads(df_response.to_json(
                                                                            orient='records', force_ascii=False))}

        return response

    def buscar_motivacao(self, texts):
        """
        Pega o modelo carregado e aplica em texts
        """
        logger.debug('Começando a Motivar...')

        response = []

        for text in texts:
            motive_dict = text
        
            # frase motivacional de acordo com seu sentimento
            if motive_dict.lower() == "feliz":
                
                list_motive = ["Felicidade é conservar energia para coisas que valem a pena", 
                                "A felicidade irradia como a fragância de uma flor e atrai todas as coisas boas em sua direção",
                                "Feliz aquele que transfere o que sabe e aprende o que ensina"]
                
                motivelen = len(list_motive) - 1
                i = rd.randint(0,motivelen)
                response.append(list_motive[i])
        
            elif motive_dict.lower() == "triste":
                list_motive = ["Nossos fracassos, às vezes,são mais frutíferos do que os êxitos - Henry Ford",
                                "Não perca o ânimo nem a vontade de continuar, os impossíveis aó existem para quem desiste!",
                                "Quando o caminho ficar difícil não desanime, são essas as estradas que levam a lugares maravilhosos"]
                
                motivelen = len(list_motive) - 1
                i = rd.randint(0,motivelen)
                response.append(list_motive[i])
                    
            else:
                response.append("A arte de ser ora audacioso, ora prudente, é a arte de vencer - Napoleão Bonaparte")

        return response