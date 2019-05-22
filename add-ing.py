print('enter string')
a=input()
b=len(a)
if b<3:
	print(a)
elif (a[-3:]!='ing'):
	print(a+'ing')
else:
	print(a.replace('ing','ly'))
