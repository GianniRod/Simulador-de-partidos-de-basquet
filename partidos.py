import random
import tkinter as tk

class BasketballGame:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Juego de Baloncesto")

        self.lbl_titulo = tk.Label(master, text="Simulador de Juego de Baloncesto")
        self.lbl_titulo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)


        self.lbl_equipo2 = tk.Label(master, text="Equipo Visitante:")
        self.lbl_equipo2.grid(row=2, column=0, padx=5, pady=5)
        self.entry_equipo2 = tk.Entry(master)
        self.entry_equipo2.grid(row=2, column=1, padx=5, pady=5)

        self.lbl_probpos = tk.Label(master, text="Posibilidad de posesion:")
        self.lbl_probpos.grid(row=3, column=0, padx=5, pady=5)
        self.entry_probpos = tk.Entry(master)
        self.entry_probpos.grid(row=3, column=1, padx=5, pady=5)

        self.btn_simular = tk.Button(master, text="Simular juego", command=self.simular_juego)
        self.btn_simular.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def simular_juego(self):
        equipo1 = self.entry_equipo1.get()
        equipo2 = self.entry_equipo2.get()
        probpos = float(self.entry_probpos.get())

        probabilidades_equipo1 = {
            '2 puntos': 0.41,
            '3 puntos': 0.34,
            'perdida': 0.12,
            '1 punto falta': 0.10
        }
        probabilidades_equipo2 = {
            '2 puntos': 0.39,
            '3 puntos': 0.36,
            'perdida': 0.16,
            '1 punto falta': 0.15
        }

        puntuacion_equipo1 = 0
        puntuacion_equipo2 = 0

        for i in range(26*4):
            if random.random() < probpos:
                equipo = equipo1
                probabilidades = probabilidades_equipo1
            else:
                equipo = equipo2
                probabilidades = probabilidades_equipo2

            tipo_lanzamiento = random.choices(['2 puntos', '3 puntos', 'perdida', '1 punto falta'], 
                                               [probabilidades['2 puntos'], probabilidades['3 puntos'], probabilidades['perdida'], probabilidades['1 punto falta']])[0]

            if tipo_lanzamiento == '2 puntos':
                puntos = 2
            elif tipo_lanzamiento == '3 puntos':
                puntos = 3
            elif tipo_lanzamiento == 'perdida':
                puntos = 0
            elif tipo_lanzamiento == '1 punto falta':
                puntos = 1

            if equipo == equipo1:
                puntuacion_equipo1 += puntos
            else:
                puntuacion_equipo2 += puntos

        resultado = tk.Label(self.master, text=f"{equipo1}: {puntuacion_equipo1}  {equipo2}: {puntuacion_equipo2}")
        resultado.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    root.iconbitmap('C:/Users/giann/OneDrive/Documentos/Ataques LPBB/LPBB2.ico')
    game = BasketballGame(root)
    root.mainloop()
