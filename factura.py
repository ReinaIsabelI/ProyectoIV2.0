class factura:
    def __init__(self, razon_social, fecha, direccion_fiscal, cedula, telefono, descripcion, cantidad, precio, iva, total):
        self.razon_social = razon_social
        self.fecha = fecha
        self.direccion_fiscal = direccion_fiscal
        self.cedula= cedula
        self.telefono = telefono
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        self.iva = iva
        self.total = total


    def toDBCollection(self):
        return{
            'razon_social': self.razon_social, 
            'fecha': self.fecha,
            'direccion_fiscal': self.direccion_fiscal,
            'cedula': self.cedula,
            'telefono': self.telefono, 
            'descripcion': self.descripcion,
            'cantidad': self.cantidad,
            'precio': self.precio,
            'iva': self.iva,
            'total': self.total
        }