print("""The program will start at 0.
At what number should it end ?""")
range = input(">")
while not range.isdigit() or range != 0 or range != 1:
  print("You have to enter a positive number with no decimal greater than one.")
  range = input(">")
prime_numbers = [True]
