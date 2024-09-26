import math

def DDA(x0, y0, x1, y1, canvas):
    """
    Implementa o algoritmo DDA (Digital Differential Analyzer) para desenhar uma linha.
    Este algoritmo calcula os pontos da linha usando incrementos constantes em x e y.
    """
    # Arredonda as coordenadas iniciais e finais
    x0, y0, x1, y1 = round(x0), round(y0), round(x1), round(y1)
    
    # Calcula a distância em x e y
    dx = x1 - x0
    dy = y1 - y0
    
    # Determina o número de passos baseado na maior distância
    steps = max(abs(dx), abs(dy))

    # Calcula o incremento em x e y para cada passo
    x_increment = dx / steps
    y_increment = dy / steps

    # Inicializa as coordenadas
    x, y = x0, y0
    points = []
    
    # Gera os pontos da linha
    for _ in range(steps):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    # Cria e retorna a linha no canvas
    return canvas.create_line(points, tags="drawable")

def Bresenham(x0, y0, x1, y1, canvas):
    """
    Implementa o algoritmo de Bresenham para desenhar uma linha.
    Este algoritmo usa apenas operações inteiras, tornando-o eficiente.
    """
    # Arredonda as coordenadas iniciais e finais
    x0, y0, x1, y1 = round(x0), round(y0), round(x1), round(y1)
    
    # Calcula as diferenças absolutas
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    # Determina a direção do incremento
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    
    # Inicializa o erro
    err = dx - dy

    points = []
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        
        # Calcula o próximo ponto
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    # Cria e retorna a linha no canvas
    return canvas.create_line(points, tags="drawable")

def BresenhamCircle(x0, y0, radius, canvas):
    """
    Implementa o algoritmo de Bresenham para desenhar um círculo.
    Este algoritmo desenha o círculo dividindo-o em oito octantes simétricos.
    """
    def draw_circle_points(xc, yc, x, y, points):
        # Adiciona os pontos simétricos nos oito octantes
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y), 
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x), 
            (xc + y, yc - x), (xc - y, yc - x)
        ])

    x = 0
    y = radius
    d = 3 - 2 * radius  # Valor inicial do parâmetro de decisão
    points = []

    while y >= x:
        # Desenha os pontos em todos os octantes
        draw_circle_points(x0, y0, x, y, points)
        x += 1
        
        # Atualiza o parâmetro de decisão e y
        if d > 0:
            y -= 1
            d += 4 * (x - y) + 10
        else:
            d += 4 * x + 6

    # Cria e retorna o círculo no canvas como um polígono sem preenchimento
    return canvas.create_polygon(points, outline='black', fill='', tags="drawable")