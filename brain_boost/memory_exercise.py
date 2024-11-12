import random
import time

def memory_exercise(difficulty="fácil"):
    items = ["manzana", "coche", "casa", "árbol", "libro", "gato", "río"]
    length = {"fácil": 3, "intermedio": 5, "difícil": 7}[difficulty]
    sequence = random.sample(items, length)
    
    print("Memoriza esta secuencia:", sequence)
    time.sleep(3)  # Ajusta el tiempo si quieres un mayor desafío
    print("\n" * 100)  # Borra la pantalla para ocultar la secuencia
    
    answer = input("¿Cuál era la secuencia? Separa cada palabra con una coma: ")
    if answer.split(", ") == sequence:
        return "¡Correcto! Buena memoria."
    else:
        return f"Incorrecto. La secuencia correcta era: {sequence}"
