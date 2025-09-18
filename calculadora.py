import tkinter as tk

lista = []
lista_simbolos = ['🆑', "+", "-", "x", "/", "="]
lista_calculadora = []
contador_simbolos = 0
string = ""
contador = 1


def ingresar_numeros(c):
    global string
    lista_calculadora.append(c)
    if lista_calculadora[0] != "-":
        if lista_calculadora[(len(lista_calculadora) - 1)] in lista_simbolos and lista_calculadora[(len(lista_calculadora) - 2)] in lista_simbolos:
            del lista_calculadora[(len(lista_calculadora) - 2)]
        
    contenido = "".join(lista_calculadora)
    variable.set(contenido)
    string = contenido
    
def eliminar(cadena):
    global string
    nueva_cadena = cadena[:(len(cadena) - 1)]
    string = nueva_cadena
    del lista_calculadora[(len(lista_calculadora)) - 1]
    variable.set(nueva_cadena)
    
def realizar_operacion(contenido):
    global lista_calculadora
    global string
    var1 = ""
    var2 = ""
    simbolo_guardar = ""
    punto_de_partida = 0
    for i in range(len(contenido)):
        if i == 0 and contenido[i] == "-":
            var1 = var1 + contenido[i]
            continue
        if contenido[i] in lista_simbolos:
            punto_de_partida = i + 1
            simbolo_guardar = contenido[i]
            break
        var1 = var1 + contenido[i]
        
    
    if punto_de_partida == 0 or simbolo_guardar == contenido[(len(contenido) - 1)]:
        return ""
        
    for i in range(punto_de_partida, len(contenido)):
        
        if contenido[i] not in lista_simbolos:
           var2 = var2 + contenido[i]
           
        if i == (len(contenido) - 1) or contenido[i] in lista_simbolos:
            if simbolo_guardar == "+":
                var1 = int(var1) + int(var2)
                var2 = ""
                
            elif simbolo_guardar == "-":
                var1 = int(var1) - int(var2)
                var2 = ""
                
            elif simbolo_guardar == "x":
                var1 = int(var1) * int(var2)
                var2 = ""
            
            elif simbolo_guardar == "/":
                var1 = float(var1) / float(var2)
                var2 = ""
                
            simbolo_guardar = contenido[i]
    
    variable.set(str(var1))
    lista_calculadora = [str(var1)]
    string = ""
    
    
    
def comprobacion(simbolo):
    if simbolo != '🆑' and simbolo != "=":
        if lista_calculadora != [] or simbolo == '-':
            ingresar_numeros(simbolo)
        
    if lista_calculadora != [] :
        if simbolo == "=":
            realizar_operacion(string)
        elif simbolo == "🆑":
            eliminar(string)

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
        activeforeground = "white", command = lambda x = str(contador): ingresar_numeros(x)).pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 20, pady = 11)
        contador += 1
        
    for index in range(2):
        tk.Button(i, text = f"{lista_simbolos[contador_simbolos]}", bg = "#736E6E", relief = tk.FLAT, fg="white", font = ("arial", 40, "bold"), activebackground = "#423838", 
        activeforeground = "white", command = lambda x = lista_simbolos[contador_simbolos]: comprobacion(x)).pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 20, pady = 11)
        contador_simbolos += 1
        
boton = tk.Button(app, text = f"0", bg = "#736E6E", fg="white", relief = tk.FLAT, font = ("arial", 30, "bold"), activebackground = "#423838", 
        activeforeground = "white", height = 1, width = 3, command = lambda x = str(0): ingresar_numeros(x))
boton.pack(side = tk.LEFT, fill = tk.Y, expand = True, padx = 20, pady = 11)

app.mainloop()
