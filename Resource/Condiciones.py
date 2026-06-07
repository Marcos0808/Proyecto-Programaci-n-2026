# Condiciones.py
from Recursos import ResourceManager
from Eventos import EventManager

class ConditionsManager:
    def __init__(self):
        self.resource_manager = ResourceManager()
        self.event_manager = EventManager()

    def conditions_place(self, place, beginning):
        var = self.resource_manager.resource(1)
        personal = self.resource_manager.resource(4)
        result = list()
        #Salon G/P | Lobby | Sala de Reunion
        if place == var[0] or place == var[1] or place == var[6] or place == var[7]:
            result.append(personal[2])
        #Piscina G/P
        if place == var[4] or place == var[5]:
            result.append(personal[13])
        #Area de Excursion
        if place == var[8] and beginning >=8 and beginning < 19:
            result.append(personal[10])
            result.append(personal[11])
        #Area de Exhibicion
        if place == var[2] and beginning >=8 and beginning < 19:
            result.append(personal[20])
        #Zona Deportiva
        if place == var[3] and beginning >=8 and beginning < 19:
            result.append(personal[14])
        return result
       
    def conditions_personal_personal(self, staff):
        personal = self.resource_manager.resource(4)
        var = 0
        control = len(staff)
        result = list()
        while var < control:
            #Chef - Camarero 
            if staff[var] == personal[5]:
                result.append(personal[4]) 
            #Cantante - J.Seguridad/T.Sonido
            if staff[var] == personal[19]:
                result.append(personal[15]) 
                result.append(personal[8]) 
            #J.Seguridad - G.Seguridad
            if staff[var] == personal[15]:
                result.append(personal[16]) 
            #I.Especial - Gerente
            if staff[var] == personal[17]:
                result.append(personal[0]) 
            #I.VIP - Gerente/G.Seguridad
            if staff[var] == personal[18]:
                result.append(personal[0]) 
                result.append(personal[16]) 
            #Gerente - Asistente
            if staff[var] == personal[0]:
                result.append(personal[1]) 
            var = var + 1
        return result
            
    def conditions_personal_resource(self, staff):
        personal = self.resource_manager.resource(4)
        implements = self.resource_manager.resource(7)
        var = 0
        control = len(staff)
        result = list()
        while var < control:
            #Chofer - V.Transporte
            if staff[var] == personal[10]:
                result.append(implements[9]) 
            #Limpieza - I.Limpieza
            if staff[var] == personal[2]:
                result.append(implements[0]) 
            #Barman - Cocteleria
            if staff[var] == personal[6]:
                result.append(implements[7]) 
            #Chef - U.Cocina/Alimento
            if staff[var] == personal[5]:
                result.append(implements[5]) 
                result.append(implements[6]) 
            #Organizador - Mesa/Silla
            if staff[var] == personal[3]:
                result.append(implements[3]) 
                result.append(implements[4]) 
            #T.Sonido - E.Audio/Altavoz
            if staff[var] == personal[8]:
                result.append(implements[10]) 
                result.append(implements[11]) 
            #T.Iluminacion - Proyector
            if staff[var] == personal[9]:
                result.append(implements[13]) 
            #Mantenimiento - Pantalla
            if staff[var] == personal[7]:
                result.append(implements[14]) 
            #Cantante - Microfono
            if staff[var] == personal[19]:
                result.append(implements[12]) 
            #A.Deportivo - I.Deportivo
            if staff[var] == personal[14]:
                result.append(implements[1]) 
            #Salvavida - E.Prim.Aux
            if staff[var] == personal[13]:
                result.append(implements[2]) 
            #Artesano/Artista/D.Cultural - Puesto.V.F.A 
            if staff[var] == personal[20] or staff[var] == personal[21] or staff[var] == personal[22]:
                result.append(implements[8]) 
            var = var + 1
        return result
    
    def control_personal_available(self, staff, beginning):
        personal = self.resource_manager.resource(4)
        control_personal = self.resource_manager.resource(5)
        var = 0
        control = len(staff)
        #Comprobacion
        count = 0
        sub_count = control
        while var < control:
            value = staff[var]
            index = personal.index(value)
            verification = control_personal[index]
            var = var + 1
            if (verification == "Completo"):
                sub_count = sub_count - 1
            if (verification == "Diurno"):
                count = count + 1
            if (verification == "Nocturno") :
                count = count - 1
        if beginning >= 8 and beginning < 19:
            if count == sub_count:
                return True
            else:
                return False
        if beginning < 8 or beginning >= 19:
            count = count * (-1)
            if count == sub_count:
                return True
            else:
                return False
            
    def available_personal(self, elemt, guest):
        personal = self.resource_manager.resource(4)
        guest = int(guest)
        var = 0
        control = len(elemt)
        control_personal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while var < control:
            value = elemt[var]
            index = personal.index(value)
            if value == personal[4] or value == personal[16]:
                control_personal[index] = 1 if guest < 10 else guest / 10 
            elif value == personal[20]  or value == personal[21] or value == personal[22]:
                control_personal[index] = 1 if guest < 16 else guest / 16 
            else: 
                control_personal[index] = 1
            var = var + 1
        return control_personal

    def available_resource(self, elemt , guest, personal):
        resource = self.resource_manager.resource(7)
        guest = int(guest)
        var = 0
        control = len(elemt)
        control_resource = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while var < control:
            value = elemt[var]
            index = resource.index(value)
            if value == resource[1] or value == resource[4] or value == resource[6]:
                control_resource[index] = guest
            elif value == resource[3]:
                control_resource[index] = 1 if guest < 4  else guest / 4 
            elif value == resource[11] or value == resource[13]:
                control_resource[index] = 1 if guest < 20 else guest / 20 
            elif value == resource[8]:
                control_resource[index] = personal[20] + personal[21] + personal[22] 
            else:
                control_resource[index] = 1
            var = var + 1
        return control_resource
         
    def control_general(self, dictionary, date_2, personal_1, resource_1, place_1, guest_1):
        available_personal = self.resource_manager.resource(6)
        available_resource = self.resource_manager.resource(8)
        list_dictionary = list(dictionary)
        var = 0
        control = len(list_dictionary)
        result_personal = personal_1
        result_resource = resource_1
        result_guest = int(guest_1)
        if control == 0:
            return True
        while var < control:
            value = dictionary[list_dictionary[var]]
            date_1 = value.get('Date', 'N/A')
            personal_2 = value.get('Available_Personal', 'N/A')
            resource_2 = value.get('Available_Resource', 'N/A')
            place_2 = value.get('Place', 'N/A')
            guest_2 = value.get('Guests', 'N/A')
            if self.time(date_1, date_2):
                result_personal = [a + b for a,b in zip(result_personal, personal_2)]
                result_resource = [a + b for a,b in zip(result_resource, resource_2)]
                result_guest = int(guest_2) + result_guest
                if place_1 == place_2:
                    self.inf = 0
                    return False 
                var = var + 1
            else:
                var = var + 1
        checking_personal = [a - b for a,b in zip(available_personal, result_personal)]
        checking_resource = [a - b for a,b in zip(available_resource, result_resource)]
        if 80 - result_guest <= 0 :
            self.inf = 1
            return False
        if all(x >= 0 for x in checking_personal) and all(x >= 0 for x in checking_resource):
            return True
        self.inf = 2
        return False
    
    def control_avilable_finite(self, dictionary, date_2, personal_1, resource_1):
        available_personal = self.resource_manager.resource(6)
        available_resource = self.resource_manager.resource(8)
        control_personal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, personal_1[17], personal_1[18], personal_1[19], personal_1[20], personal_1[21], personal_1[22]]
        control_resource = [resource_1[0], 0, 0, 0, 0, resource_1[5], resource_1[6], resource_1[7], 0, 0, 0, 0, 0, 0, 0]
        list_dictionary = list(dictionary)
        var = 0
        control = len(list_dictionary)
        if control == 0:
            return True
        while var < control:
            value = dictionary[list_dictionary[var]]
            date_1 = value.get('Date', 'N/A')
            personal_2 = value.get('Available_Personal', 'N/A')
            resource_2 = value.get('Available_Resource', 'N/A')
            if date_1[0] == date_2[0] and date_1[1] == date_2[1] and date_1[2] == date_2[2]:
                control_personal[17] = personal_2[17] + control_personal[17]
                control_personal[18] = personal_2[18] + control_personal[18]
                control_personal[19] = personal_2[19] + control_personal[19]
                control_personal[20] = personal_2[20] + control_personal[20]
                control_personal[21] = personal_2[21] + control_personal[21]
                control_personal[22] = personal_2[22] + control_personal[22]

                control_resource[0] = resource_2[0] + control_resource[0]
                control_resource[5] = resource_2[5] + control_resource[5]
                control_resource[6] = resource_2[6] + control_resource[6]
                control_resource[7] = resource_2[7] + control_resource[7]

                var = var + 1 
            else: 
                var = var + 1 
        checking_personal = [a - b for a,b in zip(available_personal, control_personal)]
        checking_resource = [a - b for a,b in zip(available_resource, control_resource)]
        if all(x >= 0 for x in checking_personal) and all(x >= 0 for x in checking_resource):
            return True
        else:
            self.inf = 3
            return False       

    def time(self,date_1, date_2):
        str(date_1)
        str(date_2)
        hour_big = date_1[3] + "." + date_1[4]
        hour_end = date_1[5] + "." + date_1[6]
        sub_hour_big =  date_2[3] + "." + date_2[4]
        sub_hour_end =  date_2[5] + "." + date_2[6]
        year = int(date_1[0]) 
        month = int(date_1[1])
        day = int(date_1[2])
        sub_year = int(date_2[0])
        sub_month = int(date_2[1])
        sub_day = int(date_2[2])
        float(hour_big)
        float(hour_end)
        float(sub_hour_big)
        float(sub_hour_end)
        if ((sub_hour_big >= hour_big  and sub_hour_big < hour_end) or (sub_hour_end <= hour_end  and sub_hour_end > hour_big)) and (year == sub_year and month == sub_month and  day == sub_day):
            return True
        else:
            return False