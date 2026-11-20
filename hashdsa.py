# lis = []
# with open(r"C:\Users\Harsha A\OneDrive\Attachments\Documents\data.csv","r") as f:
#     for lines in f:
#         items = lines.split(",")
#         day = items[0]
#         price = items[1]
#         lis.append([day,price])
#     print(lis)

# for data in lis:
#     if data[0] == "Mar-06":
#         print(data[1])


# class hash:
#     def __init__(self):
#         self.max = 10
#         self.arr = [None for i in range(self.max)]

#     def getash(self,keys):
#         h = 0
#         for key in keys:
#             h+=ord(key)
#         return h%self.max

    

#     def __setitem__(self, key, value):
#         h = self.getash(key)
#         self.arr[h] = value

#     def __delitem__(self, key):
#         h = self.getash(key)
#         self.arr[h] = None

#     def __getitem__(self, key):
#         h = self.getash(key)
#         print(self.arr[h])

# t = hash()
# t["march 6"] = 45
# t["march 7"]=123
# t["march 18"]=143
# t["march 17"] = 4
# t["march 6"]
# t["march 7"]

# print(t.arr)    

# class hash:
#     def __init__(self):
#         self.max = 10
#         self.arr = [[] for i in range(self.max)]

#     def get_hash(self,key):
#         h= 0
#         for i in key:
#             h+=ord(i)
#         return h%self.max

#     def __setitem__(self, key, value):
#         h = self.get_hash(key)
#         found = False
#         for inx,element in enumerate(self.arr[h]):
#             if len(element)==2 and element[0]== key:
#                 self.arr[h][inx] = (key,value)
#                 found = True

#         if not found:
#             self.arr[h].append((key,value)) 

#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         for idx,element in enumerate(self.arr[h]):
#             if element[0]==key:
#                 del self.arr[h][idx]

#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         for idx,element in enumerate(self.arr[h]):
#             if element[0] == key:
#                 print(element[1])


# t = hash()
# t["march 6"]=767
# t["march 17"]= 645
# t["march 17"] = 420
# t["march 17"]

# print(t.arr)   
# disctionary =  {}
# with open(r"C:\Users\Harsha A\Downloads\nyc_weather (1).csv","r") as f:
#     for line in f:
#         tokens = line.split(",")
#         try:
#             temperature = int(tokens[1])
#             month_date = tokens[0]
#             disctionary[month_date] = temperature
#         except:
#             print("Invalid temperature")

# print(disctionary["Jan 9"])
# print(disctionary["Jan 4"])


# disc = {}

# with open(r"C:\Users\Harsha A\Downloads\poem.txt","r") as f:
#     for line in f:
#         tokens = line.split()
#         for token in tokens:
#             if token in disc:
#                 disc[token]+=1
#             else:
#                 disc[token]=1
# print(disc["I"])

# class hash:
#     def __init__(self):
#         self.max=10
#         self.arr = [[] for _ in range(self.max)]

#     def get_hash(self,keys):
#         h = 0
#         for key in keys:
#             h+=ord(key)
#         return h%self.max

#     def __setitem__(self, key, value):
#         h = self.get_hash(key)
#         found = False
#         for idx,element in enumerate(self.arr[h]):
#             if len(element) == 2 and element[0]== key:
#                 self.arr[h][idx]=(key,value)
#                 found= True
#         if not found:
#             self.arr[h].append((key,value))

#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         for element in self.arr[h]:
#             if element[0]==key:
#                 print(element[1])
    

#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         del self.arr[h]

# t = hash()

# t["march 1"]=765
# t["march 6"]=876
# t["march 17"] = 737


# t["march 6"]

from collections import deque

print(dir(deque))


