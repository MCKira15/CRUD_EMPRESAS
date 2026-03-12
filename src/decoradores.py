from src.utils import limpiar,titulo,pausa

def pantalla(nombre_pantalla):
    def decorador(func):
        def envoltura(*args, **kwargs):
            limpiar()
            titulo(nombre_pantalla)
            return func(*args, **kwargs)
        return envoltura
    return decorador