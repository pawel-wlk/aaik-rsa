import math

def fast_modulo_power(n, power, mod):
    result = 1
    binary_power = bin(power)[2:]

    for i in range(len(binary_power)-1, -1, -1):
        if binary_power[i] == '1':
            result = result * n % mod
        n = n*n % mod

    return result

def factorize(n):
    result = []
    k=2
    while n > 1 and k < math.sqrt(n):
        while n%k == 0:
            result += [k, int(n/k)]
            n /= k
        k+=1
    return result

def extended_gcd(a, b):
    s = 0
    t = 1
    old_s = 1
    old_t = 0
    while b != 0:
        q = a//b
        a, b = b, a%b
        old_s, s = s, old_s - q*s
        old_t, t = t, old_t - q*t
    return (a, old_s, old_t)


###
print("Tekst po odszyfrowaniu:")

with open("data.txt", 'r') as file:
    data = file.read().strip('\n').split(": ")

data = [chr(fast_modulo_power(int(i, 16), 2062465, 101080891)) for i in data]

print(''.join(data))

print("\nFaktoryzacja liczby 101080891:", tuple(factorize(101080891)))

phi=1

for i in factorize(101080891):
    phi *= i-1

e = extended_gcd(2062465, phi)[1]

print("\nKlucz publiczny:", (e, 101080891))

