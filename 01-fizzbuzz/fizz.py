
#fizzbuzz

def fizz(num):
  for num in range(1,num):
    if (num%3 == 0) and (num%5 == 0):
      print('FizzBuzz')
    elif num == 3 or (num%3 == 0):
      print('Fizz')
    elif num == 5 or (num%5 == 0):
      print('Buzz')
    else:
      print(num)
  return ''
print(fizz(20))
