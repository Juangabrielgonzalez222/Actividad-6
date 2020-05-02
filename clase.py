class FechaHora():
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __minutos=0
    __segundos=0
    def __init__(self,dia=1,mes=1,año=2020,hora=0,minutos=0,segundos=0):
        if((hora<24 and hora>-1)and (minutos<60 and minutos>-1) and(segundos<60 and segundos>-1) and (mes>0 and mes<13)):
            if ((año%400==0)or(año%100!=0 and año%4==0)):
                listameses=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                listameses=[31,28,31,30,31,30,31,31,30,31,30,31]
            if(dia<=listameses[mes-1] and dia>0):     
                self.__dia=dia
                self.__mes=mes
                self.__año=año
                self.__hora=hora
                self.__minutos=minutos
                self.__segundos=segundos
            else:
                print("dia incorrecto el rango segun el mes ingresado {} es entre:1-{}".format(mes,listameses[mes-1]))
        else:
            print("verifique valor de hora 0-23,minutos 0-59,segundos 0-59 y mes 1-12")
    def Mostrar(self):
        print("{}/{}/{} {}:{}:{}".format(self.__dia, self.__mes,self.__año,self.__hora, self.__minutos,self.__segundos))
    def __add__(self,hora):
        if (hora>-1 and hora<24):   
            self.__hora+=hora
            if ((self.__año%400==0)or (self.__año%100!=0 and self.__año%4==0)):
                listameses=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                listameses=[31,28,31,30,31,30,31,31,30,31,30,31]
            if (self.__hora>23):
                self.__hora-=24
                self.__dia+=1
            if self.__dia>listameses[self.__mes-1]:
                self.__dia-=listameses[self.__mes-1]
                self.__mes+=1
            if self.__mes>12:
                self.__mes-=12
                self.__año+=1
            return self.__hora
        else:
            return -1
    def __sub__(self,hora):
        if(hora>-1 and hora<24):     
            self.__hora-=hora  
            if ((self.__año%400==0)or (self.__año%100!=0 and self.__año%4==0)):
                listameses=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                listameses=[31,28,31,30,31,30,31,31,30,31,30,31]
            if(self.__hora<0):
                self.__hora+=24
                self.__dia-=1
            if self.__dia==0:
                if(self.__mes)==1:
                    self.__dia=listameses[11]
                    self.__mes=12
                    self.__año-=1
                else:
                    self.__mes-=1
                    self.__dia=listameses[self.__mes-1]
            return(self.__hora)
        else:
         return -1 
    def __gt__(self,hora):
        return self.__hora>hora
    def Test(self):
        print("test funciones")
        print("Suma de 5 hs a la actual, resultado:",self.__add__(5))
        self.Mostrar()
        print("Resta de 5hs a la hora actual, resultado:",self.__sub__(5))
        self.Mostrar()
        print("Suma de 20 hs a la actual, resultado:",self.__add__(20))
        self.Mostrar()
        print("Resta de 20hs a la hora actual, resultado:",self.__sub__(20))
        self.Mostrar()