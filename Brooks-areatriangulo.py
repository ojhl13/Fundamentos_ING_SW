from math import sqrt

def Calc_equilatero(lado):
	area = (0.8660)*(lado)*(lado)
	print("El area del triangulo equilatero con un lado "+str(lado)+"es: "+str(area))
def Calc_isoseles(altura , base):
	area= (base*(sqrt((altura*altura)*((base*base)/(4)))))/(2)
	print("El area del triangulo isoseles con una altura "+str(altura)+"y una base de:"+str(base)+"es: "+str(area))
def Calc_rectangulo(base,altura):
	area=(base*altura)/2
	print("El area del triangulo isoseles con una altura "+str(altura)+"y una base de:"+str(base)+"es: "+str(area))



def main():
   print "Link Start\n"
   print "Calculo de areas de tirnagulos\n"
   print "Indicar cual tipo de triangulo es:\n 1)Equilatero\n 2) Isosceles\n 3)Rectangulo\n 0) Salir "
   tipo = input("Seleccionar una opcion:")
   while(0 != int(tipo)):

   	
   	if( 1 == tipo):
   		
   		dato = float(input("Favor de escribir el valor del lado: "))
   		Calc_equilatero(dato)
   		tipo=0
	if( 2 == tipo):
   		dato = float(input("Favor de escribir el valor del altura: "))
   		dato2 = float(input("Favor de escribir el valor de la base: "))
   		Calc_isoseles(dato,dato2)
   		tipo=0
   	if( 3 == tipo):
   		dato = float(input("Favor de escribir el valor de la base: "))
   		dato2 = float(input("Favor de escribir el valor de la altura: "))
   		Calc_rectangulo(dato,dato2)
   		tipo=0
   	



if  __name__ =='__main__':main()