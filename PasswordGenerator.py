import random

lower = "abcdefghijklmnopqrstuvwxyz"

upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

NUMBER = "0123456789"

Symbol = "[]{}#()*; ._-"

all=lower + upper + NUMBER+ Symbol

length = 9

password = "admin".join(random.sample(all, length))

print(" The Password You Generated is :", password)

