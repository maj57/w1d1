def currency_converter(value):
  cents = round(value * 100)
  
  print("You have:")
  
  hundreds = cents // (100 * 100)
  print(hundreds, "hundreds")
  cents = cents - hundreds * (100 * 100)
  
  fifties = cents // (50 * 100)
  print(fifties, "fifties")
  cents = cents - fifties * (50 * 100)
  
  twenties = cents // (20 * 100)
  print(twenties, "twenties")
  cents = cents - twenties * (20 * 100)
  
  tens = cents // (10 * 100)
  print(tens, "tens")
  cents = cents - tens * (10 * 100)
  
  fives = cents // (5 * 100)
  print(fives, "fives")
  cents = cents - fives * (5 * 100)
  
  ones = cents // 100
  print(ones, "ones")
  cents = cents - ones * 100
  
  quarters = cents // 25
  print(quarters, "quarters")
  cents = cents - quarters * 25
  
  dimes = cents // 10
  print(dimes, "dimes")
  cents = cents - dimes * 10
  
  nickels = cents // 5
  print(nickels, "nickels")
  cents = cents - nickels * 5 
  
  pennies = cents
  print(pennies, "pennies")
  return ""
