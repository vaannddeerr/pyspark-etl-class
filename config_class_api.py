import requests
import json

from pyspark.sql import SparkSession

class PipelineApi:
    def __init__(self, url:str):
        self.url = url
        self.response = None
        self.error = None
        self.spark = SparkSession.builder.getOrCreate()
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
            print(f"Erro na comunicação com a API: {self.error}")
    
    def save_response(self, path:str, response:str):

        if response:
            with open(path, 'w', encoding='utf-8') as output_response:
                # Salva o dicionário no arquivo
                # indent=4 serve para o arquivo ficar "estruturado" e legível
                json.dump(response, output_response, indent=4, ensure_ascii=False)
        
            print(f"Local onde o arquivo foi salvo: '{path}'✍️")
        else:
            print(f"Não foi possível salvar. Erro: {self.error}")


    def read_dataframe(self, path_file:str, is_path:bool=True):

        if is_path:
            self.df = self.spark.read.format('json').option('multiline',True).load(path_file)
            
        else:
            print(f'Lendo Tabela...')
            self.df = self.spark.read.table(path_file)
            return self.df

        print(f'📖Lendo DataFrame')

    def write_dataframe(self, tableName:str):
        """Grava o DataFrame atual como uma tabela Delta."""
        if self.df is None:
            raise ValueError("❌Não há dados carregados para gravar! Use ler_tabela primeiro.")
        
        self.spark.sql(f'drop table if exists {tableName}')

        self.df.write \
            .format("delta") \
            .mode('overwrite') \
            .option('overwriteSchema',True)\
            .saveAsTable(tableName)
            
        print(f"Tabela {tableName} gravada com sucesso✔️.")
        


    