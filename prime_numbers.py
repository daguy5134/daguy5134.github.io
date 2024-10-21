print("""The program will start at 0.
At what number should it end ?""")
repeat_range = input(">")
while not repeat_range.isdigit() or range != 0 or range != 1:
    print("You have to enter a positive number with no decimal greater than one.")
    repeat_range = input(">")
prime_numbers = [True] * (int(repeat_range) + 1)
for base_number in range(0, int(repeat_range)):
    if prime_numbers[base_number]:
        for multiples in range(base_number ** 2, int(repeat_range) // base_number + 1):
        


exit()
