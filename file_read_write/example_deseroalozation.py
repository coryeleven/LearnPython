import  pickle
pkl_file = open("data.pkl","rb")
data = pickle.load(pkl_file)
data1 = pickle.load(pkl_file)
data2 = pickle.load(pkl_file)
data3 = pickle.load(pkl_file)

print(data)
print(data1)
print(data2)
print(data3)

pkl_file.close()