class Room:
    def __init__(self, room_number: int, room_type: str,available: bool = True):
        #Inicia una nueva habitación con el número, tipo y estado de disponibilidad
        self.room_number = room_number # Número único de la habitación
        self.room_type = room_type # Tipo de habitación (individual, doble, suite, etc.)
        self.available = available  # Estado de disponibilidad (True si está libre, False si está ocupada)


    def __str__(self):
        #Representación en texto de la habitación
        availability = "Disponible" if self.available else "Ocupada"
        return f"Habitación {self.room_type}, {self.room_number} está: {availability}"    

class RoomManagement:
    def __init__(self):
        #Inicia un diccionario vacío para almcenar las habitaciones
        self.rooms = {}

    def add_room(self, room: Room):
        """Agrega una nueva habitación al sistema."""
        if room.room_number in self.rooms:
            print(f"Error: La habitación {room.room_number} ya existe")
        else:
            self.rooms[room.room_number] = room
            print(f"Habitación {room.room_number} agregada correctamente")   

    def check_availability(self, room_number: int):
        """Verifica si una habitación está disponible."""
        room = self.rooms.get (room_number)
        if room:
            return "Disponible" if room.available else "Ocupada"
        else:
            return "Habitación no encontrada"
        
    def update_availability (self, room_number: int, available: bool):    
        #Actualiza el estado de disponibilidad de la habitación
        room = self.rooms.get (room_number)
        if room:
            room.available = available
            print(f"El estado de la habitación {room_number} ha sido actualizado")
        else:
            print(f"Error: La habitación {room_number} no existe")    


#COMPROBACIÓN DE QUE EL CÓDIGO FUNCIONA 

if __name__ == "__main__":
    # Creamos una instancia de RoomManagement
    room_management = RoomManagement()

    # Creamos algunas habitaciones
    room1 = Room(101, "Individual")
    room2 = Room(102, "Doble")
    room3 = Room(103, "Suite", available=False)  # Esta habitación está ocupada

    # Agregamos las habitaciones al sistema
    room_management.add_room(room1)
    room_management.add_room(room2)
    room_management.add_room(room3)

    # Verificamos la disponibilidad de las habitaciones
    print(room_management.check_availability(101))  # Debería decir "Disponible"
    print(room_management.check_availability(103))  # Debería decir "Ocupada"
    print(room_management.check_availability(105))  # No existe, debería decir "Habitación no encontrada."

    # Actualizamos el estado de una habitación
    room_management.update_availability(101, False)  # Marcamos la habitación 101 como ocupada
    print(room_management.check_availability(101))  # Debería decir "Ocupada"


