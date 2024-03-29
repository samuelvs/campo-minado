#    Estruturas de dados em Python
#    Samuel V. de Amorim, 2019
#    Jogo Campo Minado
#    Python version 3.7

from random import randint
from fila_array import *
import os

game_over = False
tab = [[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]
size_x = 9
size_y = 9
total_bombs = 10

def get_vsl(x, y):
  return tab[x-1][y-1]
def get_vsr(x, y):
  return tab[x-1][y+1]
def get_vil(x, y):
  return tab[x+1][y-1]
def get_vir(x, y):
  return tab[x+1][y+1]
def get_left(x, y):
  return tab[x][y-1]
def get_right(x, y):
  return tab[x][y+1]
def get_up(x, y):
  return tab[x-1][y]    
def get_down(x, y):
  return tab[x+1][y]

def show_tab():
  for i in tab:
    for j in i:
      print(j, end=' ')
    print()
  print()

def show_tab_player():
  for i in tab:
    for j in i:
      if j == 'L':
        print('0', end=' ')
      elif j == 'B':
        print('*', end=' ')
      elif j == '*':
        print('#', end=' ')
      elif j < 0:
        print(j*-1, end=' ')
      else:
        print('#', end=' ')
    print()
  print()

def add_bombs(n):
  for i in range(n):
    repeted = True
    while repeted:
      x = randint(0,size_x)
      y = randint(0,size_y)
      if tab[x][y] != '*':
        tab[x][y] = '*'
        repeted = False

def add_bomb_counts():
  for x in range(size_x+1):
    for y in range(size_y+1):
      b = 0
      if x == 0 and tab[x][y] != '*': #limite cima
        if y == 0:
          if get_right(x,y) == '*':
            b += 1
          if get_down(x,y) == '*':
            b += 1
          if get_vir(x,y) == '*':
            b += 1
        elif y == size_y:
          if get_left(x,y) == '*':
            b += 1
          if get_down(x,y) == '*':
            b += 1
          if get_vil(x,y) == '*':
            b += 1
        else:
          if get_left(x,y) == '*':
            b += 1
          if get_vil(x,y) == '*':
            b += 1
          if get_down(x,y) == '*':
            b += 1
          if get_vir(x,y) == '*':
            b += 1
          if get_right(x,y) == '*':
            b += 1
        tab[x][y] = b
      elif x == size_x and tab[x][y] != '*': #limite baixo
        if y == 0:
          if get_up(x,y) == '*':
            b += 1
          if get_vsr(x,y) == '*':
            b += 1
          if get_right(x,y) == '*':
            b += 1
        elif y == size_y:
          if get_up(x,y) == '*':
            b += 1
          if get_vsl(x,y) == '*':
            b += 1
          if get_left(x,y) == '*':
            b += 1
        else:
          if get_left(x,y) == '*':
            b += 1
          if get_vsl(x,y) == '*':
            b += 1
          if get_up(x,y) == '*':
            b += 1
          if get_vsr(x,y) == '*':
            b += 1
          if get_right(x,y) == '*':
            b += 1
        tab[x][y] = b
      elif x > 0 and x < size_x and y == 0 and tab[x][y] != '*': #limite esq
        if get_up(x,y) == '*':
          b += 1
        if get_vsr(x,y) == '*':
          b += 1
        if get_right(x,y) == '*':
          b += 1
        if get_vir(x,y) == '*':
          b += 1
        if get_down(x,y) == '*':
          b += 1
        tab[x][y] = b
      elif x > 0 and x < size_x and y == size_y and tab[x][y] != '*': #limite dir
        if get_up(x,y) == '*':
          b += 1
        if get_vsl(x,y) == '*':
          b += 1
        if get_left(x,y) == '*':
          b += 1
        if get_vil(x,y) == '*':
          b += 1
        if get_down(x,y) == '*':
          b += 1
        tab[x][y] = b
      elif tab[x][y] != '*':
        if get_vsl(x,y) == '*':
          b += 1
        if get_up(x,y) == '*':
          b += 1
        if get_vsr(x,y) == '*':
          b += 1
        if get_right(x,y) == '*':
          b += 1
        if get_vir(x,y) == '*':
          b += 1
        if get_down(x,y) == '*':
          b += 1
        if get_vil(x,y) == '*':
          b += 1
        if get_left(x,y) == '*':
          b += 1
        tab[x][y] = b

def choose(l,c):
  out = False
  f = FilaArray()
  f.enqueue([l,c])
  status = False
  while not f.is_empty() and not status:
    n = f.dequeue()
    x = n[0]
    y = n[1]

    if tab[x][y] != '*' and tab[x][y] != 'L' and tab[x][y] != 'B':
      if tab[x][y] < 0:
        continue
    if tab[x][y] == 'L' or tab[x][y] == 'B':
      continue
    if tab[x][y] == 0:
      tab[x][y] = 'L'
    elif tab[x][y] == '*':
      tab[x][y] = 'B'
      out = True
      game_over = True
      status = True
    elif tab[x][y] > 0:
      tab[x][y] = tab[x][y] * -1
      out = True

    if not out:
      if x == 0: #limite cima
        if y == 0:
          if get_right(x,y) == 0:
            f.enqueue([x,y+1])
          if get_down(x,y) == 0:
            f.enqueue([x+1,y])
          if get_vir(x,y) == 0:
            f.enqueue([x+1,y+1])
        elif y == size_y:
          if get_left(x,y) == 0:
            f.enqueue([x,y-1])
          if get_down(x,y) == 0:
            f.enqueue([x+1,y])
          if get_vil(x+1,y-1) == 0:
            f.enqueue([x,y])
        else:
          if get_left(x,y) == 0:
            f.enqueue([x,y-1])
          if get_vil(x,y) == 0:
            f.enqueue([x+1,y-1])
          if get_down(x,y) == 0:
            f.enqueue([x+1,y])
          if get_vir(x,y) == 0:
            f.enqueue([x+1,y+1])
          if get_right(x,y) == 0:
            f.enqueue([x,y+1])
      elif x == size_x: #limite baixo
        if y == 0:
          if get_up(x,y) == 0:
            f.enqueue([x-1,y])
          if get_vsr(x,y) == 0:
            f.enqueue([x-1,y+1])
          if get_right(x,y) == 0:
            f.enqueue([x,y+1])
        elif y == size_y:
          if get_up(x,y) == 0:
            f.enqueue([x-1,y])
          if get_vsl(x,y) == 0:
            f.enqueue([x+1,y-1])
          if get_left(x,y) == 0:
            f.enqueue([x,y-1])
        else:
          if get_left(x,y) == 0:
            f.enqueue([x,y-1])
          if get_vsl(x,y) == 0:
            f.enqueue([x+1,y-1])
          if get_up(x,y) == 0:
            f.enqueue([x-1,y])
          if get_vsr(x,y) == 0:
            f.enqueue([x-1,y+1])
          if get_right(x,y) == 0:
            f.enqueue([x,y+1])
      elif x > 0 and x < size_x and y == 0: #limite esq
        if get_up(x,y) == 0:
          f.enqueue([x-1,y])
        if get_vsr(x,y) == 0:
          f.enqueue([x-1,y+1])
        if get_right(x,y) == 0:
          f.enqueue([x,y+1])
        if get_vir(x,y) == 0:
          f.enqueue([x+1,y+1])
        if get_down(x,y) == 0:
          f.enqueue([x+1,y])
      elif x > 0 and x < size_x and y == size_y: #limite dir
        if get_up(x,y) == 0:
          f.enqueue([x-1,y])
        if get_vsl(x,y) == 0:
          f.enqueue([x-1,y-1])
        if get_left(x,y) == 0:
          f.enqueue([x,y-1])
        if get_vil(x,y) == 0:
          f.enqueue([x+1,y-1])
        if get_down(x,y) == 0:
          f.enqueue([x+1,y])
      else:
        if get_vsl(x,y) == 0:
          f.enqueue([x-1,y-1])
        if get_up(x,y) == 0:
          f.enqueue([x-1,y])
        if get_vsr(x,y) == 0:
          f.enqueue([x-1,y+1])
        if get_right(x,y) == 0:
          f.enqueue([x,y+1])
        if get_vir(x,y) == 0:
          f.enqueue([x+1,y+1])
        if get_down(x,y) == 0:
          f.enqueue([x+1,y])
        if get_vil(x,y) == 0:
          f.enqueue([x+1,y-1])
        if get_left(x,y) == 0:
          f.enqueue([x,y-1])

def add_around():
  for x in range(size_x+1):
    for y in range(size_y+1):
      alt = False
      #if x >= 0 and x < len(tab) and y >= 0 and y < len(tab[x]):
      if tab[x][y] != 'L' and tab[x][y] != '*' and tab[x][y] != 'B':
        if tab[x][y] > 0:
          if x == 0: #limite cima
            if y == 0:
              if get_right(x,y) == 'L' or get_down(x,y) == 'L' or get_vir(x,y) == 'L':
                alt = True
            elif y == size_y:
              if get_left(x,y) == 'L' or get_down(x,y) == 'L' or get_vil(x+1,y-1) == 'L':
                alt = True
            else:
              if get_left(x,y) == 'L' or  get_vil(x,y) == 'L' or get_down(x,y) == 'L' or get_vir(x,y) == 'L' or get_right(x,y) == 'L':
                alt = True
          elif x == size_x: #limite baixo
            if y == 0:
              if get_up(x,y)  == 'L' or  get_vsr(x,y)  == 'L' or  get_right(x,y)  == 'L':
                alt = True
            elif y == size_y:
              if get_up(x,y)  == 'L' or  get_vsl(x,y)  == 'L' or  get_left(x,y)  == 'L':
                alt = True
            else:
              if get_left(x,y)  == 'L' or  get_vsl(x,y)  == 'L' or  get_up(x,y)  == 'L' or  get_vsr(x,y)  == 'L' or  get_right(x,y)  == 'L':
                alt = True
          elif x > 0 and x < size_x and y == 0: #limite esq
            if get_up(x,y)  == 'L' or  get_vsr(x,y)  == 'L' or   get_right(x,y)  == 'L' or   get_vir(x,y)  == 'L' or  get_down(x,y)  == 'L':
              alt = True
          elif x > 0 and x < size_x and y == size_y: #limite dir
            if get_up(x,y)  == 'L' or  get_vsl(x,y)  == 'L' or  get_left(x,y)  == 'L' or  get_vil(x,y)  == 'L' or  get_down(x,y)  == 'L':
              alt = True
          else:
            if get_vsl(x,y)  == 'L' or  get_up(x,y)  == 'L' or  get_vsr(x,y)  == 'L' or   get_right(x,y)  == 'L' or  get_vir(x,y)  == 'L' or  get_down(x,y)  == 'L' or  get_vil(x,y)  == 'L' or  get_left(x,y)  == 'L':
              alt = True
      if alt:
        tab[x][y] = tab[x][y] * -1

def is_game_over():
  over = False
  for i in tab:
    for j in i:
      if j == 'B':
        over = True
        break
      elif j != 'L' and j != '*':
        if j > -1:
          break
  return over

def is_end():
  end = 0
  for i in tab:
    for j in i:
      if j == 0:
        end += 1
      if j != 'L' and j != '*' and j != 'B':
        if j > -1:
          end += 1
  if end > 0:
    return False
  else:
    return True

def test():
  for i in tab:
    for j in i:
      if j == 'B':
        return True

add_bombs(total_bombs)
add_bomb_counts()
#show_tab()
show_tab_player()

while not is_end():
  print('Linha: ')
  x = int(input())
  print('Coluna: ')
  y = int(input())
  choose(x,y)
  os.system('cls' if os.name == 'nt' else 'clear')
  add_around()
  #show_tab()
  show_tab_player()
  if test():
    break

print('Fim de jogo!')
if(is_end()):
  print('Você venceu!')
else:
  print('Você perdeu!')
