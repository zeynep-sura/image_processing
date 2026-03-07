import pandas as pd

#  normal  sözlük

# personel_list = {'ad': ['zeynep', 'sena', 'melek', 'melda', 'süm', 'melike'],
#                  'yas': [21,20,21,22,21,21],
#                  'maas': [80000,80000,80000,70000,90000,90000]}

# df = pd.DataFrame(personel_list)
# print(df)

#excelden alıp göstermek için: 

df = pd.read_csv("personel_list.csv")
print(df) 
print(df.head(2))  #baştan itibaren kaç eleman varsa onları bastırır

print(df.columns)
print(df.describe())
print(df.dtypes)
print(df.tail(1)) #sondqn gönsterir
print(df.shape)
print(df.sum())
print(df['maas'].sum())

print(df[df['maas']> 50])