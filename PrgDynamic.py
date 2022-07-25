import numpy as np

y=(input("Lenth of list:"))
list1=[]
for i in range (len(y)):
    element = input("enter the element:")
    list1.append(element)
print("list element are:",list1)
x=(input("Lenth of list:"))
list2=[]
for i in range (len(x)):
    element = input("enter the element:")
    list2.append(element)
print("list element are:",list2)
c=input("Capacité")
n=len(y)
objects=np.zeros(n)
T= np.zeros((n+1,c+1))


for i in range (n):
    for j in range(c+1):
        if j >= y[i]:
            T[i+1,j]=max(T[i,j], T[i,j-y[i]]+x[i])
        else:
            T[i+1,j]=T[i,j]

print(T)

i,j=np.shape(T)
i-=1
j-=1
while T[i,j]==T[i,j-1]:
    j-=1
while j>=0:
    while i>0 and T[i,j]==T[i-1,j]:
        i-=1
    j=j-y[i-1]
    if j>=0:
        objects[i-1]=1
    i-=1
print("solution objects: ",objects)
print("solution : ", T[i,j])
