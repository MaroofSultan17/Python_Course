
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2


dic = {"+": add,
       "-": sub,
       "*": mul,
       "/": div
       }

number_1 = float(input("Enter the number : "))
for key in dic:
    print(key)
cont = False
answer = 0
operation_symbol = input("Pick an operator : ")
number_2 = float(input("Enter the next number : "))
cal_function = dic[operation_symbol]
answer = cal_function(round(number_1, 2), round(number_2, 2))
print(f"{number_1} {operation_symbol} {number_2} = {round(answer, 2)}")
while not cont:
    should_cont = input(f"Type 'yes' to continue Calculating with {answer} , or type 'no' to exit: ").lower()
    if should_cont == "yes":
        operation_symbol1 = input("Pick an operator : ")
        number_3 = float(input("Enter the next number : "))
        cal_function1 = dic[operation_symbol1]
        answer1 = cal_function1(answer, number_3)
        print(f"{answer} {operation_symbol1} {number_3} = {round(answer1, 2)}")
        answer = answer1
        cont = False
    elif should_cont == "no":
        cont = True
