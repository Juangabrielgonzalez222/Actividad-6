from clase import FechaHora
if __name__ == '__main__':
    #funciones del menú
    def op1(horario):
        hora=int(input("Ingrese la hora para sumar al del reloj:"))        
        resultado=horario+hora
        if(resultado!=-1):
            print("Hora nueva:",resultado)
            print("Horario nuevo:")
            horario.Mostrar()
        else:
            print("Ingresar valor horario entre 0-23 hs para restar al reloj")
    def op2(horario):
        hora=int(input("Ingrese la hora para restar a la del reloj:"))
        resultado=horario-hora
        if(resultado!=-1):
            print("Hora nueva:",resultado)
            print("Horario nuevo:")
            horario.Mostrar()
        else:
            print("Ingresar valor horario entre 0-23 hs para restar al reloj")
    def op3(horario):
        hora=int(input("Ingrese la hora para comparar:"))
        if horario > hora:
            print("La hora ingresada es menor")
        else:
            print("La hora ingresada es mayor")
    def op4():
        horario.Test()
    def op5():
        print("Usted salio del programa")
    
    print("Bienvenido al programa")
    d=int(input("Ingrese Dia: "))

    mes=int(input("Ingrese Mes: "))

    a=int(input("Ingrese Año: "))

    h=int(input("Ingrese Hora: "))

    m=int(input("Ingrese Minutos: "))

    s=int(input("Ingrese Segundos: "))
    horario=FechaHora(d,mes,a,h,m,s)
    op=None
    dicopciones={1:op1,2:op2,3:op3,4:op4,5:op5}
    while(op!=5):
        print("Menu:")
        print("Ingrese 1 para sumar hora")
        print("Ingrese 2 para restar hora")
        print("Ingrese 3 para comparar horas")
        print("Ingrese 4 para ejecutar un test")
        print("Ingrese 5 para salir")
        op=int(input("Imgrese opción:"))
        opcion=dicopciones.get(op,"No se encontro la opcion rango 1-4, 4 para salir")
        if(op==4 or op==5):
            opcion()
        else:
            opcion(horario)
        
    
        
        
    


