import numpy as np 

# zero dimenisonal array
arr = np.array(10)
print("Dimension:-",arr.ndim)

# single dimensional array 
arr1 = np.array([12,23,34,45,56,67])

print(arr1)
print(arr1[2])
print(arr1[4])

print(arr1[1]+ arr1[4])

# slicing 
print(arr1[2:5])

# sum of all elements 
print("Sum of elements :- ",np.sum(arr1))

# max number 
print("Max Number :-",np.max(arr1))

# min number 
print("Min Number :- ",np.min(arr1))

print("_____________________________")
for i in arr1:
    print(i)

sum1=0 

for i in arr1:
    sum1+=i
print("Sum of Elements :-",sum1)

fruits = np.array(["Mango","Banana","Kiwi","Orange","Pineapple"])

print(fruits[3:5])

print(np.sort(arr1))

result = np.sort(arr1)

print(result[::-1])

a =np.array([2,3,4,5])
b =np.array([5,6,7,8])

print(a+b)
print(a*b)

print(a+10) 

print("Shape :-",a.shape)
print(a.dtype)

# special arrays 

print(np.zeros(5))
print(np.ones(6))
print(np.full(5,7))


