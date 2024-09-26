# Aplicativo de Desenho e Manipulação de Formas

Este aplicativo é uma ferramenta interativa para desenho e manipulação de formas geométricas, implementando diversos algoritmos clássicos de computação gráfica.

## Funcionalidades

1. **Desenho de Linhas**
   - Algoritmo DDA (Digital Differential Analyzer)
   - Algoritmo de Bresenham

2. **Desenho de Círculos**
   - Algoritmo de Bresenham para círculos

3. **Recorte de Linhas**
   - Algoritmo de Cohen-Sutherland
   - Algoritmo de Liang-Barsky

4. **Manipulação de Formas**
   - Escala
   - Reflexão (em X, Y, ou ambos)
   - Rotação

## Como Usar

1. **Iniciar o Aplicativo**
   - Basta executar o arquivo TP_CG.exe

2. **Desenhar Formas**
   - Selecione o algoritmo de desenho desejado no menu lateral.
   - Clique e arraste no canvas para desenhar a forma.

3. **Recortar Linhas**
   - Selecione um dos algoritmos de recorte.
   - Desenhe linhas no canvas - elas serão automaticamente recortadas conforme as janelas de recorte predefinidas.

4. **Manipular Formas**
   - Use os botões de manipulação no menu lateral para selecionar a operação desejada.
   - Clique em uma forma no canvas para aplicar a transformação.


## Estrutura do Projeto

- `main.py`: Ponto de entrada do aplicativo e interface gráfica principal.
- `drawing_algorithms.py`: Implementações dos algoritmos de desenho (DDA, Bresenham).
- `clipping_algorithms.py`: Implementações dos algoritmos de recorte de linha.
- `shape_manipulation.py`: Funções para manipulação de formas (escala, reflexão, rotação).
- `ui_components.py`: Componentes da interface do usuário.

