def fun1(num):
  return [x for x in range(1,num+1) if num%x == 0]
def fun2(num):
  return sum(fun1(num))
def fun3(num):
  numofelements = len(fun1(num))
  return fun1(num), fun2(num), numofelements

print(fun3(60))
