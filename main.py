from config_class_api import PipelineApi
from etl_process import etl


def executa_pipeline():
    file_path = 'dadosabertos_v2.json'
    path = f'/Volumes/workspace/default/landing_zone/{file_path}'

    print('================================')
    menager = PipelineApi(url='https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')
    print(f'Consumindo API:{menager}')

    print('================================')
    resultado = menager.consummer_api()
    print(f'Resultado da solicitação...')

    print('================================')
    menager.save_response(path, resultado)
    print(f'Salvando resultado...')

    print('================================')
    menager.read_dataframe(path, is_path=True)
    menager = etl(menager.df)
    print(f'Aplicando transformação:{menager}')
    
    return menager

    

if __name__=="__main__":
    executa_pipeline()    
