from tkinter import *
from tkinter import ttk 

raiz=Tk()
raiz.title("Ejercicio 2")
raiz.geometry("770x680")

# definir estilo para el Frame 1
estilo = ttk.Style()
estilo.configure('gris.TFrame', background='gray40')
estilo = ttk.Style()
estilo.configure('negro.TFrame', background='black')
estilo = ttk.Style()
estilo.configure('cafe.TFrame', background='#482525')
estiloEntry = ttk.Style()
estiloEntry.configure('cafe.TEntry', background='#482525')

#------------------------------------------------ FRAME 1 ----------------------------------------------------------------------------
Frame1 = ttk.Frame(raiz, padding="10 5 188 5", style='gris.TFrame')
Frame1.grid(column=0, row=0, padx=0, pady=0)

imagenCarrito = PhotoImage(file="carrito.png")
etqImagen = ttk.Label(Frame1)
etqImagen.grid(sticky=(W), column=0, row=0, padx=0, pady=0)
etqImagen.config(background='gray40')
etqImagen['image'] = imagenCarrito
ttk.Label(Frame1, text="Product managament", font=("arial", 36, 'bold'), background="gray40",
           foreground='white').grid(column=1, row=0, padx=0, pady=0)

#------------------------------------------------ FRAME 2 ----------------------------------------------------------------------------
Frame2 = ttk.Frame(raiz, padding="30 10 30 20", style='negro.TFrame')
Frame2.grid(column=0, row=1, padx=0, pady=0)

#------------------------------------------------ FRAME 3 ----------------------------------------------------------------------------
Frame3 = ttk.Frame(Frame2, padding="10 10 10 10", style='cafe.TFrame')
Frame3.grid(column=0, row=0, padx=0, pady=0)

#Frame mitad superior*************************************************************
Frame31 = ttk.Frame(Frame3, padding="10 10 63 10", style='cafe.TFrame')
Frame31.grid(column=0, row=0, padx=0, pady=0)

#Frame tabla*************************************************************
Frame32 = ttk.Frame(Frame3, padding="10 10 10 10", style='cafe.TFrame')
Frame32.grid(column=0, row=1, padx=0, pady=0)

tv = ttk.Treeview(Frame32, columns=("col1","col2", "col3", "col4"))
tv.grid(column=0, row=0, padx=0, pady=0)
tv.column("#0",width=130)
tv.column("col1",width=130, anchor=CENTER)
tv.column("col2",width=130, anchor=CENTER)
tv.column("col3",width=130, anchor=CENTER)
tv.column("col4",width=130, anchor=CENTER)

tv.heading("#0", text="IdProduct", anchor=CENTER)
tv.heading("col1", text="NameP", anchor=CENTER)
tv.heading("col2", text="Description", anchor=CENTER)
tv.heading("col3", text="Quantity", anchor=CENTER)
tv.heading("col4", text="UnitePrice", anchor=CENTER)





#Frame productos mitad superior*************************************************************
Frame311 = ttk.Frame(Frame31, padding="10 10 10 10", style='cafe.TFrame')
Frame311.grid(column=0, row=0, padx=0, pady=0)

ttk.Label(Frame311, text="Id product: ", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=0, row=0, padx=30, pady=10, sticky=(W))
ttk.Label(Frame311, text="Name: ", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=0, row=1, padx=30, pady=10, sticky=(W))
ttk.Label(Frame311, text="Description: ", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=0, row=2, padx=30, pady=10, sticky=(W))
ttk.Label(Frame311, text="Quantity: ", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=0, row=3, padx=30, pady=10, sticky=(W))
ttk.Label(Frame311, text="Price: ", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=0, row=4, padx=30, pady=10, sticky=(W))

ttk.Label(Frame311, text="_____________________", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=1, row=0, padx=15, pady=10, sticky=(S))
ttk.Label(Frame311, text="_____________________", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=1, row=1, padx=15, pady=10, sticky=(S))
ttk.Label(Frame311, text="_____________________", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=1, row=2, padx=15, pady=10, sticky=(S))
ttk.Label(Frame311, text="_____________________", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=1, row=3, padx=15, pady=10, sticky=(S))
ttk.Label(Frame311, text="_____________________", font=("arial", 14, 'bold'), background="#482525", 
          foreground='white').grid(column=1, row=4, padx=15, pady=10, sticky=(S))

idEntry = Entry(Frame311, width=20, justify = CENTER, font=("arial", 14), background='#482525', borderwidth=0, foreground='white')
idEntry.grid(column=1, row=0, padx=0, pady=0, sticky=(N))
nameEntry = Entry(Frame311, width=20, justify = CENTER, font=("arial", 14), background='#482525', borderwidth=0, foreground='white')
nameEntry.grid(column=1, row=1, padx=0, pady=0, sticky=(N))
descripcionEntry = Entry(Frame311, width=20, justify = CENTER, font=("arial", 14), background='#482525', borderwidth=0, foreground='white')
descripcionEntry.grid(column=1, row=2, padx=0, pady=0, sticky=(N))
quantityEntry = Entry(Frame311, width=20, justify = CENTER, font=("arial", 14), background='#482525', borderwidth=0, foreground='white')
quantityEntry.grid(column=1, row=3, padx=0, pady=0, sticky=(N))
priceEntry = Entry(Frame311, width=20, justify = CENTER, font=("arial", 14), background='#482525', borderwidth=0, foreground='white')
priceEntry.grid(column=1, row=4, padx=0, pady=0, sticky=(N))

#Frame botones mitad superior*************************************************************
Frame312 = ttk.Frame(Frame31, padding="10 10 10 10", style='cafe.TFrame')
Frame312.grid(column=1, row=0, padx=0, pady=0)

botonSave = Button(Frame312, text="Save", width=10, background='green', font=("arial", 14), foreground='white').grid(column=0, row=1, padx=0, pady=0, columnspan=3)
botonDelete = Button(Frame312, text="Delete", width=10, background='red', font=("arial", 14), foreground='white').grid(column=0, row=2, padx=0, pady=10, columnspan=3)
botonUpdate = Button(Frame312, text="Update", width=10, background='orange', font=("arial", 14), foreground='white').grid(column=0, row=3, padx=0, pady=10, columnspan=3)

imagenbuscar = PhotoImage(file="bucar.png")
etqImagenbuscar = Button(Frame312)
etqImagenbuscar.grid(sticky=(W), column=0, row=0, padx=0, pady=10)
etqImagenbuscar.config(background='#482525', borderwidth=0)
etqImagenbuscar['image'] = imagenbuscar

imagenlimpiar = PhotoImage(file="limpiar.png")
etqImagenlimpiar = Button(Frame312)
etqImagenlimpiar.grid(sticky=(W), column=1, row=0, padx=0, pady=10)
etqImagenlimpiar.config(background='#482525', borderwidth=0)
etqImagenlimpiar['image'] = imagenlimpiar

botonSave = Button(Frame312, text="Back", background='#482525', font=("arial", 14), foreground='blue', borderwidth=0).grid(column=2, row=0, padx=0, pady=10, columnspan=2)

raiz.mainloop()