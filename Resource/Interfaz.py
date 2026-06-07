# Interfaz.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from Eventos import EventManager
from Recursos import ResourceManager
from Condiciones import ConditionsManager
class App:
    def __init__(self):
        self.event_manager = EventManager()
        self.resource_manager = ResourceManager()
        self.conditions_manager = ConditionsManager()

        self.window = tk.Tk()
        self.window.title("Gestor de Eventos")
    
       
        self.event_listbox = tk.Listbox(self.window)
        self.event_listbox.pack(fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(self.window, text="Agregar Evento", command=self.add_event)
        self.add_button.pack(side=tk.LEFT)

        self.remove_button = tk.Button(self.window, text="Eliminar Evento", command=self.remove_event)
        self.remove_button.pack(side=tk.LEFT)

        self.details_button = tk.Button(self.window, text="Ver Detalles", command=self.show_details)
        self.details_button.pack(side=tk.LEFT)
        
        self.place_button = tk.Button(self.window, text="Lugares", command=self.show_place)
        self.place_button.pack(side=tk.LEFT)
    
        self.staff_button = tk.Button(self.window, text="Personal", command=self.show_staff)
        self.staff_button.pack(side=tk.LEFT)
    
        self.resource_button = tk.Button(self.window, text="Recursos", command=self.show_resource)
        self.resource_button.pack(side=tk.LEFT)

        self.update_event_list()

    def run(self): # Ejecuta la Interfaz
        self.window.mainloop()

    def update_event_list(self): # Actualiza la lista
        self.event_listbox.delete(0, tk.END)
        for event in self.event_manager.get_events():
            self.event_listbox.insert(tk.END, event)

    def add_event(self): # Agrega un evento
        self.event_name = simpledialog.askstring("Agregar Evento", "Nombre del evento:")
        if self.event_name:
            self.date_selection()

    def remove_event(self): # Remueve un evento
        selected_event = self.event_listbox.curselection()
        if selected_event:
            event_name = self.event_listbox.get(selected_event)
            self.event_manager.remove_event(event_name)
            self.update_event_list()
        else:          
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")

    def show_details(self): # Muestra los detalles
        selected_event = self.event_listbox.curselection()
        selected_event_name = self.event_listbox.get(selected_event) 
        if selected_event:
            messagebox.showinfo("Detalles",self.event_manager.inf_event(selected_event_name))
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para ver detalles.")

    def show_place(self): # Muestra los Lugares
        show_place = self.resource_manager.show_place()
        messagebox.showinfo("Lugares",f"Lugares    CP/Mín  CP/Máx\n\n{show_place}")

    def show_staff(self): # Muestra el Personal
        show_staff = self.resource_manager.show_staff()
        messagebox.showinfo("Personal",f"Peronal    Horario    Disponibilidad\n\n{show_staff}")
    
    def show_resource(self): # Muestra los Recursos
        show_resource = self.resource_manager.show_resource()
        messagebox.showinfo("Recursos",f"Recursos    Disponibilidad\n\n{show_resource}")

    def personal_selection(self): #Selección de Personal
        self.event_personal = tk.Toplevel(self.window)
        self.event_personal.title("Seleccionar Personal")
        self.event_personal.geometry('200x420')
        self.elementos_personal = self.resource_manager.resource(4)
        self.listbox_personal = tk.Listbox(self.event_personal, selectmode=tk.MULTIPLE, height=23)
        for item in self.elementos_personal:
            self.listbox_personal.insert(tk.END, item)
        self.listbox_personal.pack()
        btn_save = tk.Button(self.event_personal, text="Aceptar", command=self.save_personal_selection)
        btn_save.pack()
    
    def save_personal_selection(self): #Guarda la selección de Personal
        self.personal_select = [self.listbox_personal.get(i) for i in self.listbox_personal.curselection()]
        self.personal_select_add = self.conditions_manager.conditions_personal_personal(self.personal_select)
        self.personal_select_place = self.conditions_manager.conditions_place(self.event_place_item, self.value)
        self.sub_personal_select_list = self.personal_select + self.personal_select_place
        self.personal_select_list =  self.personal_select_add + self.sub_personal_select_list
        self.personal_select_end = list(set(self.personal_select_list))
        #Verifica el Horario del personal
        if self.conditions_manager.control_personal_available(self.personal_select_end, self.value):
            self.event_personal_item = self.personal_select_end
            self.event_resource_item = self.conditions_manager.conditions_personal_resource(self.event_personal_item)
            self.available_personal = self.conditions_manager.available_personal(self.event_personal_item, self.event_guest_item)
            self.available_resource = self.conditions_manager.available_resource(self.event_resource_item, self.event_guest_item, self.available_personal)
            dictionary = self.event_manager.events
            self.event_personal.destroy()
            if self.conditions_manager.control_general(dictionary, self.event_date_item, self.available_personal, self.available_resource, self.event_place_item, self.event_guest_item) and self.conditions_manager.control_avilable_finite(dictionary, self.event_date_item, self.available_personal, self.available_resource):
                self.event_manager.add_event(self.event_name, self.event_date_item, self.event_place_item, self.event_guest_item, self.event_personal_item, self.event_resource_item, self.available_personal, self.available_resource)
                self.update_event_list()
                self.event_personal.mainloop()
            else:
                var = self.conditions_manager.inf
                if var == 0:
                    messagebox.showerror("Error","El espacio solicitado\nno se encuentra disponible en este momento")
                if var == 1:
                    messagebox.showerror("Error","El número de invitados solicitado\nexcede la capacidad disponible")
                if var == 2:
                    messagebox.showerror("Error","El número de personal solicitado\nexcede la capacidad disponible")
                if var == 3:
                    messagebox.showerror("Error","La cantidad de elementos solicitado\nexcede el stock disponible para la fecha actual")
                self.event_personal.mainloop()
        else:
            messagebox.showerror("Error", "Por favor, tenga en cuenta el horario del personal")


    def place_selection(self): #Selección de Lugar
        self.event_place = tk.Toplevel(self.window)
        self.event_place.title("Seleccionar Lugar")
        self.event_place.geometry('200x200')
        self.elementos_place = self.resource_manager.resource(1)
        self.copy_elementos_place = self.elementos_place
        if self.value < 8 or self.value >= 19 :
            del self.copy_elementos_place[3]
            del self.copy_elementos_place[7]
        else:
            self.copy_elementos_place = self.resource_manager.resource(1)
        self.listbox_place = tk.Listbox(self.event_place, selectmode=tk.SINGLE, height=10)
        for item in self.copy_elementos_place:
            self.listbox_place.insert(tk.END, item)
        self.listbox_place.pack()
        btn_save = tk.Button(self.event_place, text="Aceptar", command=self.save_place_selection)
        btn_save.pack()

    def save_place_selection(self): #Guarda la selección de Lugar
        self.place_select = self.listbox_place.get(self.listbox_place.curselection()) if self.listbox_place.curselection() else None
        if self.place_select is None:
            messagebox.showwarning("aviso", "Por favor, seleccione un solo elemento")
            return
        self.event_place_item = self.place_select
        self.event_place.destroy()
        self.guest_selection()
        self.event_place.mainloop()
        

    def guest_selection(self): #Seleccion de Invitados
        var = self.event_place_item
        list_index = self.resource_manager.resource(1)
        index = list_index.index(var)
        list_max = self.resource_manager.resource(2)[index]
        list_min = self.resource_manager.resource(3)[index]
        while True:
            self.guest = simpledialog.askstring("Invitados", "Cantidad")
            if self.guest is None:
                messagebox.showinfo("Info","Introduce un numero")
                return None
            if self.guest.isdigit() and int(self.guest) <= list_max and int(self.guest) >= list_min:
                self.event_guest_item = self.guest
                self.personal_selection()
                return self.guest   
            else:
                messagebox.showerror("Error", "Por favor, Introduce un numero de acuerdo a la capacidad del lugar seleccionado")


    def date_selection(self): #Seleccion de Fecha
        self.date = tk.Tk()
        self.date.geometry('280x230')
        self.date.title("Selector Fecha y Hora")

        #Descripcion
        ttk.Label(self.date, text="Fecha").grid(row=0, column=2)
        ttk.Label(self.date, text="Hora de Inicio").grid(row=3, column=2)
        ttk.Label(self.date, text="Hora de Final").grid(row=6, column=2)

        # Hora de Inicio
        ttk.Label(self.date, text="Hora").grid(row=4, column=1)
        self.combo_hour_beginning = ttk.Combobox(self.date, state="readonly", width=4,
                                      values=[f"{i:02d}" for i in range(0, 24)])
        self.combo_hour_beginning.current(1)
        self.combo_hour_beginning.grid(row=5, column=1)

        # Minutos de Inicio
        ttk.Label(self.date, text="Minutos").grid(row=4, column=3)
        self.combo_min_beginning = ttk.Combobox(self.date, state="readonly", width=4,
                                     values=[f"{i:02d}" for i in range(0, 60)])
        self.combo_min_beginning.current(0)
        self.combo_min_beginning.grid(row=5, column=3)

        # Hora de Final
        ttk.Label(self.date, text="Hora").grid(row=7, column=1)
        self.combo_hour_end = ttk.Combobox(self.date, state="readonly", width=4,
                                      values=[f"{i:02d}" for i in range(0, 24)])
        self.combo_hour_end.current(1)
        self.combo_hour_end.grid(row=8, column=1)

        # Minutos de Final
        ttk.Label(self.date, text="Minutos").grid(row=7, column=3)
        self.combo_min_end = ttk.Combobox(self.date, state="readonly", width=4,
                                     values=[f"{i:02d}" for i in range(0, 60)])
        self.combo_min_end.current(0)
        self.combo_min_end.grid(row=8, column=3)
        
        # Día
        ttk.Label(self.date, text="Día").grid(row=1, column=0)
        self.combo_day = ttk.Combobox(self.date, state="readonly", width=4)
        self.combo_day.grid(row=2, column=0)
        
        # Mes
        ttk.Label(self.date, text="Mes").grid(row=1, column=2)
        self.combo_month = ttk.Combobox(self.date, state="readonly", width=4,
                                     values=[f"{i:02d}" for i in range(1, 13)])
        self.combo_month.current(0)
        self.combo_month.grid(row=2, column=2)
        self.combo_month.bind("<<ComboboxSelected>>", self.update_date)

        # Año
        ttk.Label(self.date, text="Año").grid(row=1, column=4)
        self.combo_year = ttk.Combobox(self.date, state="readonly", width=6,
                                     values=[str(i) for i in range(2026, 2126)])
        self.combo_year.current(0)
        self.combo_year.grid(row=2, column=4)
        self.combo_year.bind("<<ComboboxSelected>>", self.update_date)

        # Actualiza los días
        self.update_date()

        #Boton
        btn = ttk.Button(self.date, text= "Aceptar", command=self.save_date_selection)
        btn.grid(row=9, column=0, columnspan=6, pady=10)

    def update_date(self, event = None):
        year = int(self.combo_year.get())
        month = int(self.combo_month.get())

        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = 31
        elif month in [4, 6, 9, 11]:
            day = 30
        else:  # febrero
            day = 29 if self.bisiesto(year) else 28

        values_day = [f"{i:02d}" for i in range(1, day + 1)]
        current_day_selection = self.combo_day.get()
        self.combo_day['values'] = values_day
        if current_day_selection and current_day_selection in values_day:
            self.combo_day.set(current_day_selection)
        else:
            self.combo_day.current(0)
        
    def bisiesto(self, year):
        year = int(year)
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
    def save_date_selection(self):
        if self.combo_hour_beginning.get() < self.combo_hour_end.get() and (int(self.combo_hour_end.get()) - int(self.combo_hour_beginning.get())) <= 3:
            self.event_date_item = [self.combo_year.get(), self.combo_month.get(), self.combo_day.get(), self.combo_hour_beginning.get(), self.combo_min_beginning.get(), self.combo_hour_end.get(), self.combo_min_end.get()]
            self.value = int(self.event_date_item[3])
            self.date.destroy()
            self.place_selection()
            self.date.mainloop()
        else:
            messagebox.showerror("Error", "Por favor, Introduce una fecha correcta\nInformación: Los eventos tienen que durar más de una hora y menos de tres horas")