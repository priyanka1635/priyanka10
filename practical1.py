Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=[10,20,30,40]
x.insert(2,50)
print(x)
[10, 20, 50, 30, 40]
p={}
print("Type of p:",type(p))
Type of p: <class 'dict'>
s=set()
print(s)
set()
print("Type of s:",type(s))
Type of s: <class 'set'>
product={ "pid":101,"pname":'book'}
print("Data in Dictionary :",product)
Data in Dictionary : {'pid': 101, 'pname': 'book'}
product['price']=200
print("Data in Dictionary :",product)
Data in Dictionary : {'pid': 101, 'pname': 'book', 'price': 200}
a=(4,3,8,20)
x=list(a)
>>> print("List :",x)
List : [4, 3, 8, 20]
>>> student={"Rollno":101,"Name":'priya'}
>>> print("Name of Student : ",student["Name"])
Name of Student :  priya
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> import numpy as np
>>> x = np.array([4, 5, 6, 7, 8])
>>> print(x)
[4 5 6 7 8]
>>> type(x)
<class 'numpy.ndarray'>
>>> x=np.array(([1,4,3,10]),dtype="float")
>>> type(x)
<class 'numpy.ndarray'>
>>> x = np.zeros((3, 4))
>>> print(x)
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
>>> x=np.ones((3,4))
>>> print(x)
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
>>> x = np.full((3, 4), 7)
>>> print(x)
[[7 7 7 7]
 [7 7 7 7]
 [7 7 7 7]]
>>> x=np.eye(3,3)
>>> print(x)
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
>>> x = np.arange(2, 10, 3)
>>> print(x)
[2 5 8]
>>> x = np.linspace(7, 10, 10)
>>> print(x)
[ 7.          7.33333333  7.66666667  8.          8.33333333  8.66666667
  9.          9.33333333  9.66666667 10.        ]
