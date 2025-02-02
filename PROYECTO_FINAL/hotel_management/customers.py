class Customer:
    def __init__(self, customer_id: int, name: str, email: str, phone: str):
        #inicializa un nuevo cliente con los datos básicos
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        #sirve para mostrar la información del cliente en un formato de texto
        return f" Cliente {self.customer_id}: {self.name}, email: {self.email}, Teléfono {self.phone}"    

class CustomerManagement:
    def __init__(self):
        #Inicializa un diccionario vacío para almacenar los clientes
        self.customers = {}

    def add_customer(self, customer: Customer):
        """Agrega un nuevo cliente al sistema."""
        if customer.customer_id in self.customers:
            print(f"Error: El cliente con ID {customer.customer_id} ya existe")
        else:
            self.customers [customer.customer_id] = customer
            print(f"Cliente {customer.name} agregado correctamente")

    def get_customer(self, customer_id: int):
       """Obtiene la información de un cliente por ID."""
       return self.customers.get(customer_id, "Cliente no encontrado")
    
#COMPROBACIÓN DE QUE EL CÓDIGO FUNCIONA 

if __name__ == "__main__":
    # Creamos una instancia de CustomerManagement
    manager = CustomerManagement()

    # Creamos algunos clientes
    cliente1 = Customer(1, "Marta López", "marta@email.com", "123456789")
    cliente2 = Customer(2, "Carlos Pérez", "carlos@email.com", "987654321")

    # Agregamos los clientes al sistema
    manager.add_customer(cliente1)
    manager.add_customer(cliente2)

    # Intentamos obtener un cliente
    print(manager.get_customer(1))  # Debería mostrar los datos de Marta López
    print(manager.get_customer(3))  # No existe, debería devolver "Cliente no encontrado"    