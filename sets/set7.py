prime = {cnt for cnt in range(2, 21) if all(cnt % i != 0 for i in range(2, int(cnt**0.5) + 1))}
print(prime)

