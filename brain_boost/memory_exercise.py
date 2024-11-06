# brain_boost/memory_exercise.py

import random
import time

def memory_exercise():
    items = ["apple", "car", "house", "tree", "book", "cat", "river"]
    sequence = random.sample(items, 3)
    print("Memoriza esta secuencia:", sequence)
    time.sleep(5)  
    print("\n" * 100)  
    answer = input("¿Cuál era la secuencia? Separa cada palabra con una coma: ")
    if answer.split(", ") == sequence:
        return "¡Correcto! Buena memoria."
    else:
        return f"Incorrecto. La secuencia correcta era: {sequence}"
