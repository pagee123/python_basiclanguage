import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)  # 模擬一個耗時操作
        print(f"Number: {i}")

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1.5)  # 模擬一個耗時操作
        print(f"Letter: {letter}")

# 創建執行緒
thread1 = threading.Thread(target=print_numbers)

# 啟動 thread1
thread1.start()

# 等待 thread1 完成
thread1.join()

# 創建和啟動 thread2
thread2 = threading.Thread(target=print_letters)
thread2.start()

# 等待 thread2 完成
thread2.join()

print("Both threads have finished execution.")
