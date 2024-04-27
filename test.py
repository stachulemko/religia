import pandas as pd
import tkinter as tk
from tkinter import filedialog
import pandas as pd
def wybiernaie_folderu():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path
data = {
    'imię nazwisko': [],
    'data urodzenia': [],
    'imię bierzmowania': [],
    'świadek bierzmowania': []
}


row_labels = []
tab=[]
df = pd.DataFrame(data=data, index=row_labels)
l=0
licznik=0
while(True):
    importowanie=input("importowanie (t/n):")
    if(importowanie=='t'):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        df = pd.read_excel(file_path)
    eksportowanie = (input("eksportowanie? (t/n(ręczne wpisywanie)):"))
    if(eksportowanie == "t"):
        dzielenie=input("dzielenie na plik? (t/n)")
        if dzielenie=='t':
            nazwa=input("podaj nazwe pliku: ")
            for i in range(licznik):
                df.loc[i].to_excel(f"{wybiernaie_folderu()}/{nazwa}{i}.xlsx")
            print("------------------------------------")
        else:
            print("kupa")
            nazwa_pliku = input("Podaj nazwę pliku: ")
            
            df.to_excel(f"{wybiernaie_folderu()}/{nazwa_pliku}.xlsx")
            licznik+=1
            print("Selected folder:", wybiernaie_folderu())
            
            
    else:
        imie_nazwisko = input("Podaj imię i nazwisko: ")
        data_urodzenia = input("Podaj datę urodzenia: ")
        imie_bierzmowania = input("Podaj imię bierzmowania: ")
        swiadectwo_bierzmowania = input("Podaj świadectwo bierzmowania: ")
        df = df._append({'imię nazwisko': imie_nazwisko, 'data urodzenia': data_urodzenia, 'imię bierzmowania': imie_bierzmowania, 'świadek bierzmowania': swiadectwo_bierzmowania}, ignore_index=True)
        
        print(df)
        l+=1
        


    
    