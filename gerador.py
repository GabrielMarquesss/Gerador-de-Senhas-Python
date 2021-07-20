import random
import sys
from string import digits
from string import punctuation
from string import ascii_letters
from numbers import Number

#Variável que pega todos os dígitos disponíveis das bibliotecas acima
symbols = ascii_letters + punctuation + digits + str(Number)
#Gerador de números aleatórios com base no OS
secure_random = random.SystemRandom()
#Criação da senha, para alterar o tamanho de caracteres da mesma, mude o número do range
passwd = "".join(secure_random.choice(symbols)
                for i in range(20))
#Cria/Abre e escreve no arquivo txt onde as senhas serão armazenadas
with open('output.txt','a') as senhas:
    senhas.write(passwd)
    senhas.write('\n')