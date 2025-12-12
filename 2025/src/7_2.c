#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROWS 2000
#define MAX_COLS 2000
#define INPUT_FILE "7.txt"

char grid[MAX_ROWS][MAX_COLS];
int rows = 0;
int cols = 0;

unsigned long long current_counts[MAX_COLS];
unsigned long long next_counts[MAX_COLS];

int main() {
    FILE *fp = fopen(INPUT_FILE, "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }

    char buffer[MAX_COLS + 10]; 
    while (fgets(buffer, sizeof(buffer), fp) && rows < MAX_ROWS) {
        int len = strlen(buffer);

        while (len > 0 && (buffer[len-1] == '\r' || buffer[len-1] == '\n')) buffer[--len] = '\0';

        if (len > cols) cols = len;
        for (int i = 0; i < len; i++) grid[rows][i] = buffer[i];
        for (int i = len; i < MAX_COLS; i++) {
            grid[rows][i] = '.';
        }
        rows++;
    }
    fclose(fp);

    memset(current_counts, 0, sizeof(current_counts));
    int start_row = -1;
    int start_col = -1;

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == 'S') {
                start_row = r;
                start_col = c;
                break;
            }
        }
        if (start_row != -1) break;
    }

    if (start_row == -1) {
        printf("Error: S not found\n");
        return 1;
    }

    current_counts[start_col] = 1;
    unsigned long long grand_total = 0;

    for (int r = start_row; r < rows; r++) {
        memset(next_counts, 0, sizeof(next_counts));

        for (int c = 0; c < cols; c++) {
            unsigned long long count = current_counts[c];
            if (count == 0) continue;
            char cell = grid[r][c];
            int next_r = r + 1;

            if (cell == '^') {
                // Left Branch (row+1, col-1)
                if (next_r >= rows || c - 1 < 0) grand_total += count;
                else next_counts[c - 1] += count;

                // Right Branch (row+1, col+1)
                if (next_r >= rows || c + 1 >= cols) grand_total += count;
                else next_counts[c + 1] += count;

            } else {
                if (next_r >= rows) grand_total += count;
                else next_counts[c] += count;
            }
        }
        memcpy(current_counts, next_counts, sizeof(current_counts));
    }

    printf("Total active timelines: %llu\n", grand_total);
    return 0;
}
