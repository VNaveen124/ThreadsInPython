#currentthredex1.py
import threading
print("i am from python program")
t=threading.current_thread()
print("type of t=", type(t))  # <class, 'thrading.Thread'>
print("Name of thread=",t.getName())
t.setName("KVR")
print("Name of thread=",t.getName())
