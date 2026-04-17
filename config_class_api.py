import requests
import json

class PipelineApi:
    def __init__(self, url:str):
        self.url = url
        self.response = None
        
    def consummer_api(self):
        res = requests.get(self.url, timeout=30)
        self.response = res.json()
        return self.response
    
    def save_response(self, path:str, response:str):

        if response:
            with open(path, 'w', encoding='utf-8') as output_response:
                # Salva o dicionário no arquivo
                # indent=4 serve para o arquivo ficar "estruturado" e legível
                json.dump(response, output_response, indent=4, ensure_ascii=False)
        
        else:
            print(f"Não foi possível salvar. Erro")
