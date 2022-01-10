fib_numbers = {
1: 1, 
2: 1, 
3: 2, 
4: 3, 
5: 5
}

def fibbonaci(n):
  number = fib_numbers.get(n)
  while number == None:
     number = fibbonaci(n-2) + fibbonaci(n-1)
     fibbonaci[n] = number
  return number