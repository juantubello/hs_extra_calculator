#coding:utf8

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import numpy as np

HR_LABORALES = 8

def calculate_money(hs, tarif):
    cash = hs * tarif
    cash = f"{cash:,}"
    return cash

def clear_data():
    tv1.delete(*tv1.get_children())
    return None

def update_tarifa():
    try:
        entryString = int(entry_tarifa.get())
    except ValueError:
        tk.messagebox.showerror("Information", "Tarifa tiene que ser un numero")
        return None
    label_tarifa["text"] = "Tarifa: "+ str(entryString) + " $"

def file_dialog():
    filename = filedialog.askopenfilename(initialdir="C:/", title="Seleccione archivo")
    label_file["text"] = filename
    return None

def calulate_hs_extra(horas_extras_list):
    hrs_extra = 0

    for index in range(len(horas_extras_list)):
        if horas_extras_list[index] < HR_LABORALES and horas_extras_list[index] != 0:
            print("feriado")
        elif horas_extras_list[index] != 0:
           horas_extras_list[index] = horas_extras_list[index] - HR_LABORALES

    for hora in horas_extras_list:
        hrs_extra += int(hora)

    return hrs_extra
    
def load_excel_data():
    horas_extras_list = []

    try:
        tarifa = int(entry_tarifa.get())
    except ValueError:
        tk.messagebox.showerror("Information", "Verifique campo tarifa")
        return None

    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)      
        else:
            df = pd.read_excel(excel_filename)
            # inplace
            df.replace(np.nan, 0, inplace=True)
            print(df)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"{file_path}")
        return None
    
    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # Se convierte a lista de listas

    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview.

        if df_rows[0][0] == row[0]:
            first_row = True
        else:
            first_row = False

        if first_row:   
            for index in range(len(row) - 2):
              horas_extras_list.append(row[index + 1])
        else:
            for index in range(len(row) - 2):
              horas_extras_list[index] = horas_extras_list[index] + row[index + 1]

    horas_extra = calulate_hs_extra(horas_extras_list)
    label_hs["text"] = horas_extra

    money = calculate_money(horas_extra, tarifa)
    label_money["text"] = money + " $"

    return None

# Inicializacion
root = tk.Tk()

root.title( "Calculador de horas extra" )
root.geometry("600x600")   # Dimension de la app
root.pack_propagate(False) # No permite que los widgets redmiensionen la app.
root.resizable(0, 0)       # App en tamaño fijo.

# Frame de excel
excel_frame = tk.LabelFrame(root, text="Excel de horas")
excel_frame.place(height=250, width=600)

# Frame de tarifa
tarifa_frame = tk.LabelFrame(root, text="Ingrese tarifa")
tarifa_frame.place(height=50, width=500, rely=0.50, relx=0.08)

# Frame de horas extra
hs_frame = tk.LabelFrame(root, text="Horas Extra")
hs_frame.place(height=50, width=500, rely=0.60, relx=0.08)

# Frame de plata a cobrar
money_frame = tk.LabelFrame(root, text="A cobrar")
money_frame.place(height=50, width=500, rely=0.70, relx=0.08)

# Frame de abrir archivo
file_frame = tk.LabelFrame(root, text="Ruta del archivo")
file_frame.place(height=100, width=500, rely=0.80, relx=0.08)

# Botones de archivo
btn_abrir_archivo = tk.Button(file_frame, text="Abrir Archivo", command=lambda: file_dialog())
btn_abrir_archivo.place(rely=0.60, relx=0.50)

btn_calcular_horas = tk.Button(file_frame, text="Calcular Horas Extra", command=lambda: load_excel_data())
btn_calcular_horas.place(rely=0.60, relx=0.20)

# Texto de inicializacion archivo
label_file = ttk.Label(file_frame, text="Sin archivo")
label_file.place(rely=0, relx=0)

# Texto de inicializacion horas extra
label_hs = ttk.Label(hs_frame, text="Sin datos de horas extra")
label_hs.place(rely=0, relx=0)

# Texto de inicializacion plata a cobrar
label_money = ttk.Label(money_frame, text="Sin plata :( ")
label_money.place(rely=0, relx=0)

# Celda de input tarifa
entry_tarifa = ttk.Entry(tarifa_frame, text="Sin tarifa")
entry_tarifa.place(rely=0, relx=0)

# Boton tarifa
btn_tarifa = tk.Button(tarifa_frame, text="Cargar Tarifa", command=lambda: update_tarifa())
btn_tarifa.place(rely=-0.3, relx=0.35)

# Texto de inicializacion tarifa
label_tarifa = ttk.Label(tarifa_frame, text="Sin tarifa")
label_tarifa.place(rely=0, relx=0.60)

## Treeview Widget
tv1 = ttk.Treeview(excel_frame)
tv1.place(relheight=1, relwidth=1) 

treescrolly = tk.Scrollbar(excel_frame, orient="vertical", command=tv1.yview) 
treescrollx = tk.Scrollbar(excel_frame, orient="horizontal", command=tv1.xview) 
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
treescrollx.pack(side="bottom", fill="x") 
treescrolly.pack(side="right", fill="y") 

root.mainloop()