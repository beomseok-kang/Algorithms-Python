import queue
import threading

q = queue.Queue()

def worker(num):
    while True:
        item = q.get()
        if item is None:
            break
        # 작업 처리
        print("스레드 {0}: 처리 완료 {1}".format(num+1, item))
        q.task_done()

# 스레드 정의
num_worker_threads = 5
threads = []

# 스레드에 작업 추가
for i in range(num_worker_threads):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

# 큐에 아이템 20개 추가
for item in range(20):
    q.put(item)

q.join()

for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()