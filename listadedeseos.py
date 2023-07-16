class listadedeseos:
    def __init__(self, producto, cantidad, precio):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def toDBCollection(self):
        return{
            'producto': self.producto,
            'cantidad': self.cantidad,
            'precio': self.precio,
        }