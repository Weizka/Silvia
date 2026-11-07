from flask import Flask
from models import Mensaje
from views import GeneradorHTML


class AplicacionWeb:
    """Clase que orquesta la aplicación Flask."""

    def __init__(self):
        self.app = Flask(__name__)
        self.mensaje = Mensaje(
            destinataria="Silvia Puentes",
            mensaje_principal=(  # ← Cambié 'contenido' por 'mensaje_principal'
                "Me encanta pasar el tiempo contigo y me gustó mucho "
                "el tiempo que pasamos. Espero pasar más tiempo contigo."
            )
        )
        self.generador = GeneradorHTML(self.mensaje)
        self._configurar_rutas()

    def _configurar_rutas(self):
        @self.app.route("/")
        def inicio():
            return self.generador.generar()

    def ejecutar(self, host="127.0.0.1", puerto=5000):
        print(f"💖 Abre tu navegador en: http://{host}:{puerto}")
        self.app.run(host=host, port=puerto, debug=True)


if __name__ == "__main__":
    mi_pagina = AplicacionWeb()
    mi_pagina.ejecutar()