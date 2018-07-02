from passlib.hash import sha512_crypt

s = "penguins"

for ip in range(1000,2000):
  sp = str(ip)
  p = sp[1:]
  h = sha512_crypt.using(salt=s, rounds=5000).hash(p)
  if h[12:16] == "PcSL":
    print p, h
