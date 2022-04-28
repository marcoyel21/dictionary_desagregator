import pandas as pd
import json
#Se importan paquetes necesarios
#Se importa la tabla
df= pd.read_csv("data.csv")


#Se crea una tabla vacia para ir vaciando la info
table = pd.DataFrame(columns = ['dict'])
for i in range(len(df)):
#Si el diccionario anidado "transacciones" existe entonces extrae la info
    try:
        temp = pd.DataFrame([[json.loads(df["nvcOpciones"][i])[0]["transacciones"][0]]], columns = ['dict'])
        table = pd.concat([table, temp])
        
#Si no existe entonces pone un diccionario vacio
    except:
        temp = pd.DataFrame([['{}']], columns = ['dict'])
        table = pd.concat([table, temp])

table.reset_index(inplace=True)
table=table.drop(columns=['index'])   


# Finalmente expando el diccionario en formato tabla (con nas donde no hay info)
# Esta tabla solo contiene las nuevas columnas
df_new_columns = pd.json_normalize(table['dict'])

# Pego ambas tablas (las nuevas columnas y las viejas)
df_complete = pd.concat([df, df_new_columns], axis=1)
#df_new_columns.to_csv("data2.csv")
#df_complete.to_csv("data2.csv")