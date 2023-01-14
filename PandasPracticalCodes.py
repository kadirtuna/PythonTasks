import pandas as pd

dict1 = {"Isim":["Ali", "Veli", "Kenan", "Murat", "Ayse", "Hilal"], 
         "Yas": [15, 16, 17, 33, 45, 66],
         "Maas":[100, 150, 240, 350, 110, 220]}

#Converting dict1 to a data structure
data1 = pd.DataFrame(dict1)

print(data1)
print(data1.head())#It prints out just 5 rows.
print(data1.columns)
print(data1.info())

#Statistical Properties
print(data1.describe())
print(data1["Yas"])

#Adding a new column to data
data1["Sehir"] = ["Ankara", "Kocaeli", "İstanbul", "İzmir", "Denizli", "Balıkesir"]
print(data1)

#Printing all rows in "Yas" column out
print(data1.loc[:,"Yas"])

print(data1.loc[:2, "Yas"])#loc command works with inclusive the finish step(2). [0, 1, 2]

print(data1.loc[:2, "Yas":"Sehir"])

print(data1.loc[:2, ["Yas","Sehir"]])

print(data1.loc[::-1])#It prints the reversed data

#Iloc prints until the one less than finish step(3) at the indexes of columns(1, 2)
print(data1.iloc[:3, [0, 1]])


#Filtering
dict2 = {"Isim":["Ali", "Veli", "Kenan", "Murat", "Ayse", "Hilal"], 
         "Yas": [15, 16, 17, 33, 45, 66],
         "Maas":[100, 150, 240, 350, 110, 220]}

data2 = pd.DataFrame(dict2)
print(data2)

#filter1 is a filter that specifies the data that is bigger than 22 for the column of "Yas" 
filter1 = data2.Yas > 22
print(data2[filter1])

ortalama_yas = data2.Yas.mean()

#New column named "YAS_GRUBU" for defining whether a person is lower or bigger than the mean of age.  
data2["YAS_GRUBU"] = ["Kucuk" if ortalama_yas > i else "Buyuk" for i in data2.Yas]


dict3 = {"Isim":["Murat", "Ayse", "Hilal"], 
         "Yas": [33, 45, 66],
         "Sehir":["Ankara", "Ankara", "Antalya"]}

data3 = pd.DataFrame(dict3)
#Concatenation of data

#Vertically concatenation of data2 and data3
#For vertical, axis = 0
#For horizontal, axis = 1
data_vertical = pd.concat([data2, data3], axis = 0)
data_horizontal = pd.concat([data2, data3], axis = 1)












