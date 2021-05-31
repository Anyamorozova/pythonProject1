from itertools import cycle, count
 
for el in count(10):
    if el > 20:
        break
    print(el)

my_list = ["test1","test2","test3"]
count_ = 0
for el in cycle(my_list):
    if count_ > 10:
        break
    print(el)
    count_ += 1
