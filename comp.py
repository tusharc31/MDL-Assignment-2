from avi_trace import avi_dic
from apna_parsed import apna_dic

correct=0
incorrect=0

for key in apna_dic:
    if avi_dic[key].lower().strip()!=apna_dic[key].lower().strip():
        incorrect+=1
        print("----------------")
        print(key)
        print("AVI= ",avi_dic[key])
        print("APNA=",apna_dic[key])
    else:
        correct+=1

print(correct)
print(incorrect)
