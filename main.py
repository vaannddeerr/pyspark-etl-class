from config_class_api import PipelineApi
from etl_process import etl


def executa_pipeline():
    file_path = 'dadosabertos_v2.json'
    path = f'/Volumes/workspace/default/landing_zone/{file_path}'
    print('🔛Iniciando processamento.🔛')
    print('================================')
    menager = PipelineApi(url='https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')
  

    resultado = menager.consummer_api()
    print(f'📖Resultado da solicitação:')

    menager.save_response(path, resultado)
    print(f'✔️Arquivo salvo com sucesso')

    print('================================')
    menager.read_dataframe(path, is_path=True)
    menager = etl(menager.df)

    print('================================')
    menager.write_dataframe('tableNameFull')
    
    
    return menager

    

if __name__=="__main__":
    executa_pipeline()    
