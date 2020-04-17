from tkinter import *
import numpy as np
from tkinter import font
from utils import load_data

x,xlabels,y,ylabels=load_data("SmoothSubspace")
x=np.around(x[0],4)
y=np.around(y[0],4)

gui = Tk()
gui.title("DTW")
# gui.geometry("500x500")

my_font = font.Font(size=20)

labels = []


def dtw(x, y, gui):
    n, m = x.shape[0], y.shape[0]
    dtw_matrix = np.zeros(shape=(n+1, m+1), dtype=np.float64)
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0

    l_zero = Label(gui, text="0", bd=10, relief="ridge")
    l_zero['font'] = my_font
    l_zero.grid(row=1, column=1)

    for i in range(1, m+1):
        l = Label(gui, text="inf", bd=10, relief="ridge")
        l['font'] = my_font
        l.grid(row=1, column=i+1)

    for j in range(1, n+1):
        l = Label(gui, text="inf", bd=10, relief="ridge")
        l['font'] = my_font
        l.grid(row=j+1, column=1)

    tail_path_index_i, tail_path_index_j = 0, 0

    for i in range(1, n+1):
        labels.append([])
        for j in range(1, m+1):
            cost = abs(x[i-1]-y[j-1])

            min_from_before = min(
                dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1])

            dtw_matrix[i, j] = round(cost + min_from_before,3)

            labels[i-1].append(Label(gui, text=str(dtw_matrix[i, j]),
                                     bd=10, relief="ridge"))
            labels[i-1][j-1]['font'] = my_font
            labels[i-1][j-1].grid(row=i+1, column=j+1)

    i, j = n, m
    while True:
        min_from_before = min(
            dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1])
        if min_from_before == dtw_matrix[i-1, j]:
            labels[i-1][j-1]['bg'] = "yellow"
            i = i-1
        elif min_from_before == dtw_matrix[i, j-1]:
            labels[i-1][j-1]['bg'] = "yellow"
            j = j-1
        elif min_from_before == dtw_matrix[i-1, j-1]:
            labels[i-1][j-1]['bg'] = "yellow"
            i, j = i-1, j-1
        if i == 0 and j == 0:
            l_zero['bg'] = "yellow"
            break
    return dtw_matrix


L = Label(gui, text="    ", bd=10, relief="ridge")
L['font'] = my_font
L.grid(row=0, column=0)

for i in range(x.shape[0]):
    L = Label(gui, text=str(x[i]), bd=10, relief="ridge")
    L['font'] = my_font
    L.grid(row=0, column=i+1)

for i in range(y.shape[0]):
    L = Label(gui, text=str(y[i]), bd=10, relief="ridge")
    L['font'] = my_font
    L.grid(row=i+1, column=0)

a=dtw(y, x, gui)

gui.mainloop()
