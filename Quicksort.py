# ALLYYA NUR AZIZAH | 2209116030

import os
os.system('cls')
from random import randint

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

list_data = [] # merupakan syntax membuat list kosong menggunakan module import random
for i in range(10): # menggunakan for i in range() untuk banyak angka didalam list
    batas = randint(0,50) # menggunakan randint() untuk menentukan range angka yang akan muncul 
    list_data.append(batas)

print('Sebelum dilakukan QuickSort : ',  list_data)
quickSort(list_data,0,len(list_data)-1)
print('Setelah dilakukan QuickSort : ', list_data)