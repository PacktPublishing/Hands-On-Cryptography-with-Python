from passlib.hash import sha512_crypt

p = raw_input("Password:")
s = raw_input("Salt:")

print sha512_crypt.using(salt=s, rounds=5000).hash(p)

