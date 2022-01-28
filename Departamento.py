class Departamento:
    secuencia=0
    departamentos = []
    
    def __init__(self,descrip):
        Departamento.secuencia +=1
        self.codigo1=Departamento.secuencia
        self.descripcion=descrip
 
    def registro(self):
        return {"codigo":self.codigo1,"departamento":self.descripcion}