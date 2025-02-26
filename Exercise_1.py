Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\user> py
Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import csv
>>> import numpy as np
>>> from typing import List
>>> def id_to_fruit(fruit_id:int, fruits:List[str])->str:
...     if not (0<=fruit_id<len(fruits)): #control index
...             raise IndexError(f"Fruit ID {fruit_id} is out of range.")
...     return fruits[fruit_id] #reach to fruit list
...
>>> fruits=["apple","orange","melon","kiwi","strawberry"] #test code
>>> print(id_to_fruit (1,fruits)) #orange
orange
>>> print(id_to_fruit (3,fruits)) #kiwi
kiwi
>>> print(id_to_fruit (4,fruits)) #strawberry
strawberry
>>>
