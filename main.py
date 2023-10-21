import time
from BreadthFirstSearch import BreadthFirstSearch

fp = open("SampleFile.txt", 'r')
lines = fp.readlines()

start = time.time()
m = BreadthFirstSearch()
print(m.compute(lines))
print(m.Person1())
print(m.Person2())
end = time.time()
print("time: "+ str(end-start))
