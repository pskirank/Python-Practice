"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1,101):
    list1 = [fibonacci(i)]
    print(list1)
   # print(dict(enumerate(list1, start = 1)))

"""
x = 0
list1 = []
while int(fibonacci(x)) < 4000000:
    list1.append(fibonacci(x))
    x += 1

print(list1)
"""