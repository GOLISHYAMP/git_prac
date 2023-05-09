import time
import threading

def fast():
    print("I am in fast method")
    time.sleep(1)
def slow():
    print("I am in slow method")
    time.sleep(5)



if __name__ == "__main__":
    last_exe_time = time.time()
    while True:
        # th = threading.Thread(name="func",target=func_call)
        # th.start()
        # time.sleep(1)
        curr_time = time.time() 
        fast()
        elapse_time = curr_time-last_exe_time
        if elapse_time > 5:

            slow()
            last_exe_time = time.time()