# Exercise 3.4
# Dave Hunt
# 10/13/12


def do_twice(f,s):
   f(s)
   f(s)
   
def print_spam(s):
   print s

def print_twice(s):
   print s
   print s

def do_four(f,s):
	f(s)
	f(s)
   
#do_twice(print_twice,'spam')

do_four(print_twice,'spam')









