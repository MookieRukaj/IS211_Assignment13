def fibonacci(n):
    if n < 0:
        print ("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print (fibonacci(13))

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

print(gcd(11, 5))

def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])

print (compareTo('first', 'second'))
print (compareTo('equal', 'equal'))
print (compareTo('second', 'first'))
