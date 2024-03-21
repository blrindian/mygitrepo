#using "del","remove" and "add" 
A = [1,2,3,"A","B","C"]
print(A)
del A[1]
print(A)
print("+" * 40)
A.remove(3)
A.remove("B")
print(A)
        
A = [1,2,3,"A","B","C"]
del A[0:2]

A = [10,20,30,40,50]
A = A + [60]
print(A)
A = A + list(str(607080))
A = A + list("ABC")
print(A)
print("=" * 40)

A = [10,20,30,60,100]
A.append(200)
A.append([10,20,30])
print(A)
A.insert(3,40)
print(A)
A.insert(5,[1,2,3,4,5])
print(A)

#Lists are mutable and strings are immutable
# We can modify list assingment

A = [100,200,300,400,500]
A[4] = 600
print(A)

#Tuples are like string, they are immutable.
#Once assigned cannot be changed.
#Multiple variables can be assigned.

my_tuple = (1,2,3,"a","b","c")
print(my_tuple,type(my_tuple),len(my_tuple))

A,B,C = (10,"h",45)
print(A)
print(B)
print(C)
