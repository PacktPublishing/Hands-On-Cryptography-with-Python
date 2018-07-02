import hashlib

alg = "md5"
nr  = 100

for ip in range(1000,2000):
  sp = str(ip)
  p = sp[1:]
  h = p
  for i in range(nr):
    h = hashlib.new(alg, h).hexdigest()
  if h[0:3] == "c09":
    print p, h

