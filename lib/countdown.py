from time import sleep

def countdown(num):
    while num > 0:
        print(f"{num} SECOND(S)!")
        num -= 1
    else:
        print("HAPPY NEW YEAR!")

def countdown_with_sleep(num):
    while num > 0:
        print(f"{num} SECOND(S)!")
        num -= 1
        sleep(1)
    else:
        print("HAPPY NEW YEAR!")
