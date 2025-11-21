# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:40:42 2024

@author: lcaus
"""

import os
import time

# Variables iniciales
width, height = 40, 20  # Tamaño del campo de juego
ball_pos = [width // 2, height // 2]  # Posición inicial de la bola
ball_dir = [1, 1]  # Dirección inicial de la bola (1 derecha y 1 abajo)
paddle1_pos = height // 2 - 1  # Posición inicial de la paleta del jugador 1
paddle2_pos = height // 2 - 1  # Posición inicial de la paleta del jugador 2
paddle_size = 3  # Tamaño de la paleta
score1, score2 = 0, 0  # Puntuación de los jugadores

# Función para dibujar el campo de juego
def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Player 1: {score1}   Player 2: {score2}")
    for y in range(height):
        line = ''
        for x in range(width):
            if x == 0 and paddle1_pos <= y < paddle1_pos + paddle_size:
                line += '|'
            elif x == width - 1 and paddle2_pos <= y < paddle2_pos + paddle_size:
                line += '|'
            elif [x, y] == ball_pos:
                line += 'O'
            else:
                line += ' '
        print(line)
    print("\nUse 'w'/'s' para mover la paleta izquierda y 'o'/'l' para la derecha.")

# Función para mover la bola
def move_ball():
    global ball_pos, ball_dir, score1, score2

    # Mover la bola en la dirección actual
    ball_pos[0] += ball_dir[0]
    ball_pos[1] += ball_dir[1]

    # Detectar colisión con la parte superior e inferior del campo de juego
    if ball_pos[1] <= 0 or ball_pos[1] >= height - 1:
        ball_dir[1] = -ball_dir[1]

    # Detectar colisión con la paleta izquierda
    if ball_pos[0] == 1 and paddle1_pos <= ball_pos[1] < paddle1_pos + paddle_size:
        ball_dir[0] = -ball_dir[0]

    # Detectar colisión con la paleta derecha
    if ball_pos[0] == width - 2 and paddle2_pos <= ball_pos[1] < paddle2_pos + paddle_size:
        ball_dir[0] = -ball_dir[0]

    # Detectar si un jugador ha marcado un punto
    if ball_pos[0] <= 0:
        score2 += 1
        reset_ball()
    elif ball_pos[0] >= width - 1:
        score1 += 1
        reset_ball()

# Función para reiniciar la bola en el centro
def reset_ball():
    global ball_pos, ball_dir
    ball_pos = [width // 2, height // 2]
    ball_dir = [1, 1 if (score1 + score2) % 2 == 0 else -1]

# Función para mover las paletas
def move_paddle(player, direction):
    global paddle1_pos, paddle2_pos

    if player == 1:
        if direction == 'up' and paddle1_pos > 0:
            paddle1_pos -= 1
        elif direction == 'down' and paddle1_pos < height - paddle_size:
            paddle1_pos += 1
    elif player == 2:
        if direction == 'up' and paddle2_pos > 0:
            paddle2_pos -= 1
        elif direction == 'down' and paddle2_pos < height - paddle_size:
            paddle2_pos += 1

# Función principal para ejecutar el juego
def play_game():
    while True:
        draw()
        move_ball()
        
        # Leer la entrada del usuario
        user_input = input().lower()

        # Mover las paletas según la entrada del usuario
        if user_input == 'w':
            move_paddle(1, 'up')
        elif user_input == 's':
            move_paddle(1, 'down')
        elif user_input == 'o':
            move_paddle(2, 'up')
        elif user_input == 'l':
            move_paddle(2, 'down')

        # Control de velocidad del juego
        time.sleep(0.1)

# Iniciar el juego
play_game()