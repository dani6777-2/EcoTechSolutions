from abc import ABC, abstractmethod


class MenuBase(ABC):
    """Clase abstracta base para menús."""

    def __init__(self, servicio):
        self.servicio = servicio

    def limpiar_input(self, prompt):
        try:
            return input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            return ""

    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass
