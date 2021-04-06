from apna_parsed import apna_dic
from rutvij_parsed import rutvij_dic
our_dic=apna_dic
correct=0
incorrect=0
for key in our_dic:
    if rutvij_dic[key].lower()!=our_dic[key].lower():
        incorrect+=1
        print(key)
    else:
        correct+=1

print(correct)
print(incorrect)