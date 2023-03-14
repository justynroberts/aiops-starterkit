import json
# used to jsonify code
code = """

import random
import string
 
use_digits_answer = input("Use digits [y]/n: ")
if use_digits_answer.lower() == "n":
    use_digits = False
else:
    use_digits = True
 
use_punctuation_answer = input("Use special characters [y]/n: ")
if use_punctuation_answer.lower() == "n":
    use_punctuation = False
else:
    use_punctuation = True
 
password_length_answer = input("Length of the password [10]: ")
if password_length_answer == "":
    password_length = 10
else:
    password_length = int(password_length_answer)
 
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
 
symbols = letters
if use_digits:
    symbols += digits
if use_punctuation:
    symbols += punctuation
 
password = "".join(random.choice(symbols) for i in range(password_length))
print(password)




"""


a = json.dumps(code)

print (a)

