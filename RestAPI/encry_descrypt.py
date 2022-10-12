from passlib.hash import pbkdf2_sha256
password = "Hello"
hashed = pbkdf2_sha256.hash(password)
print(hashed)

if pbkdf2_sha256.verify('Hello',hashed):
    print("password match successfully")
else:
    print("password didn't match")