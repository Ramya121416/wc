import re
import sys      
# takes argument from command line as (python3  wc.py  text_file_name  any_arguments(-l,-w,-c)(optinal))
# -l -> count number of lines
# -w -> count number o words
# -c -> count number of characters
f = open(sys.argv[1],"r")
context = f.read()
f.close()
x=context.lower().split()

number_of_words  = len(x)
number_of_characters = len(context)
read_lines = context.splitlines()


if(len(sys.argv) >2):
  if(sys.argv[2] =="-l"):
     print(len(read_lines),end =" ")
  elif(sys.argv[2] == "-w"):
     print(number_of_words,end =" ")
  elif(sys.argv[2] == "-c"):
     print(number_of_characters,end =" " )
else : 
     print(( number_of_words), end =" " )
     print( (number_of_characters),end =" " )
     print((len(read_lines)),end =" " )
print(sys.argv[1])
f.close()
