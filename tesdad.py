x= input()
licznik=0
lista=[]
for i in range(0, len(x)):
    for j in range(1,len(x)+1):
        znak=x[i:j]
        #print(f"znak: {znak}")
        pos = x.find(znak)
        while pos != -1: # Jeśli znaleziono
           str = x[:pos] + x[pos+len(znak):] 
           #print(f"str: {str}")
           pos = x.find(znak, pos + 1)
           flaga=True
           ready=0
           if(str[::-1]!=str):
                for i in range(0,len(str)):
                    for j in range(1,len(str)+1):
                        print(f"reverse : {str[i:j][::-1]} normal: {str[i:j]} len: {len(str[i:j])}")
                        if(str[i:j][::-1]==str[i:j] and len(str[i:j])>=2):
                            #print(f"str reverse :{str[i:j][::-1]}")
                            #`print(str[i:j]c)
                            flaga=False
                            #ready=str
                            break 
                        
                    break   
                fl=True  
                if flaga and str not in lista:
                    lista.append(str)
                    print(f"str_ready : {str}") 
                
                        
                
print(licznik)               
for i in lista:
    print(f"i: {i}")         