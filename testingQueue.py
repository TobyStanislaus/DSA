import queue

'''
#q=queue.Queue()
q=queue.LifoQueue()

numbers=[1,2,3,4,5,6,7]

for x in numbers:
  q.put(x)

print(q.get())
'''

q = queue.PriorityQueue()


q.put((2,1))
q.put((3,6))

