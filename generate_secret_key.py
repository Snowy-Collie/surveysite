import os
secret_key = os.urandom(32).hex()
print(secret_key)