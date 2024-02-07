class Pagina:
    def __init__(self, contenido):
        self.contenido = contenido

class MarcoPagina:
    def __init__(self, numero):
        self.numero = numero
        self.pagina = None

class TablaPaginas:
    def __init__(self, numero_paginas):
        self.entradas = [None] * numero_paginas

class Segmento:
    def __init__(self, base, limite):
        self.base = base
        self.limite = limite

class TablaSegmentos:
    def __init__(self, numero_segmentos):
        self.entradas = [None] * numero_segmentos

class Proceso:
    def __init__(self, nombre, numero_paginas, numero_segmentos):
        self.nombre = nombre
        self.tabla_paginas = TablaPaginas(numero_paginas)
        self.tabla_segmentos = TablaSegmentos(numero_segmentos)

# Crear un proceso con 3 páginas y 2 segmentos
proceso = Proceso("Proceso1", 3, 2)

# Asignar marcos de página a las páginas del proceso
marcos_pagina = [MarcoPagina(i) for i in range(3)]
for i, marco in enumerate(marcos_pagina):
    marco.pagina = Pagina(f"Contenido de la página {i}")
    proceso.tabla_paginas.entradas[i] = marco

# Asignar segmentos al proceso
segmentos = [Segmento(0, 10), Segmento(20, 30)]
for i, segmento in enumerate(segmentos):
    proceso.tabla_segmentos.entradas[i] = segmento

# Imprimir información del proceso
print(f"Proceso: {proceso.nombre}")
print("Tabla de Páginas:")
for i, entrada in enumerate(proceso.tabla_paginas.entradas):
    print(f"Página {i}: Marco {entrada.numero} - Contenido: {entrada.pagina.contenido}")

print("Tabla de Segmentos:")
for i, entrada in enumerate(proceso.tabla_segmentos.entradas):
    print(f"Segmento {i}: Base {entrada.base}, Límite {entrada.limite}")
