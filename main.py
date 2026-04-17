from config_class_api import PipelineApi

file_path = 'dadosabertos_v2.json'
path = f'/Volumes/workspace/default/landing_zone/{file_path}'

minha_api = PipelineApi(url='https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')
resultado = minha_api.consummer_api()
minha_api.save_response(path, resultado)
