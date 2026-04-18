from config_class_api import PipelineApi
from etl_process import etl


def executa_pipeline():
    file_path = 'dadosabertos_v2.json'
    path = f'/Volumes/workspace/default/landing_zone/{file_path}'

    minha_api = PipelineApi(url='https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')
    resultado = minha_api.consummer_api()
    minha_api.save_response(path, resultado)
    df = minha_api.read_dataframe(path)
    df = etl(df)

    return df
    

if __name__=="__main__":
    executa_pipeline()    
