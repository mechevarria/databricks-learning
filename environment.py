import os
from pyspark.sql import SparkSession

catalog=os.getenv('MY_CATALOG')
schema=os.getenv('MY_SCHEMA')
table=os.getenv('MY_TABLE')

spark = SparkSession.builder.getOrCreate()

table_name=f'{catalog}.{schema}.{table}'

df = spark.table(table_name) 
df_pandas = df.toPandas()
row_count = df_pandas.shape[0]
print(f'The number of rows in {catalog}.{schema}.{table} are {row_count}')