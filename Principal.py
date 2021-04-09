from typing import Dict, Any

import requests

from Pedido import Pedido
from Delivery import Delivery
from Pizza import Pizza

pedidos = []
tipos_pizza= []
delivery = {}

def cargar_api():
    global delivery
    api_respone = requests.get('https://a.nacapi.com/pizzamet')
    data:dict = api_respone.json()
    menu = data["menu"]
    for elemento in menu:
        pizza = Pizza(elemento['pizza'],elemento['ingredientes'], elemento['precio'] )
        tipos_pizza.append(pizza)


    delivery = data["delivery"][0]



def seleccionar_pizzas(cantidad):
    pizzas = []
    for numero in range(cantidad):
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(tipos_pizza)))
        entrada_valida = False
        while not entrada_valida:
            try:
                posicion = int(input("Seleccione su pizza"))
                entrada_valida = True
            except:
                print("pizza invalida")

        menu_tamanos = '''Selecione el tamaño:
        1. pizza de 8 porciones
        2. pizza de 10 porciones
        3. pizza de 12 porciones
        Su opcion: '''
        print(menu_tamanos)
        entrada_valida = False
        while not entrada_valida:
            try:
                tamano = int(input("Seleccione el tamaño de la pizza"))
                entrada_valida = True
            except:
                print("tamaño inválido")

        menu_tipo_coccion = '''
        Selecione el tipo de coocion:
        1. Parrilla
        2. Leña                
        Su opcion: '''

        print(menu_tipo_coccion)
        entrada_valida = False
        while not entrada_valida:
            try:
                tipo = int(input("Seleccione el tipo de cocción"))
                entrada_valida = True
            except:
                print("tamanño inválido")

        pizza= {}
        pizza["pizza"]= tipos_pizza[posicion]
        pizza["tamano"] = tamano
        pizza["tipo"] = Pizza.coccion[tipo]
        pizza["precio"] = calcular_total(pizza)
        pizzas.append(pizza)
    return pizzas

def calcular_total(pizza):
    precio = int(pizza["pizza"].precios[pizza["tipo"]][:-1])
    if pizza["tamano"] == 2:
        precio += 4
    elif pizza["tamano"] == 3:
        precio += 10
    print("la pizza tiene un costo total de {}".format(precio))
    return precio

def calcular_total_factura(pedido):
    total_factura = 0
    for pizza in pedido.pizzas:
        total_factura += pizza["precio"]
    if pedido.delivery is not None:
        pedido.costo_delivery = delivery[pedido.delivery.municipio]
        total_factura+=pedido.costo_delivery
    if descuento_primo(pedido.cedula):
        total_factura = total_factura*0.95
    return total_factura

def descuento_primo(cedula):
    digito = cedula%10
    return es_primo(digito,digito-1)

def es_primo(digito,dividendo):
    if(dividendo<2):
        return True
    else:
        if(digito%dividendo == 0):
            return False
        else:
            return es_primo(digito,dividendo-1)

def solicitar_datos_delivery():
    direccion = input("Indique su direcion: ")

    print('\n'.join('{}: {} '.format(*k) for k in enumerate(delivery.keys())))
    entrada_valida = False
    while not entrada_valida:
        try:
            indice_municipio = int(input("Seleccione el municipio"))
            entrada_valida = True
        except:
            print("municipio inválido")

    municipio = list(delivery.keys())[indice_municipio]
    entrada_valida = False
    while not entrada_valida:
        try:
            telefono = int(input("Indique su numero de telefono"))
            entrada_valida = True
        except:
            print("telefono inválido")

    deliv = Delivery(direccion,municipio,telefono)
    return deliv


def crear_pedido():
    entrada_valida = False
    while(not entrada_valida):
        try:
            tipo_pedido = int(input(""""
            Tipo de pedido:
            1.Mostrador
            2.Teléfono
            Su opción: """ ))
            if(tipo_pedido in range(1,3)):
                entrada_valida = True
            else:
                print("Tipo de pedido invalida")
        except:
            print("Forma de pago invalida")
    nombre = input("Indique su nombre")

    entrada_valida = False
    while(not entrada_valida):
        try:
            cedula = int(input("Indique el numero de cedula" ))
            entrada_valida = True
        except:
            print("Cedula invalida")

    entrada_valida = False
    while(not entrada_valida):
        try:
            forma_pago = int(input(""""
            Seleccione la forma de pago:
            1.Debito
            2.Efetivo
            3.Zelle
            Su opcion: """ ))
            if(forma_pago in range(1,4)):
                entrada_valida = True
            else:
                print("Forma de pago invalida")
        except:
            print("Forma de pago invalida")
    entrada_valida = False
    while(not entrada_valida):
        try:
            cantidad = int(input("Indique la cantidad de pizzas que desea" ))
            if(cantidad>0):
                entrada_valida = True
            else:
                print("Cantidad de pizzas inválida")
        except:
            print("Cedula invalida")
    pedido = Pedido(nombre,cedula,forma_pago,tipo_pedido,cantidad)

    pizzas = seleccionar_pizzas(cantidad)
    pedido.pizzas = pizzas

    if(tipo_pedido == 2):
        delivery = solicitar_datos_delivery()
        pedido.delivery = delivery

    pedido.total = calcular_total_factura(pedido)
    pedido.mostrar_factura()
    pedidos.append(pedido)


def mostrar_estadisticas():
    pass

def guardar_texto():
    pass

def main():
    cargar_api()
    opcion =0
    while(opcion != 4):
        entrada_valida = False
        menu= '''Bienvenido
            1. Nuevo pedido
            2. Estadisticas
            3. Guardar txt
            4. salir
            Su opcion: '''
        while(not entrada_valida):
            try:
                opcion = int(input(menu))
                if(opcion in range(1,5)):
                    entrada_valida = True
                else:
                    print("opcion invalida")
            except:
                print("opcion invalida")
        if opcion == 1:
            crear_pedido()

        elif opcion == 2:
            mostrar_estadisticas()
        elif opcion == 3:
            guardar_texto()

main()




