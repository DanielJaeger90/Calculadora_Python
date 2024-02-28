import tkinter as tk
import math

# Clase para la creación de la ventana de la calculadora
class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora by Daniel Iturralde")
        self.root.configure(bg="#FCEE0C")  # Color de fondo de la ventana

        # Configuración de pantalla de la calculadora ( Color, tamaño, fuente, etc )
        self.entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14), bg="#01c4e7", fg="#ffffff")
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # mapa de botones ( texto, fila, columna )
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3), ("π", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3), ("√", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3), ("C", 3, 4),
            ("0", 4, 0), ("=", 4, 1), ("/", 4, 2), ("^", 4, 3), ("^2", 4, 4)
        ]

        for boton_texto, fila, columna in botones:
            # Configuración de color de fondo de los botones
            boton = tk.Button(root, text=boton_texto, padx=40, pady=20, bg="#01c4e7", activebackground="#2ef8a0", command=lambda text=boton_texto: self.click_boton(text))
            boton.grid(row=fila, column=columna, padx=5, pady=5)

# Función para realizar las operaciones de la calculadora
    def click_boton(self, texto):
        if texto == "=":
            try:
                resultado = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(resultado))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "No puedo hacer eso BOBO")
        elif texto == "C":
            self.entry.delete(0, tk.END)
        elif texto == "π":
            self.entry.insert(tk.END, math.pi)
        elif texto == "√":
            try:
                numero = float(self.entry.get())
                resultado = math.sqrt(numero)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(resultado))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "No puedo hacer eso BOBO")
        elif texto == "^2":
            try:
                numero = float(self.entry.get())
                resultado = numero ** 2
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(resultado))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "No puedo hacer eso BOBO")
        else:
            self.entry.insert(tk.END, texto)

# Inicialización de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
