wejsce=input()
#lista_wsyzstkich=()
def czy_na_liscie_palindrom(lp,range):
    for i in lp:
        if(range[0]<=i[0] and range[1]>=i[1]):
            return True
    return False     
def str_is_palindrome(s):
    return s == s[::-1]
    
def palindrom_in_str(s):
    for i in range(0,len(s)):
        for j in range(1,len(s)+1):
            if str_is_palindrome(s[i:j]) and len(s[i:j])>1  :
                return True
    return False

def genrate_every_sybstring_from_string(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            yield (s[i:j],(i,j))
licznik=0
lista_zakresow_palindromow=[]
for t in genrate_every_sybstring_from_string(wejsce):
    s=t[0]
    print(t)
    #lista_wsyzstkich.append([s.find(s),len(s)])
    if len(s)==1:
            licznik+=1
    else:
        #print(t[1])
        if(not czy_na_liscie_palindrom(lista_zakresow_palindromow,t[1])):
            if(palindrom_in_str(s)):
                lista_zakresow_palindromow.append(t[1])
            else:
                licznik+=1
                #print(f"t: {t}")
        
        #if()
            #print(s)
    #elif(len(s)>1 and not palindrom_in_str(s)):
        
        #abacbbdfdgbgabcfff
        #sprawdz czy ktorys z zakresow znalezinych juz palindrowow miesci sie wewnatrz tego stringa 
        #jesli prawda to przeskakujemy do nastepnego
        #jesli nie to psrawdzamy czy ten string jest palindromem
        #jesli jest palindrome to dodajemy do listy zakresow palidromow
        #jesli nie to dodajemy do licznika
    
   
print(licznik)