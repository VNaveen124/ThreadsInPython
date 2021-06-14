#threadex3.py
import time,threading
def multable(n):
	if(n<=0):
		print(n," is invalid input:")
	else:
		print("---------------------------------------------")
		print("Mul Table for :{}".format(n))
		print("---------------------------------------------")
		for i in range(1,11):
			print("{} x {}={}".format(n,i,n*i))
			time.sleep(0.5)
		print("---------------------------------------------")


#main program
n=int(input("Enter a number:"))
t1=threading.Thread(target=multable, args=(n,) )
t1.start()
