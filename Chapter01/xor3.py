text = raw_input("Enter text: ")
n = len(text)

for k in "0123456789":
  clear = ""
  for i in range(n):
    t = text[i]
    x = ord(k) ^ ord(t)
    clear += chr(x)
  print k, clear





 
