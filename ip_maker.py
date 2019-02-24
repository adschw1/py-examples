from random import randint

for i in range(0,10):
    ip = bin(randint(0,2**32))
    ip = ip[2:]
    first = ip[0:8]
    second = ip[8:16]
    third = ip[16:24]
    fourth = ip[24:]
    new_ip = str(int(first,2))+'.'
    new_ip += str(int(second,2))+'.'
    new_ip += str(int(third,2))+'.'
    new_ip += str(int(fourth,2))
    print new_ip
