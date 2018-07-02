import hashlib

# bill:"":"":AAD3B435B51404EEAAD3B435B51404EE:5875F2524BBE45F3504236B75A9A483D
# ted:"":"":AAD3B435B51404EEAAD3B435B51404EE:3881DA787A2F7028E2B027386F6FA597

for c1 in "0123456789":
  for c2 in "0123456789":
    for c3 in "0123456789":
      p = c1 + c2 + c3
      hash = hashlib.new("md4", p.encode("utf-16le")).hexdigest()
      if hash[0:3] == "388":
        print p, hash
