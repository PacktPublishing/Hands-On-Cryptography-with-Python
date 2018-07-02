texth = raw_input("Enter hex plantext: ")
text = texth.decode("hex")
n = len(text)

for k1 in "0123456789":
  for k2 in "0123456789":
    key = k1 + k2
    clear = ""
    for i in range(n):
      t = text[i]
      k = key[i%2]
      x = ord(k) ^ ord(t)
      clear += chr(x)
    print key, clear





 
