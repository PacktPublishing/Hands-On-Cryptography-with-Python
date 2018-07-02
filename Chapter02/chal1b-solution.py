import hashlib

# bill:"":"":AAD3B435B51404EEAAD3B435B51404EE:5875F2524BBE45F3504236B75A9A483D

for c1 in "0123456789":
  for c2 in "0123456789":
    p = c1 + c2 
    hash = hashlib.new("md4", p.encode("utf-16le")).hexdigest()
    if hash[0:3] == "587":
      print p, hash
