import math

def scale_object(item, factor, canvas):
    """
    Escala um objeto no canvas por um fator dado.
    
    :param item: O item do canvas a ser escalado
    :param factor: O fator de escala (> 1 para aumentar, < 1 para diminuir)
    :param canvas: O objeto canvas do Tkinter
    """
    # Obtém as coordenadas atuais do objeto
    coords = canvas.coords(item)
    
    # Calcula o centro do objeto
    cx = sum(coords[::2]) / len(coords[::2])  # Média das coordenadas x
    cy = sum(coords[1::2]) / len(coords[1::2])  # Média das coordenadas y
    
    new_coords = []
    # Aplica a escala a cada ponto do objeto
    for i in range(0, len(coords), 2):
        # Calcula as novas coordenadas aplicando o fator de escala
        new_x = cx + (coords[i] - cx) * factor
        new_y = cy + (coords[i+1] - cy) * factor
        new_coords.extend([new_x, new_y])
    
    # Atualiza as coordenadas do objeto no canvas
    canvas.coords(item, *new_coords)

def reflect_object(item, reflection_type, scale_factor, canvas):
    """
    Reflete um objeto no canvas.
    
    :param item: O item do canvas a ser refletido
    :param reflection_type: Tipo de reflexão ('X', 'Y', ou 'XY')
    :param scale_factor: Fator de escala adicional após a reflexão
    :param canvas: O objeto canvas do Tkinter
    """
    # Obtém as coordenadas atuais do objeto
    coords = canvas.coords(item)
    
    # Calcula o centro do objeto
    cx = sum(coords[::2]) / len(coords[::2])  # Média das coordenadas x
    cy = sum(coords[1::2]) / len(coords[1::2])  # Média das coordenadas y
    
    new_coords = []
    # Aplica a reflexão a cada ponto do objeto
    for i in range(0, len(coords), 2):
        x, y = coords[i], coords[i+1]
        if reflection_type in ['Y', 'XY']:
            # Reflexão em relação ao eixo Y
            x = cx + (cx - x) * scale_factor
        if reflection_type in ['X', 'XY']:
            # Reflexão em relação ao eixo X
            y = cy + (cy - y) * scale_factor
        new_coords.extend([x, y])
    
    # Atualiza as coordenadas do objeto no canvas
    canvas.coords(item, *new_coords)

def rotate_object(item, angle, canvas):
    """
    Rotaciona um objeto no canvas.
    
    :param item: O item do canvas a ser rotacionado
    :param angle: Ângulo de rotação em graus
    :param canvas: O objeto canvas do Tkinter
    """
    # Converte o ângulo para radianos
    angle = math.radians(angle)
    # Obtém as coordenadas atuais do objeto
    coords = canvas.coords(item)
    
    # Calcula o centro do objeto
    cx = sum(coords[::2]) / len(coords[::2])  # Média das coordenadas x
    cy = sum(coords[1::2]) / len(coords[1::2])  # Média das coordenadas y
    
    new_coords = []
    # Aplica a rotação a cada ponto do objeto
    for i in range(0, len(coords), 2):
        # Translada o ponto para a origem
        x, y = coords[i] - cx, coords[i+1] - cy
        # Aplica a rotação
        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = x * math.sin(angle) + y * math.cos(angle)
        # Translada o ponto de volta e adiciona à lista de novas coordenadas
        new_coords.extend([new_x + cx, new_y + cy])
    
    # Atualiza as coordenadas do objeto no canvas
    canvas.coords(item, *new_coords)