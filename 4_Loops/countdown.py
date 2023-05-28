import time

seconds = int(input("Enter the number of seconds to wait for: "))

while seconds > 0:
    print("Waiting for: " + str(seconds))
    time.sleep(1)
    seconds -=1

print("Time is Up!")