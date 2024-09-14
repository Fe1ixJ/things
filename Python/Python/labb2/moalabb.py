def siffersumma(personnummer):
    a = []
    for i in range(len(personnummer) - 1):
        siffror = int(personnummer[i])
        if i % 2 == 0:
            a.append(siffror * 2)
        else:
            a.append(siffror)

    siffersumma = 0
    for i in a:
        if i > 9:
            siffersumma += i % 10 + 1
        else:
            siffersumma += i

    return siffersumma

def kontrollsiffra(siffersumman):
    total_sum = siffersumma(personnummer)
    if total_sum % 10 ==0:
        control_digit = 0
    else:
        control_digit = (total_sum//10+1)*10 - total_sum
    return total_sum



def check_pnr(personnummer):
    control_digit= kontrollsiffra(personnummer)
    if control_digit == siffersumma[9]:  # Compare with the last digit in the list
        return True
    else:
        return False

personnummer = input("skriv in ditt personnummer: ")
check_pnr(personnummer)