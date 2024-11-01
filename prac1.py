age = int(input('How old are you?'))

def is_adult(age):
    if age >= 18 and age < 35:
        print('yeah buddy')

    elif age > 35:
        print('too old')

    else:
        print("young nigger")

is_adult(age)