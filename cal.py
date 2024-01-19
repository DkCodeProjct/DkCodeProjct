def main():
    
    user = isValid('FIND-> 1.Age / 2.BirthYear: \nENTER:[1/2] ')
    if user == 1:
        while True:
            try:
                birthYear = int(input('EnterBirthYear: '))
            except ValueError:
                pass
            else:
                outPut0 = 2024 - birthYear
                print(f'yourAge: {outPut0}')
                break
    else:
        while True:
            try:
                age = int(input('EnterAge: '))
            except ValueError:
                print('invlaidInput')
            else:
                outPut1 = 2024 - age
                print(f'YourBirthYear: {outPut1}')
                break

    

def isValid(prompt):
    while True:
        try:
            user = int(input(prompt))
        
            if user  in [1,2]:
                return user
            else:
                print('invlaidInput...')
            
        except ValueError:
            pass
if __name__ == "__main__":
    main()