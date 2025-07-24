import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    print("Stopwatch started. Press Enter to stop.")
    
    input()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    mins, secs = divmod(elapsed_time, 60)
    millis = (elapsed_time - int(elapsed_time)) * 1000

    print(f"\nElapsed Time: {int(mins):02d}:{int(secs):02d}.{int(millis):03d} (mm:ss.ms)")

if __name__ == "__main__":
    stopwatch()
