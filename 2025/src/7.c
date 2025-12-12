#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROWS 2000
#define MAX_COLS 2000
#define INPUT_FILE "7.txt"

char grid[MAX_ROWS][MAX_COLS];
int rows = 0;
int cols = 0;

unsigned char current_beams[MAX_COLS];
unsigned char next_beams[MAX_COLS];

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

	strcpy(grid[rows], buffer);
        rows++;
    }
    fclose(fp);

    memset(current_beams, 0, sizeof(current_beams));
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
        printf("Error: Start point 'S' not found.\n");
        return 1;
    }

    current_beams[start_col] = 1;

    long long total_splits = 0;

    for (int r = start_row + 1; r < rows; r++) {
        memset(next_beams, 0, sizeof(next_beams));

        int active_beams_count = 0;

        for (int c = 0; c < cols; c++) {
            if (current_beams[c]) {
                active_beams_count++;
                char cell = grid[r][c];

                if (cell == '^') {
                    total_splits++;

                    if (c > 0) next_beams[c - 1] = 1;
                    if (c < cols - 1) next_beams[c + 1] = 1;
                }
                else next_beams[c] = 1;
            }
        }

        if (active_beams_count == 0) break;

        memcpy(current_beams, next_beams, sizeof(current_beams));
    }

    printf("Total splits: %lld\n", total_splits);
    return 0;
}
