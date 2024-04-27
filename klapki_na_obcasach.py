
                  
      

def kombinacje_klapek(tab):
    tab_komb_klapki=[]
    for i in range(1,len(tab)+1):
        tab_komb_klapki.append(tab[0:i])
    return tab_komb_klapki
        
          

    
tab_max=[]
tab_wartosci=[]
liczba_osob = 5
tab_wzrosty_dzieci = [5, 15, 10, 12, 1]
liczba_dostepnych_rozmiarow_klapek = 3
tab_rozmiary_klapek = [12, 2, 1]
min_wzrost = 14
tab_new=[]
print("-----------------")
print(kombinacje_klapek(tab_rozmiary_klapek))
print("-----------------")
for i in range(len(tab_wzrosty_dzieci)):
    if(tab_wzrosty_dzieci[i]<min_wzrost):
        tab_new.append(tab_wzrosty_dzieci[i])
print(tab_new)


for i in kombinacje_klapek(tab_rozmiary_klapek):
    tab_wzrosty_dziec2i = tab_new.copy()
    print(f"i: {i}")
    print(len(i))
    while(len(i)>0):
        stałą_dlugosc=len(tab_wzrosty_dziec2i)
        max_w=max(i)
        licznik=0
        min_ktory_daje=0
        for i in range(0,len(tab_wzrosty_dziec2i)):
            if(tab_wzrosty_dziec2i[i]+max_w>=min_wzrost):
                min_ktory_daje=tab_wzrosty_dziec2i[i]
                break
        for i in range(1,len(tab_wzrosty_dziec2i)):
            if(tab_wzrosty_dziec2i[i]+max_w>=min_wzrost and tab_wzrosty_dziec2i[i]<min_ktory_daje):
                min_ktory_daje=tab_wzrosty_dziec2i[i]
        
                
        if(max_w+min_ktory_daje>=min_wzrost):
            licznik+=1

        i.remove(max_w)
        tab_wzrosty_dziec2i.remove(min_ktory_daje)
    tab_max.append([licznik,i])
        
print(tab_max)
