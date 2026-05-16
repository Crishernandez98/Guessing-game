import random

def random_num():
    random_number = random.randint(1,100)
    
    while True:
        try:
            user_input = int(input("Guess a number: "))
        except ValueError:
            print("Invalid input")
            continue
        if user_input > random_number:
            return 'Low'
        if user_input < random_number:
                print('Higher')
                pass
        if random_number == user_input:
                print('Correct')
                return
print(random_num())