class Libro():
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def MostrarBook(self):
        print(f"El titulo del libro es: {self.titulo}")
        print(f"Hecho por el autor: {self.autor}")
        print(f"y cuenta con {self.paginas} paginas en total")
        print("-" * 30)
    

libro_uno = Libro("Mundo wiguetta","Vegetta777 y Willyrex",189)
libro_dos = Libro("Salchichon","salchicha",19)
libro_tres = Libro("Recetas","chef sexo",133)


print()
libro_uno.MostrarBook()
print()
libro_dos.MostrarBook()
print()
libro_tres.MostrarBook()  

