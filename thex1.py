#thex1.py
import threading
print("Name of thread present in this Program=",threading.current_thread().getName())#main therad																									
print("Enter a numner:")
a=int(input())
res=a*a
print("square({})={}".format(a,res))
