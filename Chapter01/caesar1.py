alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = raw_input("Enter message, like HELLO: ")

n = len(str_in)
str_out = ""

for i in range(n):
   c = str_in[i]
   loc = alpha.find(c)
   print i, c, loc, 
   newloc = loc + 3
   str_out += alpha[newloc]
   print newloc, str_out

print "Obfuscated version:", str_out


