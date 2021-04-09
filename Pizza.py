class Pizza:
    porc8 = 8
    porc10 = 10
    porc12 = 12
    coccion= {1:"a la parrilla", 2:"a la leña"}
    def __init__(self, nombre, ingredientes, precios):
        self.precios = precios
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pizzas = []



    def __str__(self) -> str:
        return '''nombre:{}
        ingredientes: {}
        precios: {}'''.format(self.nombre,self.ingredientes, self.precios)