from pyspark.sql import functions as F
from pyspark.sql import dataframe
from config_class_api import PipelineApi





def etl(df:dataframe):

    df = df.withColumn('dados', F.explode(F.col('dados')))\
           .withColumn('id', F.col('dados.id'))\
           .withColumn('email', F.col('dados.email'))\
           .withColumn('idLegislatura', F.col('dados.idLegislatura'))\
           .withColumn('nome', F.col('dados.nome'))\
           .withColumn('siglaPartido', F.col('dados.siglaPartido'))\
           .withColumn('siglaUf', F.col('dados.siglaUf'))\
           .withColumn('uri', F.col('dados.uri'))\
           .withColumn('uriPartido', F.col('dados.uriPartido'))\
           .withColumn('urlFoto', F.col('dados.urlFoto')).drop(F.col('dados'))
    
    return df.show()

