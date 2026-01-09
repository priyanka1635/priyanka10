Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> x=np.array([0,1,2,3],[4,5,6,7],[8,9,10,11])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x=np.array([0,1,2,3],[4,5,6,7],[8,9,10,11])
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
>>> x=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
>>> print(x)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
>>> print(x[0,0:2])
[0 1]
>>> print(x[0,1:])
[1 2 3]
>>> print(x[0:2,1:0])
[]
>>> print(x[1:2,0:1])
[[4]]
>>> print(x[1:3,1:4])
[[ 5  6  7]
 [ 9 10 11]]
>>> print(x[1:,0:1])
[[4]
 [8]]
>>> KeyboardInterrupt
>>> print(x[1:2,:1])
[[4]]
>>> print(x[1:,1:])
[[ 5  6  7]
 [ 9 10 11]]
>>> a=np.array([[8,20,24,25],[30,35,36,40],[42,43,47,50][49,51,52,53]])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a=np.array([[8,20,24,25],[30,35,36,40],[42,43,47,50][49,51,52,53]])
TypeError: list indices must be integers or slices, not tuple
>>> import pandas as pd
