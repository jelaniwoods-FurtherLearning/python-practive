# using array-scalar type
import numpy as np

# ex 1
# dt = np.dtype(np.int32)
# print(dt)

#ex3
#int8, int16, int32, int64 can be replaced by == string 'i1', 'i2','i4', etc.
# dt = np.dtype('>i4')
# print(dt)

#ex4
#  the field name and the corresponding scalar data type is to be declared
# dt = np.dtype([('age',np.int8)])
# print(dt)

# ex5
# dt = np.dtype([('age',np.int8)])
# a = np.array([(10,),(20,),(30,)], dtype = dt)
# print(a)

#ex6
# file name can be used to access content of age column
# dt = np.dtype([('age',np.int8)])
# a  = np.array([(10,),(20,),(30,)], dtype = dt)
# print(a['age'])

# ex7
# student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
# print(student)

# ex8
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)
