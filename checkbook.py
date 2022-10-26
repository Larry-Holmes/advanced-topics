# main import
import os

# provides navigation between menu options
def option_select(choice):

    '''
    Parameter = number as a string/object
    Returns different features dependent on number passed via choice variable.
    '''
    if choice == '1':
        
        balance = check_bal()
        print()
        print(f'Your current balance is ${balance}')
    elif choice == '2':
        
        balance = check_bal()
        withdraw(balance)

    elif choice == '3':
        
        balance = check_bal()
        deposit(balance)
        
    elif choice == '4':
        
        print()
        print('Thanks, have a great day!')
    else:
        print()
        print(f'Invalid choice: {choice}')


def withdraw(balance):

    '''
    Parameter = pass in text from balance.txt file
    Returns a new balance.txt file with an updated balance.
    '''
    debit = input('How much is the debit?')

    balance = float(balance) - float(debit)
    balance = str(balance)

    with open('balance.txt', 'w') as b:
        b.write(balance)





def deposit(balance):

    '''
    Parameter = pass in text from balance.txt file
    Returns a new balance.txt file with an updated balance.
    '''
    
    credit = input('How much is the credit?')

    balance = float(balance) + float(credit)
    balance = str(balance)

    with open('balance.txt', 'w') as b:
        b.write(balance)

    # return balance

def check_bal():

    '''
    Returns a balance.txt file with text that describes the current balance of the users account.
    '''

    if os.path.exists('balance.txt') == True:

        with open('balance.txt') as b:
            
            balance = b.read()

        return balance
    
    else:

        with open('balance.txt', 'w') as b:
            balance = '0'
            b.write(balance)
        return balance


# establishes orignial checkbook balance
balance = check_bal()

# establishes entry into while loop
choice = 1

# creates while loop to allow user to navigate the menu until they want to exit
while choice != '4':
    print()
    print('What would you like to do?\n',
        '1) view current balance \n',
        '2) record a debit (withdraw) \n',
        '3) record a credit (deposit) \n',
        '4) exit')

    choice = input('Your choice? ')
    option_select(choice)


