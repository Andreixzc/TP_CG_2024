import tkinter as tk
from tkinter import ttk

def create_side_menu(root, app):
    side_menu = tk.Frame(root, width=200, bg='lightgray', relief='sunken')
    side_menu.pack(expand=False, fill='y', side='left', anchor='nw')

    buttons = [
        ("Desenhar Linha (DDA)", lambda: app.select_algorithm('DDA')),
        ("Desenhar Linha (Bresenham)", lambda: app.select_algorithm('Bresenham')),
        ("Cohen-Sutherland", lambda: app.select_algorithm('Cohen-Sutherland')),
        ("Liang-Barsky", lambda: app.select_algorithm('Liang-Barsky')),
        ("Desenhar Circunferência (Bresenham)", lambda: app.select_algorithm('Bresenham Circle')),
        ("Rotacionar Objetos", app.start_rotate),
        ("Mover Objetos", app.enable_drag),
        ("Escalar Objetos", app.start_scale),
        ("Refletir Objetos", app.start_reflect)
    ]

    #Loopando pelo array de botão e criando cada um.
    for text, command in buttons:
        btn = ttk.Button(side_menu, text=text, command=command)
        btn.pack(pady=10, padx=20, fill='x')

    return side_menu

def create_canvas(root):
    canvas = tk.Canvas(root, bg='white', width=600, height=400)
    canvas.pack(fill='both', expand=True)

    # Desenhando as janelas de clipping
    canvas.create_rectangle(50, 50, 300, 350, outline='blue', dash=(4, 2))  
    canvas.create_rectangle(310, 50, 550, 350, outline='red', dash=(4, 2))  

    return canvas