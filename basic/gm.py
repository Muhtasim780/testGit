user_input = input( )
print('welcome to the game')
print("""
'start - to start the game'
'stop - to stop the game'
'quit - to exit the game
""")
command = ""
car_started = False
car_stopped = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if car_started:
            print('the car is already started')
        else:
            car_started=True
            print('car has started')
    elif command == 'turn left' or command == 'turn right':
        print('okay as you want')
    elif command == 'stop':
        if not car_started:
            print('the car never stared')
        elif car_stopped:
            print('car is already stopped')
        else:
            car_stopped=True
            print('okay stoped')
    elif command == 'quit':
        break
    else:
        print("sorry i don't understand that!")