#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>

// Define the game constants
#define WIDTH 20
#define HEIGHT 20
#define SNAKE_SIZE 5
#define FOOD_SIZE 1

// Define the game structures
typedef struct {
    int x;
    int y;
} Point;

typedef enum {
    UP,
    DOWN,
    LEFT,
    RIGHT,
    NONE
} Direction;

// Initialize the game variables
Point snake[Snake_SIZE];
Direction direction = NONE;
int score = 0;
int food_x, food_y;
int head_x, head_y;
int tail_x, tail_y;

// Function to draw the game board
void draw_board() {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            printf(" ");
        }
        printf("\n");
    }
}

// Function to draw the snake and food on the board
void draw_game() {
    draw_board();
    for (int i = 0; i < Snake_SIZE; i++) {
        if (snake[i].x == head_x && snake[i].y == head_y) {
            printf("O"); // Head of the snake
        } else if (snake[i].x == tail_x && snake[i].y == tail_y) {
            printf("o"); // Tail of the snake
        } else {
            printf("*"); // Body of the snake
        }
    }
    printf("\n");
}

// Function to check for collisions with walls or self
int check_collision() {
    if (head_x == 0 || head_x == WIDTH - 1 || head_y == 0 || head_y == HEIGHT - 1) {
        return 1; // Collision with wall
    }
    for (int i = 0; i < Snake_SIZE; i++) {
        if (snake[i].x == head_x && snake[i].y == head_y && i != 0) {
            return 2; // Collision with self
        }
    }
    return 0; // No collision
}

// Main game loop
int main() {
    srand(time(NULL));
    food_x = rand() % WIDTH;
    food_y = rand() % HEIGHT;

    while (1) {
        draw_game();
        printf("Score: %d\n", score);
        printf("Press W/A/S/D to move, E to eat, or Q to quit.\n");
        char input[2];
        gets(input);

        if (input[0] == 'w' || input[0] == 'W') {
            direction = UP;
        } else if (input[0] == 's' || input[0] == 'S') {
            direction = DOWN;
        } else if (input[0] == 'a' || input[0] == 'A') {
            direction = LEFT;
        } else if (input[0] == 'd' || input[0] == 'D') {
            direction = RIGHT;
        } else if (input[0] == 'e' || input[0] == 'E') {
            // Eat the food
            score++;
            snake[Snake_SIZE - 1].x = head_x;
            snake[Snake_SIZE - 1].y = head_y;
            Snake_SIZE++;
        } else if (input[0] == 'q' || input[0] == 'Q') {
            break; // Quit the game
        }

        // Move the snake
        switch (direction) {
            case UP:
                head_x--;
                break;
            case DOWN:
                head_x++;
                break;
            case LEFT:
                head_y--;
                break;
            case RIGHT:
                head_y++;
                break;
        }

        if (check_collision()) {
            printf("Game Over!\n");
            return 0;
        }

        // Update the tail position
        tail_x = snake[Snake_SIZE - 1].x;
        tail_y = snake[Snake_SIZE - 1].y;

        // Check for food collision
        if (head_x == food_x && head_y == food_y) {
            score++;
            food_x = rand() % WIDTH;
            food_y = rand() % HEIGHT;
        }
    }

    return 0;
}