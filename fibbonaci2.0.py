fib_numbers = {
1: 1, 
2: 1, 
3: 2, 
4: 3, 
5: 5
}

def fibbonaci(n):
  number = fib_numbers.get(n)
  if number is None:
     number = fibbonaci(n-2) + fibbonaci(n-1)
     fib_numbers[n] = number
  return number

# благодаря запоминанию расчетов, алгоритм на считает числа по два раза, 
# поэтому сложность равна О(n) 