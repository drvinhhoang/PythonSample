
import re

email = input("what's your email? ").strip()

if re.search(r"ˆ.+@.+\.edu$", email):
    print("valid")
else:
    print("invalid")