class Pedido:

    def __init__(self,nombre_cliente,cedula,forma_pago, tipo_pedido, cant_pizzas):
        self.nombre_cliente=nombre_cliente
        self.cedula=cedula
        self.forma_pago = forma_pago
        self.tipo_pedido = tipo_pedido
        self.cant_pizzas = cant_pizzas
        self.delivery = None
        self.costo_delivery =0
        self.total = 0
        self.pizzas = []
        self.formas_pago = {1:"debito", 2:"efectivo", 3: "zelle"}
        self.pedido = { 1:"mostrador", 2: "telefono"}

    def mostrar_factura(self):
        print('''
Factura
    nombre: {}
    cedula: {}
    forma de pago: {}
    tipo de pedido {} '''.format(self.nombre_cliente,self.cedula, self.formas_pago[self.forma_pago], self.pedido[self.tipo_pedido]))
        for pizza in self.pizzas:
            print('{} {}'.format(pizza["pizza"].nombre,pizza["precio"]))
        if(self.delivery is not None):
            print("delivery {}".format(self.costo_delivery))
        print("total: {}", self.total)

