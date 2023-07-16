class carrito:
    def __init__(self, producto, precio, cantidad, iva):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
        self.iva = iva

    def toDBCollection(self):
        return{
            'producto': self.producto, 
            'precio': self.precio,
            'cantidad': self.cantidad,
            'iva': self.iva
        }