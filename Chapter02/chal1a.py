import hashlib

for c1 in "0123456789":
  p = c1 
  hash = hashlib.new("md4", p.encode("utf-16le")).hexdigest()
  print p, hash

