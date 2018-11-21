import Queue

from multiprocessing.managers import BaseManager


task_queue = Queue.Queue()
result_queue = Queue.Queue()




class QueueManager(BaseManager):
        pass




QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)


manager = QueueManager(address=('192.168.1.79',5000),authkey='abc')

print(manager)

manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

print("start distribute task")
for i in range(10):
        task.put(i)


print("start get result")
for i in range(10):
        r = result.get(timeout=10)
        print("result is :"+str(r))


manager.shutdown()