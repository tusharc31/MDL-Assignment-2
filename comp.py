from sir_parsed import sir_dic
from apna_parsed import apna_dic

correct=0
incorrect=0

for key in apna_dic:
    if sir_dic[key].lower().strip()!=apna_dic[key].lower().strip():
        incorrect+=1
        print("----------------")
        print(key)
        print("sir= ",sir_dic[key])
        print("APNA=",apna_dic[key])
    else:
        correct+=1

print(correct)
print(incorrect)
