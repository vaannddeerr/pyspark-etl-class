from pyspark.sql import functions as F






def etl(menager):

    df = menager.read_file()

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

