def decodeAtIndex(s, k):
    decoded_length = 0
    
    for char in s:
        if char.isalpha():
            decoded_length += 1
        elif char.isdigit():
            repeat = int(char)
            decoded_length *= repeat

    for char in reversed(s):
        k %= decoded_length
        if k == 0 and char.isalpha():
            return char
        if char.isalpha():
            decoded_length -= 1
        else:
            repeat = int(char)
            decoded_length //= repeat

print(decodeAtIndex("cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg", 480551547))