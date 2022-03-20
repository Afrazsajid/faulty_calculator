value1=int(input("enyter value no 1:  "))
opertor=input('enter opretor\t')
value2=int(input('enter value no 2: '))
if(value1==45 and value2==3 and opertor=='*'):
	answer=555
	print(answer)
elif(value1==56 and value2==9 and opertor=='+'):
	answer=77
	print(answer)
elif(value1==56 and value2==6 and opertor=='/'):
	answer=4
	print(answer)
elif(opertor=='*'):
	answer=value1*value2
	print(answer)
elif(opertor=='+'):
	answer=value1+value2
	print(answer)
elif(opertor=='-'):
	answer=int(value1-value2)
	print(answer)
elif(opertor=='/'):
	answer=value1/value2
	print(answer)
elif(opertor=='√'):
	operator=1/value2
	answer=int(value1**operator)
	print(answer)
