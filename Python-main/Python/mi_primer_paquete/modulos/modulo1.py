class cliente:
    def __init__(self, nombre, apellido, mail, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.edad = edad

    
    def __str__(self):
        return f"Nombre {self.nombre}, " f"Apellido {self.apellido}, " f"mail {self.mail}, " f"Edad {self.edad}" 

