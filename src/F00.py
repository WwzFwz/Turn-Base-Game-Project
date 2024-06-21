# RANDOM NUMBER GENERATOR VIA LCG ALGORITHM
import time
import datetime
"""
Random Number Generator (RNG) akan digunakan untuk menghasilkan bilangan acak dari 
sebuah Range angka. Fitur ini akan digunakan untuk berbagai fitur, terutama pada 
Monster dan Battle. Implementasi RNG dilarang menggunakan library random python 
dan harus menggunakan algoritma Linear Congruential Generator (LCG).
"""

def randomNumberGenerator(bottom:float, top:float):
    # bottom = batas bawah range nilai
    # top = batas atas range nilai
    # inisiasi nilai m, a, c, dan seed untuk LCG (most optimal values)
    m = 2**32
    a = 1103515245
    c = 12345  # ngambil waktu sekarang -> diconvert jadi int
    time.sleep(0.005)
    #seed
    current_time_ns = time.time_ns()
    microseconds = datetime.datetime.now().microsecond
    seed = current_time_ns + microseconds
    randomNumber = ((a * seed + c) % m) / m 
        
    randomNumber = randomNumber * (top - bottom) + bottom  # scale and shift ke range yang diinginkan
    return int(randomNumber) # ngembaliin nilai random



