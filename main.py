from config_class_api import PipelineApi
from etl_process import etl


def executa_pipeline():
    file_path = 'dadosabertos_v2.json'
    path = f'/Volumes/workspace/default/landing_zone/{file_path}'

    menager = PipelineApi(url='https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')
    resultado = menager.consummer_api()
    menager.save_response(path, resultado)
    menager = menager.read_dataframe(menager)
    

    return menager
    

if __name__=="__main__":
    executa_pipeline()    
