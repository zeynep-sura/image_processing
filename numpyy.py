import numpy as np 

arr = np.array([1,2,3,4,5])
print(arr)

# elemanları 0 olarak oluşturcak driekt

arr1 = np.zeros([3, 4])
print(arr1) 


arr2 = np.ones([3,4])
print(arr2)


arr3= np.arange(10,100,10)
print(arr3)

# reshape satır sütun ayarlıyo
arr4 = np.arange(20).reshape(4,5)
print(arr4)

# ndim : boyut saysını verir
# shape : dizi boyutunu verir
# size : dizideki eleman sayısını verir
# dtype : dizideki eleman türünü döndğrür

arr2d = np.arange(12).reshape(4,3)
arr3d = np.array([[[1,2], [3,4]],[[5,6], [7,8]]])
print(arr2d.ndim)
print(arr3d.ndim)
print(arr2d.shape)
print(arr3d.shape)
print(arr2d.size)
print(arr3d.size)
print(arr2d.dtype)
print(arr3d.dtype)