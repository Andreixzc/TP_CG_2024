def CohenSutherland(x0, y0, x1, y1, canvas):
    # Define os limites da janela de recorte
    xmin, ymin, xmax, ymax = 50, 50, 300, 350  

    def compute_outcode(x, y):
        # Calcula o código de região para um ponto (x, y)
        # O código é um número de 4 bits, onde cada bit representa uma região
        code = 0
        if x < xmin:      # a esquerda da janela
            code |= 1
        elif x > xmax:    # a direita da janela
            code |= 2
        if y < ymin:      # abaixo da janela
            code |= 4
        elif y > ymax:    # acima da janela
            code |= 8
        return code

    # Calcula os códigos de região para os pontos iniciais e finais da linha
    outcode0 = compute_outcode(x0, y0)
    outcode1 = compute_outcode(x1, y1)
    accept = False

    while True:
        if not (outcode0 | outcode1):  # Ambos os pontos estão dentro da janela
            accept = True
            break
        elif outcode0 & outcode1:  # Ambos os pontos estão na mesma região fora da janela
            break
        else:
            # A linha precisa ser recortada
            # Escolhe um ponto que está fora da janela
            outcode_out = outcode0 if outcode0 else outcode1

            # Encontra o ponto de interseção com a borda da janela
            if outcode_out & 8:  # ponto está acima da janela
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif outcode_out & 4:  # ponto está abaixo da janela
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif outcode_out & 2:  # ponto está à direita da janela
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif outcode_out & 1:  # ponto está à esquerda da janela
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            # Substitui o ponto fora da janela pelo ponto de interseção
            if outcode_out == outcode0:
                x0, y0 = x, y
                outcode0 = compute_outcode(x0, y0)
            else:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1)

    if accept:
        # Se a linha foi aceita, desenha no canvas
        return canvas.create_line(x0, y0, x1, y1, fill='blue', tags="drawable")
    return None  # Se a linha foi completamente rejeitada, retorna None

def LiangBarsky(x0, y0, x1, y1, canvas):
    # Define os limites da janela de recorte
    xmin, ymin, xmax, ymax = 310, 50, 550, 350 

    # Calcula o vetor da linha
    dx = x1 - x0
    dy = y1 - y0

    # Define o array p (normal às bordas da janela)
    p = [-dx, dx, -dy, dy]
    # Define o array q (distância do ponto inicial à borda da janela)
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]

    # Inicializa os parâmetros da linha
    u1 = 0  # Ponto inicial da parte visível da linha
    u2 = 1  # Ponto final da parte visível da linha

    for i in range(4):
        if p[i] == 0:
            # A linha é paralela à borda
            if q[i] < 0:
                # A linha está completamente fora da janela
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                # A linha está entrando na janela
                if t > u2:
                    return None
                elif t > u1:
                    u1 = t
            elif p[i] > 0:
                # A linha está saindo da janela
                if t < u1:
                    return None
                elif t < u2:
                    u2 = t

    # Verifica se a linha está completamente fora da janela
    if u1 > u2:
        return None

    # Calcula as coordenadas da linha recortada
    x0_new = x0 + u1 * dx
    y0_new = y0 + u1 * dy
    x1_new = x0 + u2 * dx
    y1_new = y0 + u2 * dy

    # Desenha a linha recortada no canvas
    return canvas.create_line(x0_new, y0_new, x1_new, y1_new, fill='red', tags="drawable")