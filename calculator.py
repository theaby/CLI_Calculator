#Calculator application which accepts two numbers and an action to perfrom
#End w/ restating the equation and the answer in a readable format
#Use the Try/Except in an infinite loop to continually ask for a value until it is valid

print('This is a basic calculator.\nI will ask for two numbers and an action.\n')

while (True):
    operand1 = input('First Number: ')
    try:
        operand1 = float(operand1)
        break
    except:
        print('That is an invalid number, let\'s try again.')

while (True):
    action = input('Action(+, -, /, or *: )')
    actionList = ['+', '-', '/', '*']
    if action in actionList:
        break
    else:
        print('Enter +, -, /, or *\nGive it another shot.')

while (True):
    operand2 = input('Second Number: ')
    try:
        operand2 = float(operand2)
        break
    except:
        print('That is an invalid number, let\'s try again.')

if action == '+': 
    result = operand1 + operand2
elif action == '-':
    result = operand1 - operand2
elif action == '/':
    if operand2 == 0: result = 'You can\'t divide by zero.'
    else: result = operand1 / operand2
elif action == '*':
    result = operand1 * operand2

print("\n")
print(operand1, action, operand2, "=", result)