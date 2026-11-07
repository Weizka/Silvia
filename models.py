import random


class Mensaje:
    """Clase que maneja el mensaje principal y mensajes secundarios."""

    def __init__(self, destinataria: str, mensaje_principal: str, autor: str = "Con cariño"):
        self.destinataria = destinataria
        self.mensaje_principal = mensaje_principal
        self.autor = autor
        self.mensajes_secundarios = [
            "Eres increíble 💕",
            "Me haces muy feliz 🌟",
            "Cada momento contigo es especial ✨",
            "Eres única y maravillosa 🌹",
            "Gracias por existir 💖",
            "Contigo todo es mejor 🦋",
            "Eres mi persona favorita 🌸",
            "Me encantas tal como eres 💝",
            "Contigo el tiempo vuela ⏰",
            "Eres magia pura ✨"
        ]

    def obtener_mensaje_aleatorio(self) -> str:
        """Retorna un mensaje secundario aleatorio."""
        return random.choice(self.mensajes_secundarios)

    def obtener_destinataria(self):
        return self.destinataria

    def obtener_mensaje_principal(self):
        return self.mensaje_principal