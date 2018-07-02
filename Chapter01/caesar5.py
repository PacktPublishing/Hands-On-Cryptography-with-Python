alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = raw_input("Enter ciphertext: ")

for shift in range(26):

  n = len(str_in)
  str_out = ""

  for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    newloc = (loc + shift)%26
    str_out += alpha[newloc]

  print shift, str_out

