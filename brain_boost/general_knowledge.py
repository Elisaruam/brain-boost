import random

questions = {
    "fácil": {
        "¿Cuál es la capital de Francia?": "París",
        "¿Cuántos planetas tiene el sistema solar?": "8"
    },
    "intermedio": {
        "¿Quién escribió 'Cien años de soledad'?": "Gabriel García Márquez",
        "¿Qué es el teorema de Pitágoras?": "a^2 + b^2 = c^2"
    },
    "difícil": {
        "¿En qué año comenzó la Segunda Guerra Mundial?": "1939",
        "¿Cuál es la fórmula química del agua?": "H2O"
    }
}

def general_knowledge(difficulty="fácil", tracker=None):
    question, answer = random.choice(list(questions[difficulty].items()))
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        result = "¡Correcto! Sabes mucho."
        score = 5
    else:
        result = f"Incorrecto. La respuesta correcta era: {answer}"
        score = 2
    
    print(result)
    
    # Actualiza el progreso si el tracker está presente
    if tracker is not None:
        tracker.update_progress("general_knowledge", score)
    
    return result
