x= input()
def str_is_palindrome(s):
    return s == s[::-1]
    
def palindrom_in_str(s):
    for i in range(0,len(s)):
        for j in range(1,len(s)+1):
            if str_is_palindrome(s[i:j]) and len(s[i:j])>1 and len(s[i:j])<len(s) :
                return True
    return False

licznik=0
for i in range(0, len(x)):
    for j in range(1,len(x)+1):
        znak=x[i:j]
        #print(f"znak: {znak}")
        pos = x.find(znak)
        str = x[:pos] + x[pos+len(znak):] 
        print(f"str: {str}")
        #pos = x.find(znak, pos + 1)
        flaga=True
        ready=0
        if(str[::-1]!=str):
            flaga=palindrom_in_str(str)
            if(flaga):
                    break 
            else:       
                print(f"str_ready :{str}")  
                licznik+=1
                    #print(f"str_ready :{str}")   
                
print(licznik)               
         