# Write a Python program that invoke square root function after specific milliseconds.
import math
import time
n = int(input())
t = int(input())
time.sleep(t/1000) # функция sleep(), что позволяет отсрочить выполнение вызываемого потока на указанное количество секунд.

print("Square root of", n, " after", t, "miliseconds is", math.sqrt(n))