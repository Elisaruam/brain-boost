import matplotlib.pyplot as plt
from .progress_tracker import ProgressTracker

def analyze_overall_performance():
    """
    Analiza el rendimiento promedio en cada ejercicio y muestra un gráfico de barras.
    """
    tracker = ProgressTracker()
    exercises = ["memory_exercise", "mental_math", "general_knowledge", "logic_exercise"]
    
    average_scores = {}
    for exercise in exercises:
        scores = tracker.get_progress(exercise)
        # Verifica las puntuaciones y calcula el promedio
        print(f"Puntuaciones para {exercise}: {scores}")
        if scores:
            average = sum(scores) / len(scores)
            average_scores[exercise] = average
            print(f"Promedio para {exercise}: {average}")
        else:
            average_scores[exercise] = 0  # Si no hay datos, el promedio es 0
    
    # Crear el gráfico de puntuación promedio para cada ejercicio
    exercises = list(average_scores.keys())
    averages = list(average_scores.values())
    
    plt.figure(figsize=(8, 5))
    plt.bar(exercises, averages, color='skyblue')
    plt.title("Puntuación promedio en todos los ejercicios")
    plt.xlabel("Ejercicio")
    plt.ylabel("Puntuación Promedio")
    plt.ylim(0, 5)
    plt.show()


