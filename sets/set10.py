primes = set()
for num in range(2, 21):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.add(num)

odds = {num for num in range(2, 21) if num % 2 != 0}

print("Prime numbers between 2 and 20:", primes)
print("Odd numbers between 2 and 20:", odds)

un = odds.intersection(primes)
print(un)
inter = primes.intersection(odds)
print(inter)
diff = primes.difference(odds)
print(diff)
sym_diff = primes.symmetric_difference(odds)
print(sym_diff)
