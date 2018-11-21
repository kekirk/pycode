import Queue

from multiprocessing.managers import BaseManager





class QueueManager(BaseManager):
        pass



QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')


server_addr='192.168.1.79'
print('start to connect '+str(server_addr))

m = QueueManager(address=(server_addr,5000),authkey='abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
        n = task.get(timeout=10)
        r = n*n
        print('remoute ps compute res:'+str(r))
        result.put(r)

print("has been done")