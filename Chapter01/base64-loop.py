a = raw_input("Enter encoded text:")

for i in range(6):
  a = a.decode("base64")
  print i, a
