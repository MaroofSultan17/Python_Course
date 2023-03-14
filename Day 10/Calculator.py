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

number_1 = float(input("Enter the number 1 : "))
for key in dic:
    print(key)
operation_symbol = input("chose any operator : ")
number_2 = float(input("Enter the number 2 : "))
cal_function = dic[operation_symbol]
answer = cal_function(round(number_1, 2), round(number_2, 2))
print(f"{number_1} {operation_symbol} {number_2} = {round(answer, 2)}")
