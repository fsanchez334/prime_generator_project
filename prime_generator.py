def prime_gen(n):
  list_of_numbers = []
  for x in range(n + 1):
    prime = prime_check_trial(x)
    if(prime):
      list_of_numbers.append(x)
  list_of_numbers.remove(0)
  list_of_numbers.remove(1)

  return list_of_numbers

def prime_check_trial(n):
  x = int(n ** 0.5)
  prime = True
  counter = 0
  for i in range(2, x + 1):
    if(n % i == 0):
      prime = False
  return prime

prime_gen(100)
