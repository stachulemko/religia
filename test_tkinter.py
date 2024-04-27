import tkinter as tk

def add_row():
    row = tk.Frame(root)
    row.pack()

    labels = ['imię nazwisko', 'data urodzenia', 'imię bierzmowania', 'świadek bierzmowania']
    entries = []
    for label in labels:
        label_entry_frame = tk.Frame(row)
        label_entry_frame.pack(side=tk.LEFT)

        label_widget = tk.Label(label_entry_frame, text=label)
        label_widget.pack(side=tk.LEFT)

        entry = tk.Entry(label_entry_frame)
        entry.pack(side=tk.LEFT)

        entries.append(entry)

    root.entries = entries  # Store the entry widgets in the root window for later access
    print(entries)
root = tk.Tk()
root.geometry("400x200")  # Ustawienie początkowego rozmiaru okna

add_button = tk.Button(root, text="Add Row", command=add_row)
add_button.pack()
add_button = tk.Button(root, text="importuj", command=add_row)
add_button.pack(anchor=tk.NW)



root.mainloop()
