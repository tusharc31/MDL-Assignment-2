from apna_doosra import apna_dic
from rutvij_init import rutvij_orgdic
our_dic=apna_dic
rutvij_dic=rutvij_orgdic
correct=0
incorrect=0
for key in our_dic:
    if rutvij_dic[key].lower()!=our_dic[key].lower():
        incorrect+=1
        print("----------------")
        print(key)
        print(rutvij_dic[key])
        print(apna_dic[key])
    else:
        correct+=1

print(correct)
print(incorrect)