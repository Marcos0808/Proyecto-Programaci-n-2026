# Eventos.py
import json
import os

class EventManager:
    def __init__(self, filename='eventos.json'):
        self.events = {}
        self.filename = filename
        self.load_events()

    def add_event(self, name, date, place, guests, personal, resource, available_personal, available_resource):
        
        self.events[name] = {
            "Name" : name,
            "Date" : date,
            "Place" : place,
            "Guests" : guests,
            "Personal" : personal,
            "Resource" : resource,
            "Available_Personal" : available_personal,
            "Available_Resource" : available_resource
        }
        self.order_event()
        print(f"Evento; {name}, Fecha: {date}, Lugar: {place}, Invitados: {guests}, Personal: {personal}, Recursos: {resource}")
        self.save_events()
    
    def inf_event(self, event_name):
        if event_name in self.events:
            details = self.events[event_name]
            name = details.get('Name', 'N/A')
            date = details.get('Date', 'N/A' )
            place = details.get('Place', 'N/A')
            guests = details.get('Guests', 'N/A')
            personal = details.get('Personal', 'N/A')
            resource = details.get('Resource', 'N/A')
            return f"Nombre: {name}\nInicio: {date[3]}:{date[4]} Fin: {date[5]}:{date[6]} Fecha: {date[2]}/{date[1]}/{date[0]}\nLugar: {place}\nInvitados: {guests}\nPersonal: {personal}\nRecurso: {resource}"
        else:
            print(f"El evento {event_name}, no se encuentra en el registro")

    def remove_event(self, name):
        if name in self.events:
            del self.events[name]
            print(f"Evento '{name}' eliminado.")
            self.save_events()
        else:
            print(f"Evento '{name}' no encontrado.")

    def get_events(self):
        return self.events
    
    def order_event(self):
        sorted_event = sorted(self. events.items(), key = lambda x: x[1].get('Date',''))
        self.events = dict(sorted_event)
    
    def save_events(self):
        with open(self.filename, 'w') as f:
            json.dump(self.events, f)
        print("Eventos guardados en el archivo.")
        
    def load_events(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.events = json.load(f)
            print("Eventos cargados desde el archivo.")
        else:
            print("No se encontró archivo de eventos. Se creará uno nuevo.")