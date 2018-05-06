
def fizzbuzz(num):

     print('\n'.join([str(n) if n % 3 != 0 and n % 5 != 0 else ('fizz' if n % 3 == 0 else '') + ('buzz' if n % 5 == 0 else '') for n in range(1, num+1)]))
