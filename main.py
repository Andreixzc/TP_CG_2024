import tkinter as tk
from tkinter import simpledialog, ttk
import math
from drawing_algorithms import DDA, Bresenham, BresenhamCircle
from clipping_algorithms import CohenSutherland, LiangBarsky
from shape_manipulation import scale_object, reflect_object, rotate_object
from ui_components import create_side_menu, create_canvas

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing and Shape Manipulation App")
        
        self.drawn_objects = []
        self.selected_item = None
        self.start_x = 0
        self.start_y = 0
        self.mode = None
        self.algorithm = None
        self.preview_shape = None

        self.side_menu = create_side_menu(self.root, self)
        self.canvas = create_canvas(self.root)
        
        self.bind_events()

    def bind_events(self):
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.extend_shape)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)
        self.canvas.bind("<Button-3>", self.start_drag)
        self.canvas.bind("<B3-Motion>", self.drag)
        self.canvas.bind("<ButtonRelease-3>", self.stop_drag)

    def select_algorithm(self, algo):
        self.mode = 'draw'
        self.algorithm = algo

    def start_draw(self, event):
        if self.mode != 'draw':
            return
        self.start_x, self.start_y = event.x, event.y
        self.preview_shape = None

    def extend_shape(self, event):
        if self.mode != 'draw':
            return
        if self.preview_shape:
            self.canvas.delete(self.preview_shape)

        if self.algorithm in ['DDA', 'Bresenham', 'Cohen-Sutherland', 'Liang-Barsky']:
            self.preview_shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, dash=(4, 2), fill="gray")
        elif self.algorithm == 'Bresenham Circle':
            radius = int(((event.x - self.start_x) ** 2 + (event.y - self.start_y) ** 2) ** 0.5)
            self.preview_shape = self.canvas.create_oval(self.start_x - radius, self.start_y - radius,
                                                         self.start_x + radius, self.start_y + radius,
                                                         dash=(4, 2), outline="gray")

    def end_draw(self, event):
        if self.mode != 'draw':
            return
        end_x, end_y = event.x, event.y

        if self.preview_shape:
            self.canvas.delete(self.preview_shape)
            self.preview_shape = None

        new_object = None
        if self.algorithm == 'DDA':
            new_object = DDA(self.start_x, self.start_y, end_x, end_y, self.canvas)
        elif self.algorithm == 'Bresenham':
            new_object = Bresenham(self.start_x, self.start_y, end_x, end_y, self.canvas)
        elif self.algorithm == 'Cohen-Sutherland':
            new_object = CohenSutherland(self.start_x, self.start_y, end_x, end_y, self.canvas)
        elif self.algorithm == 'Liang-Barsky':
            new_object = LiangBarsky(self.start_x, self.start_y, end_x, end_y, self.canvas)
        elif self.algorithm == 'Bresenham Circle':
            radius = int(((end_x - self.start_x) ** 2 + (end_y - self.start_y) ** 2) ** 0.5)
            new_object = BresenhamCircle(self.start_x, self.start_y, radius, self.canvas)
        
        if new_object:
            self.drawn_objects.append(new_object)

    def start_drag(self, event):
        if self.mode != 'drag':
            return
        self.start_x, self.start_y = event.x, event.y
        self.selected_item = self.canvas.find_withtag("current")
        if self.selected_item:
            self.canvas.itemconfig(self.selected_item, width=2, fill="red")

    def drag(self, event):
        if self.selected_item:
            dx = event.x - self.start_x
            dy = event.y - self.start_y
            self.canvas.move(self.selected_item, dx, dy)
            self.start_x, self.start_y = event.x, event.y

    def stop_drag(self, event):
        if self.selected_item:
            self.canvas.itemconfig(self.selected_item, width=1, fill="black")
        self.selected_item = None

    def enable_drag(self):
        self.mode = 'drag'

    def start_scale(self):
        self.mode = 'scale'
        self.canvas.bind("<Button-1>", self.select_for_scale)

    def select_for_scale(self, event):
        self.selected_item = self.canvas.find_closest(event.x, event.y)
        if self.selected_item:
            self.canvas.itemconfig(self.selected_item, width=2, fill="blue")
            scale_factor = simpledialog.askfloat("Scale", "Enter scale factor:")
            if scale_factor is not None:  
                scale_object(self.selected_item[0], scale_factor, self.canvas)
            self.canvas.itemconfig(self.selected_item, width=1, fill="black")
            self.canvas.unbind("<Button-1>")
            self.mode = None

    def start_reflect(self):
        self.mode = 'reflect'
        self.canvas.bind("<Button-1>", self.select_for_reflect)

    def select_for_reflect(self, event):
        self.selected_item = self.canvas.find_closest(event.x, event.y)
        if self.selected_item:
            self.canvas.itemconfig(self.selected_item, width=2, fill="green")
            reflect_dialog = tk.Toplevel(self.root)
            reflect_dialog.title("Reflect Object")
            
            reflection_type = tk.StringVar(value="X")
            ttk.Radiobutton(reflect_dialog, text="X Reflection", variable=reflection_type, value="X").pack()
            ttk.Radiobutton(reflect_dialog, text="Y Reflection", variable=reflection_type, value="Y").pack()
            ttk.Radiobutton(reflect_dialog, text="XY Reflection", variable=reflection_type, value="XY").pack()
            
            scale_factor = tk.DoubleVar(value=1.0)
            ttk.Label(reflect_dialog, text="Scale Factor:").pack()
            ttk.Entry(reflect_dialog, textvariable=scale_factor).pack()
            
            def apply_reflection():
                reflect_object(self.selected_item[0], reflection_type.get(), scale_factor.get(), self.canvas)
                self.canvas.itemconfig(self.selected_item, width=1, fill="black")
                reflect_dialog.destroy()
                self.canvas.unbind("<Button-1>")
                self.mode = None
            
            ttk.Button(reflect_dialog, text="Apply", command=apply_reflection).pack()

    def start_rotate(self):
        self.mode = 'rotate'
        self.canvas.bind("<Button-1>", self.select_for_rotate)

    def select_for_rotate(self, event):
        self.selected_item = self.canvas.find_closest(event.x, event.y)
        if self.selected_item:
            self.canvas.itemconfig(self.selected_item, width=2, fill="purple")
            angle = simpledialog.askfloat("Rotate", "Enter rotation angle in degrees:")
            if angle is not None:
                rotate_object(self.selected_item[0], angle, self.canvas)
            self.canvas.itemconfig(self.selected_item, width=1, fill="black")
            self.canvas.unbind("<Button-1>")
            self.mode = None

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()