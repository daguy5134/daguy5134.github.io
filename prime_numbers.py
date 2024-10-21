print("""The program will start at 0.
At what number should it end ?""")
while True:
    repeat_range = input(">")
    repeat_range = repeat_range.replace(" ", "")
    try:
        repeat_range == int(repeat_range)
        if int(repeat_range) < 0:
            raise ValueError
        elif int(repeat_range) >= 0:
            break
    except ValueError:
        print("You have to enter a positive number with no decimal greater than one.")
prime_numbers = [True] * (int(repeat_range) + 1)
prime_numbers[0] = prime_numbers[1] = False
for base_number in range(0, int(int(repeat_range) ** 0.5 + 1)):
    if prime_numbers[base_number]:
        for multiples in range(base_number ** 2, int(repeat_range) + 1, base_number):
            prime_numbers[multiples] = False
final_list = [nb for nb in range(int(repeat_range) + 1) if prime_numbers[nb]]
print(f"The prime numbers up to {repeat_range} are :{final_list}")
exit()
