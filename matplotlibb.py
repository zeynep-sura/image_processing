import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('personel_list.csv')
# print(df)

# plt.figure(figsize=(12,6))
# plt.plot(df.ad, df.yas)
# plt.xlabel('adlar')
# plt.ylabel('yaslar')
# plt.title('ad yaş grafiği')
# plt.show()

# hem yaş hem maaş grafiği nasıl gösterilir:

# plt.subplot(1,2, 1) # 3. kısım hangisini kullanacağını belirttiğimiz yer. 
# plt.plot(df.ad, df.maas)

# plt.subplot(1,2,2), plt.plot(df.ad, df.yas)

# plt.show()




# nokta gösterim: 

# plt.scatter(df.ad, df.yas)
# plt.show()



# histogram şeklinde: 

# plt.hist(df['yas'])
# plt.show()


# dairesel dilimler: 

plt.pie(df.maas, labels=df.ad)
plt.show()
