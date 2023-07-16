class auditoria:
    def __init__(self, usuario, fecha, modulo):
        self.usuario = usuario
        self.fecha = fecha
        self.modulo = modulo
       
    def toDBCollection(self):
        return{
            'usuario': self.usuario, 
            'fecha': self.fecha,
            'modulo': self.modulo,
        }