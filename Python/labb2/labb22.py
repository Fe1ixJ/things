def calculate_sum(x):
    weight = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
    total_sum = 0
    for i in range(9):
        product = x[i] * weight[i]  # Multiply the digit with the weight
        if product > 9:
            total_sum += product // 10  # Add the tens place digit
            total_sum += product % 10  # Add the ones place digit
        else:
            total_sum += product
    return total_sum

def check_pnr(x):
    total_sum = calculate_sum(x)
    if total_sum % 10 ==0:
        control_digit = 0
    else:
        control_digit = (total_sum//10+1)*10 - total_sum
    
    if control_digit == x[9]:  # Compare with the last digit in the list
        return True
    else:
        return False

print("Skriv in ditt personnummer (10 siffror utan mellanslag):")
number = input().strip()

if len(number) != 10 or not number.isdigit():
    print("Felaktigt format. Var god ange 10 siffror.")
else:
    digits = [int(digit) for digit in number]  # Convert the input string to a list of integers
    print(check_pnr(digits))