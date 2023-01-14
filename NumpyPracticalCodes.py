import numpy as np

#1 dimension numpy array
nparray1 = np.array([1, 2, 3, 4, 5])
print(nparray1.shape)
print(nparray1.ndim)
print(nparray1.size)
print(nparray1.dtype.name)
print(type(nparray1))

#2 dimension numpy array
nparray2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(nparray2)

#A numpy array filled with zeroes
nparray3 = np.zeros((3, 4))
print(nparray3)

#A numpy array filled with ones
nparray4 = np.ones((3, 4))
print(nparray4)

nparray5 = np.arange(10, 50, 5)
print(nparray5)# [10, 15, 20, 25, 30, 35, 40, 45, 50]

nparray6 = np.empty((3, 4))
print(nparray6)

nparray7 = np.linspace(10, 50, 5)
print(nparray7)# [10., 20., 30., 40., 50.]

nparray8 = np.float32([[1, 2], [3, 4]])
print(nparray8)
                     
#Mathematical operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  
print(a - b)
print(a ** 2)
                     
print(np.sum(a))
print(np.max(a))
print(np.min(a))
print(np.mean(a))
print(np.median(a))
                     
#A numpy array filled random numbers
nparray10 = np.random.random((3, 4))
print(nparray10)
                     
#Index
nparray11 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(nparray11[0])

#Slicing
print(nparray11[0:4])
print(nparray11[2:8])
print(nparray11[2:100])
print(nparray11[::-1])

#Index with a 2 dimension numpy array
nparray12 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(nparray12)
print(nparray12[1, 1])
print(nparray12[:, 1])#All values at 1th column
print(nparray12[1, 1:4])#[6, 7, 8]
print(nparray12[-1,:])

#3 dimensions numpy array for Vector
nparray13 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(nparray13)
vector1 = nparray13.ravel()
print(vector1)

print(vector1.argmax())#It returns the index of the maximum value in Vector1
print(vector1.reshape((3, 3)))#It reshapes the vector to a numpy array with the shape of (3, 3) again.











                     

                     

                     

                     

                     

                     

                     