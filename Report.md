## Índice

1. [Descripción del dominio](#descripción-del-dominio)
2. [Recursos](#recursos)
3. [Reglas](#reglas)
4. [Estructura del proyecto](#estructura-del-proyecto)
5. [Cómo ejecutar el proyecto](#cómo-ejecutar-el-proyecto)
6. [Funcionalidades](#funcionalidades)
7. [Extra](#extra)
8. [Agradecimiento](#Agradecimiento)

---

## Descripción del Dominio
El Programa es un Sistema de Gestión de Operaciones y Recursos que modela las independencias entre infraestructura, personal e inventario. Su función principal es garantizar la operatividad de las áreas mediante la validación de reglas de negocio, el control de capacidad y la gestión automatizada de ciclos de stock. Su dominio es un Hotel, el mismo cuenta con dos salones, uno grande y uno pequeño, dos Piscina, una grande y una pequeña, un Área de Exhibición, una Zona Deportiva, un Lobby, una Sala de Reuniones, un Áreas de Excursión y Otra Área. Ademas posee un total de 46 trabajadores interno, 20 trabajadores externos y un  total de 80 huéspedes. En el los recursos se dividen en: Áreas (que tienen atributos de capacidad), Personal (que tiene atributos de horario y rol) y Objetos (que tienen atributos de stock). 

---

## Recursos:

### Horario: 

| Descripción | Horario |
|---|---|
| Diurno | 08:00 - 19:00 |
| Nocturno | 19:01 - 07:59 |
| Completo | 24 horas |

### Áreas de eventos                    

| Áreas | Capacidad.Máx | Capacidad.Mín |
|---|---|---|
| Salón Grande | 50 | 31 |
| Área de Exhibición | 30 | 10 |
| Salón Grande | 20 | 8 |
| Zona Deportiva | 16 | 4 |
| Piscina Grande | 40 | 21 |
| Piscina Pequeña | 20 | 6 |
| Lobby | 20 | 10 |
| Sala de Reuniones | 15 | 8 |
| Área de Excursión | 40 | 20 |
| Otra Área | 80 | 20 |

### Personal (no limitado)                 

| Personal | Cantidad | Horario|
|---|---|---|
| Gerente | 1 | Completo |
| Asistente | 1 | Completo |
| Limpieza | 4 | Completo |
| Organizador | 2 | Completo |
| Camarero | 8 | Completo |
| Chef | 2 | Completo |
| Barman | 2 | Completo |
| Mantenimiento | 2 | Completo |
| Técnico en Sonido | 2 | Completo |
| Técnico en Iluminación | 2 | Nocturno |
| Chofer | 2 | Diurno |
| Guía | 2 | Diurno |
| Animación | 3 | Completo |
| Salvavida | 2 | Completo |
| Asistente deportivo | 2 | Diurno |
| Jefe de Seguridad | 1 | Nocturno |
| Guardia de Seguridad | 8 | Nocturno |
 
### Personal Externo (limitado)
         
| Personal | Cantidad | Horario|
|---|---|---|
| Invitado Especial | 2 | Nocturno |
| Invitado VIP | 2 | Nocturno |
| Cantante | 1 | Nocturno |
| Artesano | 5 | Diurno |
| Divulgador Cultural | 5 | Diurno |
| Artista | 5 | Completo |

- Nota: El personal limitado no se podrá reutilizar, además él mismo se actualiza al otro día

## Recursos                         

| Resursos | Cantidad | limitado |
|---|---|---| 
| Implemento de Limpieza | 6 | Sí |
| Implemento deportivo | 16 | No |
| Equipo de Primeros Auxilios | 2 | No |
| Mesa | 29 | No |
| Silla | 80 | No |
| Utensilio de Cocina | 2 | Sí |
| Alimento | 200 | Sí |
| Coctelería | 2 | Sí |
| Puesto de Venta/Feria/Artesanal | 15 | No |
| Vehículo de Transporte | 2 | No |
| Equipo de Audio | 2 | No |
| Altavoz | 4 | No |
| Micrófono | 2 | No |
| Proyector | 4 | No |
| Pantalla | 3 | No |

- NOTA: Los recursos limitado no se podrán reutilizar, además los mismos se reponen al otro día 

---

## Reglas:
1. Dependencia de recursos
- Nota: Al solicitar los recursos de la parte izquierda el programa mediante un  método llama a los recursos de la parte derecha
### Áreas de eventos - Personal                           

| Áreas de eventos | Personal | Cantidad |
|---|---|---|
| Salón Pequeño/Grande | Limpieza | 1 |
| Lobby | Limpieza |1 |
| Sala de Reuniones | Limpieza | 1 |
| Piscina Pequeña/Grande | Salvavida | 1 |
| Área de Excursión | Guia | 1 |
| Área de Excursión | Chofer | 1 |
| Área de Exhibición | Artesano | 1 |
| Zona Deportiva | Asistente Deportivo | 1 |

### Personal - Personal

| Personal | Personal | Cantidad |
|---|---|---|
| Chef | Camarero | 1 por cada 10 invitados |
| Cantante | Jefe de Seguridad | 1 |
| Cantante | Técnico en Sonido | 1 |
| Jefe Seguridad  | Guardia de Seguridad | 1 por cada 10 invitados |
| Invitado Especial | Gerente | 1 |
| Invitado VIP | Gerente | 1 |
| Invitado VIP | Guardia de Seguridad | 1 |
| Gerente | Asistente | 1 |
| Divulgador Cultural | S\P | 1 por cada 16 invitados |
| Artesano | S\P | 1 por cada 16 invitados |
| Artista | S\P | 1 por cada 16 invitados |

### Personal - Recurso

| Personal | Recurso | Cantidad |
|---|---|---|
| Chofer | Vehículo de Transporte | 1 |
| Limpieza | Implemento de Limpieza | 1 |
| Barman | Cocteleria | 1 |
| Chef | Utensilio de Cocina | 1 |
| Chef | Alimento | número de invitados |
| Organizador | Silla | número de invitados |
| Organizador | Mesa | 1 por cada 4 Sillas |
| Técnico en Sonido | Equipo de Audio | 1 |
| Técnico en Sonido | Altavoz | 1 por cada 20 invitados |
| Técnico en Iluminación | Proyector | 1 por cada 20 invitados |
| Mantenimiento | Pantalla | 1 |
| Cantante | Micrófono | 1 |
| Asistente Deportivo | Implementos deportivos | número de invitados |
| Salvavida | Equipo de Primeros Auxilios | 1 |
| Divulgador Cultural | Puesto de Venta/Feria/Artesanal | 1 por cada 1 invitado |
| Artesano | Puesto de Venta/Feria/Artesanal | 1 por cada 1 invitado |
| Artista | Puesto de Venta/Feria/Artesanal | 1 por cada 1 invitado |

2. Capacidad: 
En lugar de usar un solo número para la capacidad, usamos un rango. Esto permite implementar validaciones de seguridad: el sistema no solo debe impedir que entren x cantidad de personas a un área asignada, sino que debe alertar si el grupo es menor al mínimo y mayor al maximo requerido para que el área sea operativa. Tambien se ha de tener en cuenta la duración de los eventos que deben durar más de 1 hora y menos de 3 horas. 

3. Tiempo
Al definir turnos (Diurno/Nocturno/Completo) y tipos de jornada (no Limitado/Limitado),se permite programar la disponibilidad dinámica. Por ejemplo: el sistema no permitirá agendar un evento de "Coctelería" si el horario solicitado no coincide con la disponibilidad del personal de "Barman".

---

## Estructura del proyecto

```
Proyecto-Programaci-n-2026/
│
├── Report.md
├── README.md
└── Resource/
    ├── main.py                                 # Punto de entrada — ejecutar este archivo
    ├── interfaz.py                             # Apartado visual del programa
    ├── condiciones.py                          # Restriciones de tiempo, capacidad, etc
    ├── eventos.py                              # Lógica de carga y guardado de eventos
    ├── recursos.py                             # Almacen de datos del programa
    └── __pycache__/                            # Guardado de datos del programa
        ├── condiciones.cpython-313.pyc
        ├── eventos.cpython-313.pyc
        ├── interfaz.cpython-313.pyc
        └── recursos.cpython-313.pyc       
```

---

## Cómo ejecutar el proyecto

### Requisitos

- Python 3.10 o superior (se usan f-strings con comillas anidadas)
- No se requieren librerías externas

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/Marcos0808/Proyecto-Programaci-n-2026.git
cd Proyecto-Programaci-n-2026\Resource

# 2. Ejecutar el programa
python main.py
```

- NOTA: El programa carga automáticamente el estado guardado si existe. En caso de no existir, inicia desde cero.

---

## Funcionalidades

### Crear evento

El usuario completa el nombre del evento, selecciona el área, el horario, la cantidad de invitados y el personal a emplear, siempre y cuando se cumplan las siguientes condiciones:

- El área del evento esté vacante.
- Se respeten las reglas de capacidad de las distintas áreas (el número de invitados no debe ser inferior a la capacidad mínima ni superior a la máxima).
- Se respeten las reglas de tiempo: el personal debe estar disponible en el horario seleccionado y la duración del evento debe ser mayor a 1 hora y menor a 3 horas.
- Se permita la coexistencia con otros eventos en el mismo horario, siempre que no haya conflicto en el consumo de recursos, personal o invitados, y que las áreas de evento no coincidan.
- Se respeten las restricciones de dependencias.

### Más 

Los eventos se muestran en la interfaz una vez creados. El usuario puede visualizar los detalles de los eventos marcados, incluyendo: nombre, inicio, fin, fecha, área, invitados, personal y recursos. Además, se puede acceder a las siguientes secciones:

- Lugares: muestra las áreas de eventos con su capacidad mínima y máxima.
- Personal: muestra el listado de personal, su cantidad y horario.
- Recursos: muestra los recursos y su disponibilidad.

Cabe aclarar que esta información no se actualiza en tiempo real, ya que constituye la información base del programa. Asimismo, el sistema permite cancelar el evento seleccionado; una vez eliminado, los recursos se liberan inmediatamente.

### Guardar y Salir

Tras la creación exitosa del evento, los datos se almacenan de forma persistente. Al reiniciar la aplicación, el sistema carga automáticamente el estado guardado.

### Archivo de datos de ejemplo 

**Primer evento base**
- Nombre: Caminata en la playa
- Inicio: 6:30
- Fin: 8:00
- Fecha: 5/6/2026
- Área: Otra área
- Inivitados: 20
- Personal: Animación
- Recursos: -

**Segundo evento base**
- Nombre: Yoga
- Inicio: 9:45
- Fin: 11:30
- Fecha: 5/6/2026
- Área: Otra área
- Inivitados: 30
- Personal: Animación
- Recursos: -

**Tercero evento base**
- Nombre: Aqua Gym
- Inicio: 10:30
- Fin: 12:00
- Fecha: 5/6/2026
- Área: Piscina Pequeña
- Inivitados: 20
- Personal: Salvavidas, Animación
- Recursos: Equipo de Primeros Auxilios

**Cuarto evento base**
- Nombre: Juego de Tenis 
- Inicio: 12:00
- Fin: 14:00
- Fecha: 5/6/2026
- Área: Zona Deportiva
- Inivitados: 16
- Personal: Asistente Deportivo
- Recursos: Implementos Deportivos

**Quinto evento base**
- Nombre: Cumpleaños 
- Inicio: 14:00 
- Fin: 16:00
- Fecha: 5/6/2026
- Área: Salón Grande
- Inivitados: 35
- Personal: Organizador, Técnico en Sonido, Limpieza, Camarero, Chef, Animación 
- Recursos: Mesa, Silla, Equipo de Audio, Altavoz, Implementos de Limpieza, Utensilios de Cocina, Alimento   

**Sexto evento base**
- Nombre: Visita a las cuevas
- Inicio: 17:00
- Fin: 19:00
- Fecha: 5/6/2026
- Área: Área de Excursión
- Inivitados: 30
- Personal: Animación, Chofer, Guía
- Recursos: Vehículo de Transporte

**Septimo evento base**
- Nombre: Concierto
- Inicio: 19:30
- Fin: 21:40
- Fecha: 5/6/2026
- Area: Salón Grande
- Inivitados: 50
- Personal: Invitado Especiale, Cantante, Técnico en iluminación, Técnico en Sonido, Guardia de Seguridad, Limpieza, Mantenimiento, Gerente, Jefe de Seguridad, Barman  
- Recursos: Micrófono, Proyector, Equipo de Audio, Altavoz, Implementos de Limpieza, Pantalla y Coctelería

---

## Extra

Gracias a que el personal está categorizado por roles y no por nombres fijos, si el hotel decide contratar diez técnicos de sonido adicionales, el sistema solo requiere actualizar un valor entero en la base de datos sin necesidad de cambiar la lógica del código. Por lo tanto, el modelo actual permite, en fases futuras, implementar nuevas funciones.

---

## Agradecimiento

Deseo expresar mi más sincero agradecimiento por dedicar su valioso tiempo a la lectura de este proyecto. La revisión de este trabajo representa una oportunidad invaluable para recibir retroalimentación constructiva que contribuya al fortalecimiento de mi formación profesional. Agradezco profundamente su interés, su atención y el compromiso mostrado hacia el desarrollo de esta investigación, la cual refleja mi dedicación y esfuerzo constante por alcanzar la excelencia académica.
