import random
import time
while(1):
    l=['a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t','u',
    'v','w','x','y','z']
    v=['a','e','i','o','u']
    #num=int(input('Enter Word Length '))
    #print(len(l))

    Startup=[]
    for i in range(5):

        x=random.randint(0,25)
        y=l[x]
        Startup.append(y)
        
        #print(l[x])
        
    vowel_list=[]
    for j in range(2):
        
        vowel=random.randint(0,4)
        sel=v[vowel]
        vowel_list.append(sel)
        
        #print(v[vowel])

    final=''
    #print(vowel_list)
    Startup[1]=vowel_list[0]
    Startup[-1]=vowel_list[1]
    final=final.join(Startup)
    final=final.title()
    print(f'{final} in Bahria Enclave ')
    time.sleep(2)







    




