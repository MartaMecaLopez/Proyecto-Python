import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime

async def main():
    # Inicializar sistemas
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()
    reservation_system = ReservationSystem()

    # Crear habitaciones
    customer1 = Customer (1, "Marta", "marta@email.com", "123456789")
    customer2 = Customer (1, "Marc", "marc@email.com", "987654321")

    # Agregar clientes
    customer_mgmt.add_customer(customer1)
    customer_mgmt.add_customer(customer2)

    #Crear habitaciones
    room1 = Room(101, "Individual", True)
    room2 = Room(102, "Doble", False)

    #Agregar habitaciones al sistema
    room_mgmt.add_room(room1)
    room_mgmt.add_room(room2)


    #Verificar disponibilidad de las habitaciones
    print(f"Disponibilidad de la habitación 01: {room_mgmt.check_availability(101)}")
    print(f"Disponibilidad de la habitación 01: {room_mgmt.check_availability(102)}")
    
    #Hacer una reserva si la habitación está disponible
    if room_mgmt.check_availability(101) == "Disponible":
        reservation1 = Reservation (1, customer1.customer_id, room1.room_number, "01-02-2025", "12-02-2025")
        reservation2 = Reservation(2, customer2.customer_id, room2.room_number, "2025-02-20", "2025-02-25")
       
       
        reservation_system.add_reservation(reservation1)
        reservation_system.add_reservation(reservation2)
        print(f"Reserva autorizada: {reservation1}")
        print(f"Reserva autorizada: {reservation2}")

    # Procesar pago asincrónicamente
        print(f"Procesando el pago para el cliente {customer1.name}...")
        await process_payment(customer1.name, 150)

    #Intentar reservar una habitación ocupada
    if room_mgmt.check_availability(102) == "Ocupada":
        print(f"La habitación {room2} no está disponible para reserva")    
    pass

if __name__ == "__main__":
    asyncio.run(main())

