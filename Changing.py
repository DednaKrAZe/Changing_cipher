alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key=['t','r','g','s','x','e','k','b','u','w','f','i','p','m','d','j','z','v','o','q','l','h','n','c','a','y']
text=input()
encrypted=''
for i in text:
    registr=0
    if i not in alpha and i.lower() not in alpha:
        encrypted+=i
    else:
        if i not in alpha:
            i=i.lower()
            registr=1
        ind=alpha.index(i)
        if registr==0:
            encrypted+=key[ind]
        else:
            inew=key[ind].upper()
            encrypted+=inew
print(encrypted)
