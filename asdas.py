import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def add_data():
    global l
    imie_nazwisko = imie_nazwisko_entry.get()
    data_urodzenia = data_urodzenia_entry.get()
    imie_bierzmowania = imie_bierzmowania_entry.get()
    swiadectwo_bierzmowania = swiadectwo_bierzmowania_entry.get()
    df.loc[l] = [imie_nazwisko, data_urodzenia, imie_bierzmowania, swiadectwo_bierzmowania]
    l += 1
    tree.insert("", "end", text=l, values=[imie_nazwisko, data_urodzenia, imie_bierzmowania, swiadectwo_bierzmowania])

def export_data():
    dzielenie = dzielenie_entry.get()
    if dzielenie == 't':
        nazwa = nazwa_entry.get()
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        for i in range(licznik):
            df.loc[i].to_excel(f"{folder_path}/{nazwa}{i}.xlsx")
    else:
        nazwa_pliku = nazwa_pliku_entry.get()
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        df.to_excel(f"{folder_path}/{nazwa_pliku}.xlsx")
        licznik += 1
        print("Selected folder:", folder_path)

data = {
    'imię nazwisko': [],
    'data urodzenia': [],
    'imię bierzmowania': [],
    'świadek bierzmowania': []
}

row_labels = []
tab = []
df = pd.DataFrame(data=data, index=row_labels)
l = 0
licznik = 0

root = tk.Tk()

# Create a Treeview widget
tree = ttk.Treeview(root)
tree["columns"] = ("imię nazwisko", "data urodzenia", "imię bierzmowania", "świadek bierzmowania")

# Define column headings
tree.heading("#0", text="Index")
tree.heading("imię nazwisko", text="Imię Nazwisko")
tree.heading("data urodzenia", text="Data Urodzenia")
tree.heading("imię bierzmowania", text="Imię Bierzmowania")
tree.heading("świadek bierzmowania", text="Świadek Bierzmowania")

# Add data to the Treeview
for index, row in df.iterrows():
    tree.insert("", "end", text=index, values=row.tolist())

# Add the Treeview to the root window
tree.grid(row=0, column=0, columnspan=4)

# Add input fields for data entry
imie_nazwisko_label = tk.Label(root, text="Imię i Nazwisko:")
imie_nazwisko_label.grid(row=1, column=0)
imie_nazwisko_entry = tk.Entry(root)
imie_nazwisko_entry.grid(row=1, column=1)

data_urodzenia_label = tk.Label(root, text="Data Urodzenia:")
data_urodzenia_label.grid(row=2, column=0)
data_urodzenia_entry = tk.Entry(root)
data_urodzenia_entry.grid(row=2, column=1)

imie_bierzmowania_label = tk.Label(root, text="Imię Bierzmowania:")
imie_bierzmowania_label.grid(row=3, column=0)
imie_bierzmowania_entry = tk.Entry(root)
imie_bierzmowania_entry.grid(row=3, column=1)

swiadectwo_bierzmowania_label = tk.Label(root, text="Świadectwo Bierzmowania:")
swiadectwo_bierzmowania_label.grid(row=4, column=0)
swiadectwo_bierzmowania_entry = tk.Entry(root)
swiadectwo_bierzmowania_entry.grid(row=4, column=1)

# Add a button to add data
add_button = tk.Button(root, text="Add Data", command=add_data)
add_button.grid(row=5, column=0, columnspan=2)

# Add input fields for export options
dzielenie_label = tk.Label(root, text="Dzielenie na plik? (t/n):")
dzielenie_label.grid(row=6, column=0)
dzielenie_entry = tk.Entry(root)
dzielenie_entry.grid(row=6, column=1)

nazwa_label = tk.Label(root, text="Podaj nazwę pliku:")
nazwa_label.grid(row=7, column=0)
nazwa_entry = tk.Entry(root)
nazwa_entry.grid(row=7, column=1)

nazwa_pliku_label = tk.Label(root, text="Podaj nazwę pliku:")
nazwa_pliku_label.grid(row=8, column=0)
nazwa_pliku_entry = tk.Entry(root)
nazwa_pliku_entry.grid(row=8, column=1)

# Add a button to export data
export_button = tk.Button(root, text="Export Data", command=export_data)
export_button.grid(row=9, column=0, columnspan=2)

root.mainloop()
