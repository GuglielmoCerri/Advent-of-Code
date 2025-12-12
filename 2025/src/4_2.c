#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROWS 2048
#define MAX_COLS 2048

char grid[MAX_ROWS][MAX_COLS];
char remove_mask[MAX_ROWS][MAX_COLS];

int main() {
    FILE *fp = fopen("4.txt", "r");
    if (fp == NULL) {
        perror("Error: Could not open 4.txt");
        return 1;
    }

    int rows = 0;
    int cols = 0;

    while (fgets(grid[rows], MAX_COLS, fp)) {
        grid[rows][strcspn(grid[rows], "\r\n")] = 0;

        if (rows == 0) {
            cols = strlen(grid[rows]);
        }
        rows++;
        if (rows >= MAX_ROWS) break;
    }
    fclose(fp);

    long total_removed = 0;
    int changed;

    do {
        changed = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                remove_mask[r][c] = 0;

                if (grid[r][c] == '@') {
                    int neighbors = 0;

                    for (int dy = -1; dy <= 1; dy++) {
                        for (int dx = -1; dx <= 1; dx++) {
                            if (dy == 0 && dx == 0) continue;

                            int nr = r + dy;
                            int nc = c + dx;

                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                                if (grid[nr][nc] == '@') {
                                    neighbors++;
                                }
                            }
                        }
                    }

                    if (neighbors < 4) {
                        remove_mask[r][c] = 1;
                        changed = 1;
                    }
                }
            }
        }

        if (changed) {
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c < cols; c++) {
                    if (remove_mask[r][c] == 1) {
                        grid[r][c] = '.'; 
                        total_removed++;
                    }
                }
            }
        }
    } while (changed);

    printf("Total rolls removed: %ld\n", total_removed);

    return 0;
}
