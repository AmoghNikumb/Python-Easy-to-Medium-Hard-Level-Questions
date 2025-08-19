List = [1,2,3,4,5,6]
Dict = {'Key Num :'+ str(cnt): cnt **2 for cnt in List}
print(List)
print(Dict)
Dict2 ={cnt :Dict[cnt] for cnt in Dict}
print(Dict2)