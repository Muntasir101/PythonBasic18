# Declare Function
def summation():
    number1 = 10
    number2 = 5
    print(number1+number2)

# Calling functions
summation()

# without parameters
def subtraction():
    number1 = 10
    number2 = 5
    print(number1 - number2)
subtraction()

# with parameters but without return
def subtraction_parameter(number1, number2):
    print(number1 - number2)

subtraction_parameter(20,30)

# with parameters and with return
def subtraction_parameter_return(number1, number2):
    return number1 - number2

result = subtraction_parameter_return(60,50)
print(result)

def summation_parameter_return(number1, number2):
    return number1 + number2

final_result = subtraction_parameter_return(50,10) + summation_parameter_return(10,80)
print(final_result)

