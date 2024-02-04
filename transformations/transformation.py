from pyspark.sql import functions as f 

def addColumn(df,new_column):
    df = df.withColumn(f'{new_column}',f.lit('hiii'))
