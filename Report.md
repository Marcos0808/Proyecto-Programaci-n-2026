# Dominio del proyecto: Hotel:
El Programa es un Sistema de Gestión de Operaciones y Recursos que modela las independencias entre infraestructura, personal e inventario. Su función principal es garantizar la operatividad de las áreas mediante la validación de reglas de negocio, el control de capacidad y la gestión automatizada de ciclos de stock. Su dominio es un Hotel, el mismo cuenta con dos salones, uno grande y uno pequeño, dos Piscina, una grande y una pequeña, un Área de Exhibición, una Zona Deportiva, un Lobby, una Sala de Reuniones, un Áreas de Excursión y Otra Área. Ademas posee un total de 46 trabajadores interno, 20 trabajadores externos y un  total de 80 huéspedes. En el los recursos se dividen en: Áreas (que tienen atributos de capacidad), Personal (que tiene atributos de horario y rol) y Objetos (que tienen atributos de stock). 

# Horario: 
.Diurno ------ 08:00am - 19:00pm
.Nocturno ---- 19:01pm - 07:59am 
.Completo ---- una jornada (24h)

# Recursos:
## Áreas de eventos                 Capacidad
.Salón Grande                       (50 max, 31 min)
.Salón Pequeño                      (30 max, 10 min)
.Área de Exhibición                 (20 max, 8 min)
.Zona Deportiva                     (16 max, 4 min)
.Piscina Grande                     (40 max, 21 min)
.Piscina Pequeña                    (20 max, 6 min)
.Lobby                              (20 max, 10 min)
.Sala de Reuniones                  (15 max, 8 min)
.Área de Excursión                  (40 max, 20 min)
.Otra Área                          (80 max, 20 min)

**no limitado**
## Personal                 (46)    Horario 
.Gerente                    (1)     Completo 
.Asistente                  (1)     Completo 
.Limpieza                   (4)     Completo 
.Organizador                (2)     Completo 
.Camarero                   (8)     Completo
.Chef                       (2)     Completo 
.Barman                     (2)     Nocturno
.Mantenimiento              (2)     Completo 
.Técnico en Sonido          (2)     Completo 
.Técnico en Iluminación     (2)     Nocturno 
.Chofer                     (2)     Diurno
.Guía                       (2)     Diurno
.Animación                  (3)     Completo
.Salvavida                  (2)     Completo
.Asistente deportivo        (2)     Diurno
.Jefe de Seguridad          (1)     Nocturno
.Guardia de Seguridad       (8)     Nocturno
 
**limitado**
## Personal Externo         (20) 
.Invitado Especial          (2)     Nocturno
.Invitado VIP               (2)     Nocturno
.Cantante                   (1)     Nocturno
.Artesano                   (5)     Diurno
.Divulgador Cultural        (5)     Diurno
.Artista                    (5)     Completo

Nota: El personal limitado no se podrá reutilizar, además él mismo se actualiza al otro día

## Recursos                         (360)
.Implemento de Limpieza             (6)     [limitada]
.Implemento deportivo               (16)
.Equipo de Primeros Auxilios        (2)    
.Mesa                               (20)  
.Silla                              (80)
.Utensilio de Cocina                (2)     [limitada]
.Alimento                           (200)   [limitada]
.Coctelería                         (2)     [limitada]
.Puesto de Venta/Feria/Artesanal    (15)
.Vehículo de Transporte             (2) 
.Equipo de Audio                    (2)
.Altavoz                            (4)
.Micrófono                          (2)
.Proyector                          (4)
.Pantalla                           (3)

NOTA: Los recursos limitado no se podrán reutilizar, además los mismos se reponen al otro día 

# Reglas:
1. Dependencia de recursos
## Áreas de eventos - Personal                           
.Salón Pequeño/Grande ------------- Limpieza
.Lobby ---------------------------- Limpieza
.Sala de Reuniones ---------------- Limpieza 
.Piscina Pequeña/Grande------------ Salvavida
.Área de Excursión ---------------- Guia
.Área de Excursión ---------------- Chofer
.Área de Exhibición --------------- Artesano
.Zona Deportiva ------------------- Asistente Deportivo
## Personal - Personal
.Chef ----------------------------- Camarero = 1 por cada 10 invitados
.Cantante ------------------------- Jefe de Seguridad
.Cantante ------------------------- Técnico en Sonido
.Jefe Seguridad ------------------- Guardia de Seguridad = 1 por cada 10 invitados
.Invitado Especial ---------------- Gerente
.Invitado VIP --------------------- Gerente
.Invitado VIP --------------------- Guardia de Seguridad
.Gerente -------------------------- Asistente 
.Divulgador Cultural -------------- 1 por cada 16 invitados
.Artesano ------------------------- 1 por cada 16 invitados
.Artista -------------------------- 1 por cada 16 invitados
## Personal - Recurso
.Chofer --------------------------- Vehículo de Transporte
.Limpieza ------------------------- Implemento de Limpieza
.Barman --------------------------- Cocteleria
.Chef ----------------------------- Utensilio de Cocina
.Chef ----------------------------- Alimento = Cantidad de invitados
.Organizador ---------------------- Silla = Cantidad de invitados
.Organizador ---------------------- Mesa = 1 por cada 4 Sillas
.Técnico en Sonido ---------------- Equipo de Audio
.Técnico en Sonido ---------------- Altavoz = 1 por cada 20 invitados
.Técnico en Iluminación ----------- Proyector = 1 por cada 20 invitados
.Mantenimiento -------------------- Pantalla
.Cantante ------------------------- Micrófono
.Asistente Deportivo -------------- Implementos deportivos = cantidad de invitados
.Salvavida ------------------------ Equipo de Primeros Auxilios
.Divulgador Cultural -------------- Puesto de Venta/Feria/Artesanal = 1 por cada 1 invitado
.Artesano ------------------------- Puesto de Venta/Feria/Artesanal = 1 por cada 1 invitado
.Artista -------------------------- Puesto de Venta/Feria/Artesanal = 1 por cada 1 invitado

2. Capacidad: 
En lugar de usar un solo número para la capacidad, usamos un rango. Esto permite implementar validaciones de seguridad: el sistema no solo debe impedir que entren x cantidad de personas a un área asignada, sino que debe alertar si el grupo es menor al mínimo y mayor al maximo requerido para que el área sea operativa. Tambien se ha de tener en cuenta la duración de los eventos que deben durar más de 1 hora y menos de 3 horas. 

3. Tiempo
Al definir turnos (Diurno/Nocturno/Completo) y tipos de jornada (no Limitado/Limitado),se permite programar la disponibilidad dinámica. Por ejemplo: el sistema no permitirá agendar un evento de "Coctelería" si el horario solicitado no coincide con la disponibilidad del personal de "Barman".

# Extra 
Gracias a que el personal está categorizado por roles y no por nombres fijos, si el hotel decide contratar 10 técnicos de sonido adicionales, el sistema solo requiere actualizar un valor entero en la base de datos, no cambiar la lógica del código, por lo que el modelo actual permite, en fases futuras implementar nuevas funciones 

Nota: Para la ejecución del programa debes tener instalada la última versión de python, y mediante la terminal ejecutar el archivo Main.py que se encuentra dentro de la carpeta Planificador Inteligente de Eventos\Resource.