from collections import defaultdict
from datetime import datetime

class Reservation:
    def __init__(self, reservation_id: int, customer_id: int, room_id: int, check_in_date: str, check_out_date: str):
        """Inicia una nueva reserva con los detalles"""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def __str__ (self):
        #Representación en texto de la reserva 
        return f"Reserva {self.reservation_id} - Cliente {self.customer_id}, Habitación {self.room_id}, Fecha de entrada {self.check_in_date} y fecha de salida {self.check_out_date}"   


        

class ReservationSystem:
    def __init__(self):
        #Inicia un diccionario vacío para almacenar las reservas
        self.reservations = {}

    def add_reservation(self, reservation: Reservation):
        """Agrega una nueva reserva al sistema."""
        if reservation.reservation_id in self.reservations:
            print (f"Error: La reserva con ID {reservation.reservation_id} ya existe")
        else:
            self.reservations[reservation.reservation_id] = reservation
            print(f"Reserva {reservation.reservation_id} agregada correctamente")
        

    def cancel_reservation(self, reservation_id: int):
        """Cancela una reserva existente por ID."""
        if reservation_id in self.reservations:
            del self.reservations[reservation_id]
            print(f"Reserva {reservation_id} cancelada correctamente")
        else:
            print(f"Error: No se encontró la reserva con ID {reservation_id}") 


    def get_reservation (self, reservation_id: int):
        #Obtiene la información de una reserva por ID
        return self.reservations.get(reservation_id, "Reserva no encontrada") 



#COMPROBACIÓN DE QUE EL CÓDIGO FUNCIONA 
if __name__ == "__main__":
    # Creamos una instancia de ReservationSystem
    reservation_system = ReservationSystem()

    # Creamos algunas reservas
    reservation1 = Reservation(1, 1, 101, "2025-02-10", "2025-02-15")
    reservation2 = Reservation(2, 2, 102, "2025-02-20", "2025-02-25")

    # Agregamos las reservas al sistema
    reservation_system.add_reservation(reservation1)
    reservation_system.add_reservation(reservation2)

    # Intentamos obtener una reserva
    print(reservation_system.get_reservation(1))  # Debería mostrar los detalles de la reserva 1
    print(reservation_system.get_reservation(3))  # No existe, debería devolver "Reserva no encontrada"

    # Intentamos cancelar una reserva
    reservation_system.cancel_reservation(1)  # Debería cancelar la reserva 1
    print(reservation_system.get_reservation(1))  # Debería decir que la reserva no se encuentra


                


