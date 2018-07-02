import hashlib

p   = raw_input("Password:")
alg = raw_input("Algorithm (md5 or sha1):")
nr  = int( raw_input("# rounds:") )

h = p
for i in range(nr):
  h = hashlib.new(alg, h).hexdigest()

print nr, h


