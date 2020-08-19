tools={}
while(1):
    c=input()
    if(c=="q"):
        for k in tools.keys():print(k)
    else:
        tools[c]=0
