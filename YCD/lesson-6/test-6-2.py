i=0
while i<=5:
	j=0
	while j<=i:
		# print("*",j,end="")
		print("*",end="")
		j+=1
		pass	
	i+=1
	print("")
	pass	
else:
	print("END")

i=1
while i <=9:
	j=1
	while j<=i:
		print("%d*%d=%d" % (j,i,i*j), " ", end="")
		j+=1
		pass
	i+=1
	print("")
	pass

i=11
while i <=19:
	j=11
	while j<=i:
		print("%d*%d=%d" %  (j,i,i*j), " ", end="")
		j+=1
		pass
	i+=1
	print("")
	pass

i = 2
while i < 100:
	# print("Number is %d" %i)
	is_prime = True
	j = 2
	# ti = 0
	while j < i:
		if i % j==0:
			is_prime = False
			# print("j=%d"%j, " ", end="")
			# ti+=1
			break
		j += 1
	if is_prime:
		print("%d is Prime Number "%i)
	# else:
		# print("time is %d"%ti)
	i += 1