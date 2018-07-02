import hashlib

alg = "sha1"
nrmax  = 5000

for ip in range(1000,2000):
  sp = str(ip)
  p = sp[1:]
  h = p
  for i in range(nrmax):
    h = hashlib.new(alg, h).hexdigest()
    if h[0:5] == "f6dc2":
      print i+1, "rounds: password =", p, "Hash = ",  h

