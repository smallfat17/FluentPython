from time import perf_counter
import collections
import dis
import Lib
p0 = perf_counter()
for i in range(10**7):
    a = {range(10)}
print(perf_counter() - p0)  #2.188863558

p1 = perf_counter()
for i in range(10**7):
    a = set(range(10))

print(perf_counter() - p1) #3.760827926

p2 = perf_counter()
for i in range(10**7):
    a = {i for i in range(10)}
print(perf_counter() - p2)

