import json
import os

class ProgressTracker:
    def __init__(self, file_path="progress.json"):
        self.file_path = file_path
        self.load_progress()

    def load_progress(self):
        # Carga el progreso desde el archivo JSON si existe
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.data = json.load(file)
        else:
            self.data = {}

    def save_progress(self):
        # Guarda el progreso actual en el archivo JSON
        with open(self.file_path, "w") as file:
            json.dump(self.data, file)

    def update_progress(self, exercise, score):
        # Actualiza la puntuación del ejercicio
        if exercise not in self.data:
            self.data[exercise] = []
        self.data[exercise].append(score)
        self.save_progress()

    def get_progress(self, exercise):
        # Obtiene el progreso de un ejercicio específico
        return self.data.get(exercise, [])
    
    def reset_progress(self):
        """
        Limpia todos los datos de progreso guardados en progress.json.
        """
        self.data = {}
        self.save_progress()
