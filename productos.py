class productos:
    def __init__(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def toDBCollection(self):
        return{
            'nombre': self.nombre, 
            'precio': self.precio,
            'cantidad': self.cantidad,
            'categoria': self.categoria
        }