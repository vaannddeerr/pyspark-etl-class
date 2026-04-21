from pyspark.sql import functions as F






def etl(df):

    

    df = df.withColumn('dados', F.explode(F.col('dados')))\
           .withColumn('id', F.col('dados.id'))\
           .withColumn('email', F.col('dados.email'))\
           .withColumn('idLegislatura', F.col('dados.idLegislatura'))\
           .withColumn('nome', F.col('dados.nome'))\
           .withColumn('siglaPartido', F.col('dados.siglaPartido'))\
           .withColumn('siglaUf', F.col('dados.siglaUf'))\
           .withColumn('uri', F.col('dados.uri'))\
           .withColumn('uriPartido', F.col('dados.uriPartido'))\
           .withColumn('urlFoto', F.col('dados.urlFoto'))\
           .withColumn('df_carga', F.current_timestamp())\
           .drop(F.col('dados'))
    
    print(f'💹volumetria:{df.count()}')
    print(f'🔃Aplicando transformação:')

    return df

