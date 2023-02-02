import time
import random
from multiprocessing import Process
from multiprocessing import current_process
def f():
<<<<<<< HEAD
   for i in range(5):
   print (f"hola soy {current_process().name}, " + \
      f"{current_process().pid}, {current_process().is_alive()}, vuelta {i}")
   time.sleep(random.random()/3)
def g():
   print ("adios")
if __name__ == "__main__":
   N = 3
   lp = []
   for i in range(N):
      lp.append(Process(target=f, name=f"ana_{i}"))
   for p in lp:
      p.start()
   q = Process(target=g)
   q.start()
   print ("fin")
=======
for i in range(5):
print (f"hola soy {current_process().name}, " + \
f"{current_process().pid}, {current_process().is_alive()}, vuelta {i}")
time.sleep(random.random()/3)
def g():
print ("adios")
if __name__ == "__main__":
N = 3
lp = []
for i in range(N):
lp.append(Process(target=f, name=f"ana_{i}"))
for p in lp:
p.start()
q = Process(target=g)
q.start()
print ("fin")
>>>>>>> 557304cbca84537ea9c1454c95de2ed85ca315a5
