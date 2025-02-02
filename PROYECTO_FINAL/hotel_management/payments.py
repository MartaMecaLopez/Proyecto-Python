import asyncio
import random

async def process_payment(customer_name, amount):
    """Simula el procesamiento de un pago."""
    print(f"Iniciando el procesamiento del pago para {customer_name} por la cantidad de {amount}€...")


    #Simulación del tiempo de procesamiento del pago:
    await asyncio.sleep(2) #2 segundos

    #Generamos un número aleatorio para simular si el pago fue exitoso o fallido
    payment_success = random.choice ([True, False])


    if payment_success:
        print(f"Pago de {amount}€ procesado con éxito para {customer_name}")
        return True
    else:
        print(f"Error al procesar el pago de {amount}€ para{customer_name}")
        return False
