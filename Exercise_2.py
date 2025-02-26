Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\user> py
Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> def swap(coords:np.ndarray)->np.array:
...     coords_copy=coords.copy()
...     coords_copy[:,[0,1,2,3]]=coords[:,[1,0,3,2]] #[x1,x2,y1,y2]
...     return coords_copy
...
>>> coords=np.array([[10,5,15,6,0],[11,3,13,6,0],[5,3,13,6,1],[4,4,13,6,1],[6,5,13,16,1]]) #test code
>>> swapped_coords=swap(coords)
>>> print(swapped_coords)
[[ 5 10  6 15  0]
 [ 3 11  6 13  0]
 [ 3  5  6 13  1]
 [ 4  4  6 13  1]
 [ 5  6 16 13  1]]
>>>
