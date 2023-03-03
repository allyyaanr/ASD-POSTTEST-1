# ALLYYA NUR AZIZAH | 2209116030

import os
os.system('cls')
from random import randint

def mergesort(arr): #untuk membagi list
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #variable memecah list
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge (left,right)

def merge(left, right):
    result = [] #list kosong digunakan untuk menampung nilai

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    elif right:
        result += right
    return result


list_data = [] # merupakan syntax membuat list kosong menggunakan module import random
for i in range(10): # menggunakan for i in range() untuk banyak angka didalam list
    batas = randint(0,50) # menggunakan randint() untuk menentukan range angka yang akan muncul 
    list_data.append(batas)

print('Sebelum dilakukan Mergesort : ',  list_data)
akhir = mergesort(list_data)
print('Setelah dilakukan Mergesort : ', akhir)