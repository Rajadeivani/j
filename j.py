def fizz_buzz(n):
    if n%5==0:
        return 'FizzBuzz'

    elif n % 5==0:
        return 'Buzz'
    else:
        return n

for num in range(1,100):
    print(fizz_buzz(num))
