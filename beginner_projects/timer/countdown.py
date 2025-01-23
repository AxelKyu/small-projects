import time

def countdown():
    timer_length = int(input("Time Length in seconds: "))
    temp = 0

    for i in range (timer_length, 0, -1):
        print (f"{i}s")
        time.sleep(1)
    
    print ("Times Up!")

if __name__ == "__main__":
    countdown()
