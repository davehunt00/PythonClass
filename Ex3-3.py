# Exercise 3.3
# Dave Hunt
# 10/13/12


def right_justify(s):
   count = 70 - len(s)
   pad = ''
   
   while count > 0:
     pad = pad + '.'
     count = count - 1	
	 
   print pad + s
   
right_justify("This is some text")
right_justify("This is much longer than that")





