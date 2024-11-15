from IPython.display import clear_output
import random
import time

def memory_exercise(difficulty="fácil", tracker=None):
    """
    Presenta una secuencia de palabras para que el usuario las memorice.

    Parameters:
    - difficulty (str): Nivel de dificultad ("fácil", "intermedio", "difícil").
    - tracker (ProgressTracker, optional): Objeto para guardar el progreso.

    Returns:
    - result (str): Mensaje de resultado (correcto/incorrecto).
    """
    items = ["manzana", "coche", "casa", "árbol", "libro", "gato", "río"]
    length = {"fácil": 3, "intermedio": 5, "difícil": 7}[difficulty]
    sequence = random.sample(items, length)
    
    print("Memoriza esta secuencia:", ", ".join(sequence))
    time.sleep(3)
    
    clear_output(wait=True)
    print("La secuencia ha desaparecido.\n")
    
    answer = input("¿Cuál era la secuencia? Escribe las palabras separadas por comas: ")
    
    answer_list = [word.strip().lower() for word in answer.split(",")]
    sequence_list = [word.lower() for word in sequence]

    if answer_list == sequence_list:
        result = "¡Correcto! Buena memoria."
        score = 5
    else:
        result = f"Incorrecto. La secuencia correcta era: {', '.join(sequence)}"
        score = 2
    
    print(result)
    
    if tracker is not None:
        tracker.update_progress("memory_exercise", score)
    
    return result

