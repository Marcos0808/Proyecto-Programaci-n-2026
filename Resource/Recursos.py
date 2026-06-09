class ResourceManager:

    def resource(self, num : int):

        resource_place = ["Salón Grande","Salón Pequeño","Area de Exhibición","Zona Deportiva","Piscina Grande",
                         "Piscina Pequeña","Lobby","Sala de Reuniones","Área de Excursión","Otra Área"]

        resource_place_guest_max = [50 ,30 ,20 ,16 ,40 ,20 ,20 ,15 ,40 ,80]

        resource_place_guest_min = [31 ,10 ,8 ,4 ,21 ,6 ,10 ,8 ,20 ,20]

        resource_staff = ["Gerente","Asistente","Limpieza","Organizador","Camarero","Chef","Barman","Mantenimiento","Técnico en Sonido",
                      "Técnico en Iluminación","Chofer","Guía","Animación","Salvavidas","Asistente Deportivo","Jefe de Seguridad",
                      "Guardia de Seguridad","Invitado Especiale","Invitado VIP","Cantante","Artesano","Divulgador Cultural","Artista"]
    
        resource_staff_hour = ["Completo","Completo","Completo","Completo","Completo","Completo","Nocturno","Completo","Completo","Nocturno","Diurno",
                     "Diurno","Completo","Completo","Diurno","Nocturno","Nocturno","Nocturno","Completo","Nocturno","Diurno","Diurno","Completo"]
    
        resource_staff_available = [1, 1, 4, 2, 8, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 8, 2, 2, 1, 5, 5, 5]

        resource = ["Implementos de Limpieza","Implementos Deportivos","Equipo de Primeros Auxilios","Mesa","Silla","Utensilios de Cocina","Alimento",
                    "Cocteleria","Puesto de Venta/Feria/Artesanal","Vehículo de Transporte","Equipo de Audio","Altavoz","Micrófono","Proyector","Pantalla"]

        resource_available = [6, 16, 2, 20, 80, 2, 200, 2, 15, 2, 2, 4, 2, 4, 3]

        if num == 1 :
            return resource_place
        if num == 2 :
            return resource_place_guest_max
        if num == 3 :
            return resource_place_guest_min
        if num == 4 :
            return resource_staff
        if num == 5 :
            return resource_staff_hour
        if num == 6 :
            return resource_staff_available
        if num == 7 :
            return resource
        if num == 8 :
            return resource_available


    def show_place(self):
        
        resource_place = self.resource(1)
        resource_place_guest_max = self.resource(2)
        resource_place_guest_min = self.resource(3)
        inf = list()
        var = 0
        control = len(resource_place)
       
        while var < control:

            place = resource_place[var]
            max = resource_place_guest_max[var]
            min = resource_place_guest_min[var]
            inf.append(f"{place}   {min} - {max}")
            var = var + 1

        message = "\n".join(inf)
        return message


    def show_staff(self):
        
        resource_staff = self.resource(4)
        resource_staff_hour = self.resource(5)
        resource_staff_available = self.resource(6)
        inf = list()
        var = 0
        control = len(resource_staff)
       
        while var < control:
            staff = resource_staff[var]
            hour = resource_staff_hour[var]
            available = resource_staff_available[var]
            inf.append(f"{staff}   {hour}   {available}")
            var = var + 1

        message = "\n".join(inf)
        return message

    def show_resource(self):

        resource_use = self.resource(7)
        resource_use_available = self.resource(8)
        inf = list()
        var = 0
        control = len(resource_use)
       
        while var < control:
            use = resource_use[var]
            available = resource_use_available[var]
            inf.append(f"{use}   {available}")
            var = var + 1

        message = "\n".join(inf)
        return message