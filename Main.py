from helpers import Helper
from departamentos import Departamento
from empleados import Empleado
from cargo import Cargo 
import os

#Busca codigo cargo
def buscargo(cod):
  cod=int(cod)
  cCar = 0     
  for pos in range(0,len(Cargo.cargos)):
    cargo = Cargo.cargos[pos]
    if cargo["codigo"] == cod:
       cCar = cargo["cargo"]
       break
  return cCar  

#Busca codigo departamento
def busdepartamento(cod):
  cod=int(cod)
  cDep = 0     
  for pos in range(0,len(Departamento.departamentos)):
    departamento = Departamento.departamentos[pos]
    if departamento["codigo"] == cod:
       cDep = departamento["departamento"]
       break
  return cDep

#Repite el listado
helper = Helper()
lista = ["1) Cargo","2) Departamento","3) Empleados","4) Salir"]
opcion=""

#Menu principal
while opcion != "4":
  os.system("cls")
  opcion = helper.menu(lista,"*"*20+" MENÚ FICHA PERSONAL "+"*"*20)
  
  #Menu Cargo
  if opcion == "1":
    opc1=""
    while opc1 != "3":
      os.system("cls")
      opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"*"*20+" MANTENIMIENTO DE CARGOS "+"*"*20)
      os.system("cls")
      
      #ingreso
      if opc1 == "1":
        nombre= ""
        #valida cargo
        while len(nombre) > 20 or nombre == "":
          print("*"*20,"INGRESO DE CARGOS","*"*20)
          nombre= input("Cargo: ")
          os.system("cls")
        art = Cargo(nombre)
        articulo = art.registro()
        Cargo.cargos.append(articulo)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
        
      #consulta  
      elif opc1 == "2":
        print("*"*20,"LISTADO DE CARGOS","*"*20)
        print("Código"," "*5,"Descripción"," "*5)
        for art in Cargo.cargos:
          cod = art["codigo"]
          des = art["cargo"]
          print(" "*2,cod," "*7,des," "*(15-len(des)))
        print("")
        print("*"*59)
        input("Presione una tecla para continuar...")

  #Menu departamento
  elif opcion == "2":       
    opc2=""
    while opc2 != "3":
      os.system("cls")
      opc2 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"*"*20+" MANTENIMIENTO DE DEPARTAMENTOS "+"*"*20)
      os.system("cls")
      
      #ingreso
      if opc2 == "1":
        nombre= ""
        
        #valida departamento
        while len(nombre) > 20 or len(nombre) < 5:
          os.system("cls")
          print("*"*20,"INGRESO DE DEPARTAMENTOS","*"*20)
          nombre= input("Departamento: ")
        dep = Departamento(nombre)
        categoria = dep.registro()
        Departamento.departamentos.append(categoria)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      
      #consulta
      elif opc2 == "2":
        print("*"*20,"LISTADO DE DEPARTAMENTOS","*"*20)
        print("Código"," "*5,"Descripción")
        for art in Departamento.departamentos:
          cod2 = art["codigo"]
          des2 = art["departamento"]
          print(" "*2,cod2," "*7,des2," ")
        print("")
        print("*"*66)
        input("Presione una tecla para continuar...")
   
  #Menu empleado      
  elif opcion == "3":
    opc3=""
    while opc3 != "3":
      os.system("cls")
      opc3 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"*"*20+" MANTENIMIENTO DE EMPLEADOS "+"*"*20)
      os.system("cls")
      
      #ingreso
      if opc3 == "1":
        print("*"*20,"INGRESO DE EMPLEADOS","*"*20)        
        nombre= input("Ingrese Nombre : ")
        
        #valida nombre
        while len(nombre) > 20 or len(nombre) < 3:
          os.system("cls")
          print("INCORRECTO: ingrese de 3 a 20 digitos...")
          nombre= input("Ingrese Nombre : ")
        os.system("cls")
      
        #valida cedula
        cedula=0
        while True:
          try:
            cedula=input("Ingrese Cedula: ")
            error=int(cedula)      
            while len(cedula) != 10 :
              os.system("cls")
              print("INCORRECTO: ingrese 10 números...")
              cedula= input("Ingrese Cedula : ")
              error=int(cedula)
              os.system("cls") 
            break
          except ValueError:
            os.system("cls")     
            print("INCORRECTO: ingrese 10 números...")
        os.system("cls")
         
        #valida codigo cargo
        while True:
          try:  
            cargo= input("Ingrese codigo del Cargo : ")
            cargo in str(buscargo(cargo))
            if buscargo(cargo) == 0:
              os.system("cls")
              print ("INCORRECTO: Asegurese que el cargo exista...")
              continue
            else:
              break
          except ValueError:  
            os.system("cls")
            print ("INCORRECTO: Asegurese que el cargo exista...")
        os.system("cls")    
        
        #valida codigo departamento
        while True:
          try:  
            departamento= input("Ingrese codigo del Departamento : ")
            departamento in str(buscargo(departamento))
            if buscargo(departamento) == 0:
              os.system("cls")
              print ("INCORRECTO: Asegurese que el departamento exista...")
              continue
            else:
              break
          except ValueError:  
            os.system("cls")
            print ("INCORRECTO: Asegurese que el departamento exista...")
        os.system("cls") 
        
        #valida sueldo  
        sueldo=0.00
        while True:
          try:
            sueldo=float(input("Ingrese Sueldo: $ "))
            break
          except ValueError:
            os.system("cls")
            print("INCORRECTO: Asegurese que sean enteros o decimales...")
        os.system("cls") 

        #muestra listado a usar
        print("*"*20,"INGRESO DE EMPLEADOS","*"*20)
        print("Nombre                 : ",nombre)
        print("Cedula                 : ",cedula)
        print("Codigo del Cargo       : ",cargo)
        print("Codigo del Departamento: ",departamento)
        print("Sueldo                 :  $",sueldo)
        
        #registro
        art = Empleado(nombre,cedula,cargo,departamento,sueldo)
        articulo = art.registro()
        Empleado.empleados.append(articulo)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      
      #consulta
      elif opc3 == "2":
        print("*"*29,"LISTADO DE EMPLEADOS","*"*29)
        print("Código"," "*3,"Nombre"," "*3,"Cédula","       Cargo   ","     Departamento","      Sueldo")
        for art in Empleado.empleados:
          cod = art["codigo"]
          nom = art["nombre"]
          ced =art["cedula"] 
          cCar = art["cargo"]
          codCar = buscargo(cCar)
          cDep = art["departamento"]
          codDep = busdepartamento(cDep)
          sue = art["sueldo"]
          print(" "*2,cod," "*5,nom," "*(9-len(nom)),ced," "*(12-len(ced)),codCar,
                " "*(12-len(str(codCar))),codDep," "*(17-len(str(codDep))),"$" ,sue," "*(0-len(str(sue))))
        print("")
        print("*"*80)
        input("Presione una tecla para continuar...")
  
  #Menu salir              
  elif opcion == "4":
    print(" ")
    print("Elegiste Salir")
   
        
print("Gracias por visitarnos, vuelve pronto")