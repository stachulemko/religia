import pandas as pd
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from openpyxl.workbook import Workbook
import tkinter as tk
entries = []
data = {
    'imię nazwisko': [],
    'data urodzenia': [],
    'imię bierzmowania': [],
    'świadek bierzmowania': []
}
licznik_glob=0

row_labels = []
df = pd.DataFrame(data=data, index=row_labels)
def importowanie():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    print(df)
    for i in range(len(df)):
        add_row()
    print(f"df:{df.iterrows()}")
    print(entries)
    for i, row in df.iterrows():
        print(f"i: {i}")
        print(0,row['imię nazwisko'])
        print(0,row['data urodzenia'])
        print(0,row['imię bierzmowania'])
        print(0,row['świadek bierzmowania'])
        # Adjust indexing here
        entries[i*4].insert(0,row['imię nazwisko'])
        entries[i*4+1].insert(0,row['data urodzenia'])
        entries[i*4+2].insert(0,row['imię bierzmowania'])
        entries[i*4+3].insert(0,row['świadek bierzmowania'])        
      
    
def data_to_exel():
    
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    nazwa="bierzmow"
    print(f"licznik_glob: {licznik_glob}")
    print(df)
    for i in range(licznik_glob-1):
        df.loc[i].to_excel(f"{folder_path}/{nazwa}{i}.xlsx")
def export ():
    licznik=0
    tab=[]
    print(f"entries: {entries}")
    for i in entries:
        print(i.get())
        tab.append(i.get())
        if(licznik==4):
            print(f"tab: {tab}")
            df._append({'imię nazwisko': tab[0], 'data urodzenia': tab[1], 'imię bierzmowania': tab[2], 'świadek bierzmowania': tab[3]}, ignore_index=True)
            tab.clear()
            licznik=0
            
        licznik+=1
    #print(len(df))
    data_to_exel()
        
        
def add_row():
    global licznik_glob
    row = tk.Frame(root)
    row.pack()

    labels = ['imię nazwisko', 'data urodzenia', 'imię bierzmowania', 'świadek bierzmowania']
    licznik_glob=licznik_glob+1
    for label in labels:
        label_entry_frame = tk.Frame(row)
        label_entry_frame.pack(side=tk.LEFT)

        label_widget = tk.Label(label_entry_frame, text=label)
        label_widget.pack(side=tk.LEFT)

        entry = tk.Entry(label_entry_frame)
        entry.pack(side=tk.LEFT)

        entries.append(entry)
    


root = tk.Tk()
root.geometry("400x200")  # Ustawienie początkowego rozmiaru okna

add_button = tk.Button(root, text="Add Row", command=add_row)
add_button.pack()
add_button = tk.Button(root, text="importuj", command=importowanie)
add_button.pack(anchor=tk.NW)
add_button = tk.Button(root, text="export", command=export)
add_button.pack(anchor=tk.NW)



root.mainloop()




    
    