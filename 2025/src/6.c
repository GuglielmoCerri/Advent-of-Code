#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_ROWS 1000
#define MAX_COLS 20000
#define INPUT_FILE "6.txt"

char grid[MAX_ROWS][MAX_COLS];
int max_row = 0;
int max_col = 0;

int is_column_empty(int col) {
    for (int r = 0; r < max_row; r++) {
        char c = grid[r][col];
        if (c != ' ' && c != '\0' && c != '\n' && c != '\r') {
            return 0;
        }
    }
    return 1;
}

long long solve_problem_block(int start_col, int end_col) {
    long long numbers[100];
    int count = 0;
    char operator = 0;

    for (int r = 0; r < max_row; r++) {
        char line_buffer[256];
        int buf_idx = 0;
        int has_digit = 0;
        for (int c = start_col; c <= end_col; c++) {
            char ch = grid[r][c];
            if (!isspace(ch) && ch != '\0') {
                line_buffer[buf_idx++] = ch;
                if (isdigit(ch)) has_digit = 1;
            }
        }
        line_buffer[buf_idx] = '\0';

        if (buf_idx > 0) {
            if (strchr(line_buffer, '+')) operator = '+'
	    else if (strchr(line_buffer, '*')) operator = '*';
            else if (has_digit) numbers[count++] = atoll(line_buffer);
        }
    }

    if (count == 0) return 0;
    long long result = 0;

    if (operator == '+') {
        result = 0;
        for (int i = 0; i < count; i++) {
            result += numbers[i];
        }
    } else if (operator == '*') {
        result = 1;
        for (int i = 0; i < count; i++) {
            result *= numbers[i];
        }
    } else {
        if (count == 1) return numbers[0];
    }

    return result;
}

int main() {
    FILE *fp = fopen(INPUT_FILE, "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }
    for (int i = 0; i < MAX_ROWS; i++) {
        memset(grid[i], ' ', MAX_COLS);
        grid[i][MAX_COLS - 1] = '\0';
    }

    char buffer[MAX_COLS];
    int row = 0;
    while (fgets(buffer, sizeof(buffer), fp)) {
        int len = strlen(buffer);
        while (len > 0 && (buffer[len-1] == '\n' || buffer[len-1] == '\r')) buffer[--len] = ' ';

	for (int i = 0; i < len; i++) {
            grid[row][i] = buffer[i];
        }

        if (len > max_col) max_col = len;
        row++;
    }
    max_row = row;
    fclose(fp);

    long long grand_total = 0;
    int in_block = 0;
    int start_col = 0;

    for (int c = 0; c <= max_col; c++) {
        int empty = is_column_empty(c);

        if (!in_block && !empty) {
            in_block = 1;
            start_col = c;
        } else if (in_block && empty) {
            grand_total += solve_problem_block(start_col, c - 1);
            in_block = 0;
        }
    }

    printf("Grand Total: %lld\n", grand_total);
    return 0;
}
