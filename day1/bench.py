import timeit
import sys

sys.setrecursionlimit(15000)


with open("input.txt") as f:
    text = f.read().strip()




from iterative import iterative
time = timeit.timeit("iterative(text)", number=10000,
                     globals={"iterative": iterative, "text": text})
print("iterative", time)



from recursive import recursive
time = timeit.timeit("recursive(text)", number=10000,
                     globals={"recursive": recursive, "text": text})
print("recursive", time)


from bluespan import bluespan
time = timeit.timeit("bluespan(text)", number=10000,
                     globals={"bluespan": bluespan, "text": text})
print("bluespan", time)


from golf import golf
time = timeit.timeit("golf(text)", number=10000,
                     globals={"golf": golf, "text": text})
print("golf", time)
