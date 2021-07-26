import pickle

data = 'hello world'
data1 = list(range(20)) [1::2]
data2 = {"x","y","z"}
data3 = {"a":data,"b":data1,"c":data2}

print(data)
print(data1)
print(data2)
print(data3)
print("data4")

output = open("data.pkl","wb")
pickle.dump(data,output)
pickle.dump(data1,output)
pickle.dump(data2,output)
pickle.dump(data3,output)
output.close()