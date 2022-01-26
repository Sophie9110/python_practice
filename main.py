state_start=True
state_stop=True
while True:
    information=input("> ")
    if information=="help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""")
    elif information=="start":
        if state_start:
            state_start=False
            print("Car started...Ready to go")
        else:
            print("Car alredy has started")
    elif information=="stop":
        if state_stop:
            state_stop=False
            print("Car stopped.")
        else:
            print("Car alredy has stopped")
    elif information=="quit":
        break
    else:
        print("I don't understand that... ")

