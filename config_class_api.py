import requests
import json

from spark_config import spark_session

class PipelineApi:
    def __init__(self, url:str):
        self.url = url
        self.response = None
        self.error = None
        self.spark = spark_session
        self.df = None
        
    def consummer_api(self):
        try:
            res = requests.get(self.url, timeout=30) # Função da biblioteca requests que executa o pedido de acesso na API
                                                     # timeout=30 parametro que diz ao python para aguardar no máximo 30 seg pela resposta.
            res.raise_for_status() # verifica se o site retorno algum erro como "404 Not Found". Se estiver tudo ok ele não faz nada.
            self.response = res.json()  # Aqui pego o  conteúdo do site que geralmente vem em um formato de texto em JSON, converto para um formato que python entenda no caso JSON. 
            self.error = "Nenhum" # Como tudo deu certo , ai qualquer registro de erro é limpo  erros anteriores.
            return self.response # A função termina aqui entregando os dados para quem chamou.
        
        except Exception as e:
            self.error = str(e)         # Aqui preenchemos o erro, se der ruim
            self.response = None
            return None
    
    def save_response(self, path:str, response:str):

        if response:
            with open(path, 'w', encoding='utf-8') as output_response:
                # Salva o dicionário no arquivo
                # indent=4 serve para o arquivo ficar "estruturado" e legível
                json.dump(response, output_response, indent=4, ensure_ascii=False)
        
            print(f"Arquivo salvo com sucesso como '{path}'!")
        else:
            print(f"Não foi possível salvar. Erro: {self.error}")


    def read_dataframe(self, path_file:str, is_path:bool=True):

        if is_path:
            self.df = self.spark.read.format('json').option('multiline',True).load(path_file)
        else:
            self.df = self.spark.read.table(path_file)
        
            return self.df

        print(f'Dataframe carregado com sucesso, registros capturados:{self.df.count()}')

    