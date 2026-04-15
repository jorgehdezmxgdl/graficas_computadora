import tkinter as tk

class Ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Algoritmo de Flood Fill")
        self.ventana.geometry("500x700")
        points = [50, 150, 150, 50, 250, 150]
        self.dibuja_poligono(points)
        points = [40, 100, 90, 160, 140, 110, 190, 170, 240, 120, 190, 70, 140, 90, 90, 40]
        self.dibuja_poligono(points)
        points = [20, 100, 70, 160, 120, 110, 170, 170, 220, 120, 170, 70, 120, 90, 70, 40, 40, 100, 90, 90]
        self.dibuja_poligono(points)
        self.ventana.mainloop()

    def dibuja_poligono(self, vertices):
        self.canvas = tk.Canvas(self.ventana, width=300, height=200, bg="lightgray")
        self.canvas.pack()
        self.canvas.create_polygon(vertices, fill="blue", outline="black")


ventana = Ventana()