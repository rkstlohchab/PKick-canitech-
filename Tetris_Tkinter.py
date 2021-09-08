from tkinter import *
from copy import deepcopy
from random import randrange, choice
import time

tk = Tk()

W, H = 10, 20
T = 36

sc = Canvas(tk, width=750, height=940, bg="red", highlightthickness=0)
sc.pack()

game_sc = Canvas(tk, width=361, height=721, bg="yellow", highlightthickness=0)
game_sc.place(x=20, y=20, anchor=NW)

img_obj1 = PhotoImage(file="C:/Users/Dell/PycharmProjects/Tetris/img/tetris1.png")
sc.create_image(0, 0, anchor=NW, image=img_obj1)

img_obj2 = PhotoImage(file="C:/Users/DELL/PycharmProjects/Tetris/img/tetris.png")
game_sc.create_image(0, 0, anchor=NW, image=img_obj2)

score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}
record = "0" 

sc.create_text(450, 30,text="TETRIS", font=("WiGuru 2", 50),fill="red", anchor=NW)
sc.create_text(500, 640,text="Score:", font=("WiGuru 2", 35),fill="white", anchor=NW)
_score = sc.create_text(542, 690,text=str(score), font=("WiGuru 2", 35),fill="gold", anchor=NW)
sc.create_text(480, 500,text="Record:", font=("WiGuru 2", 35),fill="white", anchor=NW)
_record = sc.create_text(522, 550,text=record, font=("WiGuru 2", 35),fill="gold", anchor = NW)

grid = [[game_sc.create_rectangle(x * T, y * T, T * (x + 1), T * (y + 1)) for x in range(W)] for y in range(H)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]               

figures = [[[x + W // 2, y + 1, 1, 1] for x, y in fig_pos] for fig_pos in figures_pos]
get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))
field = [[0 for i in range(W)] for j in range(H)]

figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def check_borders():
    if figure[i][0] < 0 or figure[i][0] > W - 1:
        return False
    if figure[i][1] > H- 1 or field[figure[i][1]][figure[i][0]]:
        return False
    return True

def move_obj(event):
    global rotate, anim_limit, dx
    if event.keysym == 'Up':
        rotate = True
    elif event.keysym == 'Down':
        anim_limit = 100
    elif event.keysym == 'Left':
        dx = -1
    elif event.keysym == 'Right':
        dx = 1

game_sc.bind_all("<KeyPress-Up>",move_obj)
game_sc.bind_all("<KeyPress-Down>",move_obj)
game_sc.bind_all("<KeyPress-Left>",move_obj)
game_sc.bind_all("<KeyPress-Right>",move_obj)


flag, dx, rotate = True, 0, False
anim_count, anim_speed, anim_limit = 0, 60, 2000
while flag:
    if flag:
        #move x
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i][0] += dx
            if not check_borders():
                figure = deepcopy(figure_old)

        #move y
        anim_count += anim_speed
        figure_old = deepcopy(figure)
        if anim_count > anim_limit:
            anim_count = 0
            figure_old = deepcopy(figure)
            for i in range(4):
                figure[i][1] += 1
                if not check_borders():
                    for i in range(4):
                        field[figure_old[i][1]][figure_old[i][0]] = color
                    figure, color = next_figure, next_color
                    next_figure, next_color = deepcopy(choice(figures)), get_color()
                    anim_limit = 2000
                    break


        # rotate
        axis = figure[0]
        figure_old = deepcopy(figure)
        if rotate:
            for i in range(4):
                x = figure[i][1] - axis[1]
                y = figure[i][0] - axis[0]
                figure[i][0] = axis[0] - x
                figure[i][1] = axis[1] + y
                if not check_borders():
                    figure = deepcopy(figure_old)

        fig = []
        # draw figure
        for i in range(4):
            x = figure[i][0] * T
            y = figure[i][1] * T
            fig.append(game_sc.create_rectangle(x, y, x + T, y + T, fill = rgb_to_hex(color)))

        # draw field
        for j, row in enumerate(field):
            for i, col in enumerate(row):
                if col:
                    x, y = i * T, j * T
                    fig.append(game_sc.create_rectangle(x, y, x + T, y + T, fill = rgb_to_hex(col)))

        # draw next figure
        fig2 = []
        for i in range(4):
            x = next_figure[i][0] * T + 380
            y = next_figure[i][1] * T + 185
            fig2.append(sc.create_rectangle(x, y, x + T, y + T, fill = rgb_to_hex(next_color)))

        dx, rotate = 0, False
        tk.update_idletasks()
        tk.update()
        for i in fig:
            game_sc.delete(i)
        for i in fig2:
            sc.delete(i)
        
    time.sleep(0.005)
        



tk.mainloop()