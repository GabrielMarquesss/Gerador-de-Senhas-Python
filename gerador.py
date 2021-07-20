import random
import sys
from string import digits
from string import punctuation
from string import ascii_letters
from numbers import Number

symbols = ascii_letters + punctuation + digits + str(Number)
secure_random = random.SystemRandom()
passwd = "".join(secure_random.choice(symbols)
                for i in range(20))
sys.stdout = open('output.txt', 'w')
print(passwd)
sys.stdout.close()