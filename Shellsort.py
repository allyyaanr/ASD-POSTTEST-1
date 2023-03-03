# ALLYYA NUR AZIZAH | 2209116030

import os
os.system('cls')
from random import randint # module ini digunakan untuk menampilkan angka pada list kosong

def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

list_data = [] # merupakan syntax membuat list kosong menggunakan module import random
for i in range(10): # menggunakan for i in range() untuk banyak angka didalam list
    batas = randint(0,50) # menggunakan randint() untuk menentukan range angka yang akan muncul 
    list_data.append(batas)

print('Sebelum dilakukan ShellSort : ', list_data)

size = len(list_data)
shellSort(list_data, size)

print('Setelah dilakukan ShellSort : ', list_data)