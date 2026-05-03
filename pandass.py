import pandas as pd
import numpy as np
#  normal  sözlük

# personel_list = {'ad': ['zeynep', 'sena', 'melek', 'melda', 'süm', 'melike'],
#                  'yas': [21,20,21,22,21,21],
#                  'maas': [80000,80000,80000,70000,90000,90000]}

# df = pd.DataFrame(personel_list)
# print(df)

#excelden alıp göstermek için: 

# df = pd.read_csv("personel_list.csv")
# print(df) 
# print(df.head(2))  #baştan itibaren kaç eleman varsa onları bastırır

# print(df.columns)
# print(df.describe())
# print(df.dtypes)
# print(df.tail(1)) #sondqn gönsterir
# print(df.shape)
# print(df.sum())
# print(df['maas'].sum())

# print(df[df['maas']> 50])


disIndeksler=["onder","onder","onder","zeynep","zeynep","zeynep"]
icIndeksler=["a","b","c","d","e","f"]
birlesmisIndeks=list(zip(disIndeksler,icIndeksler))
birlesmisIndeks=pd.MultiIndex.from_tuples(birlesmisIndeks)

listem=[[1,"f"],[2,"g"],[3,"h"],[4,"k"],[5,"l"],[6,"m"]]
dizisi=np.array(listem)
listemDataFrame=pd.DataFrame(dizisi,index=birlesmisIndeks,columns=["yas","uye"])
print(listemDataFrame)

print(listemDataFrame.loc["onder"].loc["a"])
listemDataFrame.index.names=["aile adi","uye"]
print(listemDataFrame)