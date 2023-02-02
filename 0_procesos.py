from time import sleep
from random import random
"""
DocumentaciÃ³n multiprocessing
https://docs.python.org/3.6/library/multiprocessing.html
"""
from multiprocessing import Process
def f():
<<<<<<< HEAD
   for i in range(5):
      print ("hola", i)
      sleep(random())
if __name__ == "__main__":
   p = Process(target=f)
   q = Process(target=f)
   p.start()
   q.start()
   print ("fin")
=======
for i in range(5):
print ("hola", i)
sleep(random())
if __name__ == "__main__":
p = Process(target=f)
q = Process(target=f)
p.start()
q.start()
print ("fin")
>>>>>>> 557304cbca84537ea9c1454c95de2ed85ca315a5
