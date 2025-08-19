Dict = {cnt : cnt ** 2 for cnt in range (1,11)}
print(Dict)
dict2 = {k :round(k**0.5,2) for k in Dict.keys()}
print(dict2)
dict3 = {k: v*3 for k , v in Dict.items()}
print(dict3)
Dict4 = {k: v for k, v in Dict.items() if (k % 2 != 0)}
print('Dict4 = ', Dict4)
Dict5 = {
    k if (k % 2 == 0) else k ** 3 :
    v if (v % 2 == 0) else v ** 3
    for k, v in Dict.items()
}
print('Dict5 = ', Dict5)


