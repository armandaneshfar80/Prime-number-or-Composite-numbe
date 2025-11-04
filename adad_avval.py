import time
start_time = time.time()

def click():
    while True:
        num = int(input("enter your number:"))
        if num ==0:
            print("end while")
            break
        if time.time() - start_time > 25:
            print("time up")
            break
        if num == 1:
            print("not avval and not morakkab")
        for i in range(2,num):
            if num % i == 0:
                print("morakkab")
                break
        else:
            print("avval")
click()