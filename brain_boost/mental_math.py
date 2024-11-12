import random

def mental_math(difficulty="fácil", tracker=None):
    ranges = {"fácil": (1, 10), "intermedio": (10, 50), "difícil": (50, 100)}
    num1 = random.randint(*ranges[difficulty])
    num2 = random.randint(*ranges[difficulty])
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)
    
    user_answer = int(input(f"¿Cuál es el resultado de {question}? "))
    if user_answer == correct_answer:
        result = "¡Correcto! Buen cálculo mental."
        score = 5  # Puntuación alta para respuesta correcta
    else:
        result = f"Incorrecto. La respuesta correcta era: {correct_answer}"
        score = 2  # Puntuación baja para respuesta incorrecta
    
    print(result)
    
    # Actualiza el progreso si el tracker está presente
    if tracker is not None:
        tracker.update_progress("mental_math", score)
    
    return result
