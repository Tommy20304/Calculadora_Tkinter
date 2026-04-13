import tkinter as tk

lista = []
contador_simbolos = 0
string = ""
contador = 1


class Calculadora:
    def __init__(self):
        self.lista_calculadora = []
        self.string = ""
        self.lista_simbolos = ['🆑', "+", "-", "x", "/", "="]
    
    #si el ingreso de numeros o simbolos es incorrecto, hace operaciones para corregirlo
    def determinar_errores_de_signos(self):
        
        #se comprueba que el primer numero ingresado no sea un simbolo, a excepcion del simbolo de resta
        if not self.lista_calculadora[0].isdigit() and self.lista_calculadora[0] != "-":
            del self.lista_calculadora[0]
            return ""

        #se comprueba que si se ingresa un simbolo despues de ingresar otro simbolo, se elimine el simbolo anterior y se reemplace por el nuevo
        if len(self.lista_calculadora) > 1:
            
            #si el simbolo de resta es el primer digito ingresado, se quita el simbolo nuevo
            if self.lista_calculadora[-2] == "-" and self.lista_calculadora[-1] in self.lista_simbolos and len(self.lista_calculadora) == 2:
                del self.lista_calculadora[-1]
                return ""
            
            if self.lista_calculadora[-1] in self.lista_simbolos and self.lista_calculadora[-2] in self.lista_simbolos:
                del self.lista_calculadora[-2]
                return ""
        
    def ingresar_numeros(self,c):
        self.lista_calculadora.append(c)
        
        #se comprueba los signos que se ingresaron
        self.determinar_errores_de_signos()
            
        contenido = "".join(self.lista_calculadora)
        variable.set(contenido)
        self.string = contenido
        
    def eliminar(self,cadena):
        nueva_cadena = cadena[:(len(cadena) - 1)] #se elimina el ultimo caracter de la cadena
        self.string = nueva_cadena
        del self.lista_calculadora[(len(self.lista_calculadora)) - 1]
        variable.set(nueva_cadena)
        
    #se realiza la operacion dependiendo del simbolo que se ingrese
    def realizar_operacion(self, contenido):
        num1 = ""
        num2 = ""
        simbolo_guardar = ""
        punto_de_partida = 0
        for i in range(len(contenido)):
            
            #si el signo resta esta al inicio, se junta en el var1
            if i == 0 and contenido[i] == "-":
                num1 = num1 + contenido[i]
                continue
            
            #cuando se rastre un simbolo, se guarda el simbolo y se marca el punto de partida para el var2
            if contenido[i] in self.lista_simbolos:
                punto_de_partida = i + 1
                simbolo_guardar = contenido[i]
                break
            
            num1 = num1 + contenido[i]
            
        
        if punto_de_partida == 0 or simbolo_guardar == contenido[-1]:
            return ""
            
        #se recorre el contenido a partir del punto de partida para juntar el var2
        for i in range(punto_de_partida, len(contenido)):
            
            if contenido[i] not in self.lista_simbolos:
                num2 = num2 + contenido[i]
            
            #si es el ultimo digito o se encontro un simbolo, se hace esto
            if i == (len(contenido) - 1) or contenido[i] in self.lista_simbolos:
                if simbolo_guardar == "+":
                    num1 = int(num1) + int(num2)
                    num2 = ""
                    
                elif simbolo_guardar == "-":
                    num1 = int(num1) - int(num2)
                    num2 = ""
                    
                elif simbolo_guardar == "x":
                    num1 = int(num1) * int(num2)
                    numr2 = ""
                
                elif simbolo_guardar == "/":
                    num1 = float(num1) / float(num2)
                    num2 = ""
                    
                simbolo_guardar = contenido[i]
        
        variable.set(str(num1))
        self.lista_calculadora = [str(num1)]
        self.string = ""
        
        
    #comprueba que los simbolos se ingresen en el momento correcto
    def comprobacion(self, simbolo):
        if simbolo != '🆑' and simbolo != "=":
            if self.lista_calculadora != [] or simbolo == '-':
                self.ingresar_numeros(simbolo)
            
        if self.lista_calculadora != [] :
            if simbolo == "=":
                self.realizar_operacion(self.string)
            elif simbolo == "🆑":
                self.eliminar(self.string)

cal = Calculadora()

#area de configuracion de la ventana y botones
app = tk.Tk()
app.configure(background = "black")
app.title("Calculadora")
variable = tk.StringVar(app)
numero = tk.StringVar(app)

barra = tk.Label(app, text = "", bg = "white", fg = "black", 
                 font = ("arial", 30, "bold"), textvar = variable)

barra.pack(side = tk.TOP, fill = tk.BOTH, expand = True,padx = 0, pady = 1)

frame = tk.Frame(app)
frame.configure(background = "black")
frame.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 22, pady = 11)

for i in range(3):
    frame1 = tk.Frame(frame)
    lista.append(frame1)
    
    lista[i].configure(background = "black")
    lista[i].pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 22, pady = 11)
    
for i in lista:    
    for e in range(3):
        tk.Button(i, text = f"{contador}", bg = "#736E6E", relief = tk.FLAT, fg="white", font = ("arial", 30, "bold"), activebackground = "#423838", 
        activeforeground = "white", command = lambda x = str(contador): cal.ingresar_numeros(x)).pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 20, pady = 11)
        contador += 1
        
    for index in range(2):
        tk.Button(i, text = f"{cal.lista_simbolos[contador_simbolos]}", bg = "#736E6E", relief = tk.FLAT, fg="white", font = ("arial", 40, "bold"), activebackground = "#423838", 
        activeforeground = "white", command = lambda x = cal.lista_simbolos[contador_simbolos]: cal.comprobacion(x)).pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 20, pady = 11)
        contador_simbolos += 1
        
boton = tk.Button(app, text = f"0", bg = "#736E6E", fg="white", relief = tk.FLAT, font = ("arial", 30, "bold"), activebackground = "#423838", 
        activeforeground = "white", height = 1, width = 3, command = lambda x = str(0): cal.ingresar_numeros(x))
boton.pack(side = tk.LEFT, fill = tk.Y, expand = True, padx = 20, pady = 11)

app.mainloop()
