dic={}
with open("./samyak_trace.txt", "r") as f1:
    lines=f1.readlines()
    # print(lines)
    for line in lines:
        # print(line)
        key=line.split(":")
        value=key[1]
        key=key[0]
        # print(key)
        dic[key]=value.split("=")[0]
    print("samyak_dic=",end="")
    print(str(dic))
