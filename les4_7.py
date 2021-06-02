from itertools import count

def fact(n):
    result = 1
    for el in count(1):
        if el > n: 
          break
        result = el*result
    yield result

number = 4 '''факториал, который хотим вычислить'''
str_ = "{}! = ".format(number)

for el in range(1,number+1):
  if el == number:
    str_ += "{} = ".format(el)
  else:
    str_ += "{} * ".format(el)
for el in fact(number):
  str_ += "{}".format(el)

print(str_)
