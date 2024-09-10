import time

def pomodoro():
    count = int(input('choisire le temps : '))
    while count != 0:
        count -= 1
        time.sleep(1)
    print('time up')

if __name__ == "__main__":
    pomodoro()