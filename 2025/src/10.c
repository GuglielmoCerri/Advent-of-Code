#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <limits.h>

#define INPUT_FILE "10.txt"
#define MAX_LIGHTS 64
#define MAX_BUTTONS 64

typedef unsigned long long Bitmask;

typedef struct {
    Bitmask target;
    int num_lights;
    Bitmask buttons[MAX_BUTTONS];
    int num_buttons;
} Machine;

int parse_machine(char *line, Machine *m) {
    m->target = 0;
    m->num_lights = 0;
    m->num_buttons = 0;

    char *ptr = line;

    char *start = strchr(ptr, '[');
    char *end = strchr(ptr, ']');
    if (!start || !end) return 0;

    for (char *c = start + 1; c < end; c++) {
        if (*c == '#') {
            m->target |= (1ULL << m->num_lights);
        }
        m->num_lights++;
    }

    ptr = end + 1;

    while ((start = strchr(ptr, '(')) != NULL) {
        char *brace = strchr(ptr, '{');
        if (brace && brace < start) break;

        end = strchr(start, ')');
        if (!end) break;

        Bitmask btn = 0;
        char *num_ptr = start + 1;
        while (num_ptr < end) {
            if (isdigit(*num_ptr)) {
                int idx = strtol(num_ptr, &num_ptr, 10);
                if (idx >= 0 && idx < m->num_lights) {
                    btn |= (1ULL << idx);
                }
            } else {
                num_ptr++;
            }
        }

        m->buttons[m->num_buttons++] = btn;
        ptr = end + 1;
    }

    return 1;
}

int solve_machine(Machine *m) {
    int R = m->num_lights;
    int C = m->num_buttons;

    unsigned char mat[MAX_LIGHTS][MAX_BUTTONS + 1];
    memset(mat, 0, sizeof(mat));

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if ((m->buttons[c] >> r) & 1) {
                mat[r][c] = 1;
            }
        }
        if ((m->target >> r) & 1) {
            mat[r][C] = 1;
        }
    }

    int pivot_row = 0;
    int pivot_cols[MAX_BUTTONS];
    for(int i=0; i<MAX_BUTTONS; i++) pivot_cols[i] = -1;

    for (int col = 0; col < C && pivot_row < R; col++) {
        int sel = -1;
        for (int row = pivot_row; row < R; row++) {
            if (mat[row][col]) {
                sel = row;
                break;
            }
        }

        if (sel == -1) {
            continue;
        }

        if (sel != pivot_row) {
            for (int k = col; k <= C; k++) {
                unsigned char temp = mat[pivot_row][k];
                mat[pivot_row][k] = mat[sel][k];
                mat[sel][k] = temp;
            }
        }

        for (int row = 0; row < R; row++) {
            if (row != pivot_row && mat[row][col]) {
                for (int k = col; k <= C; k++) {
                    mat[row][k] ^= mat[pivot_row][k];
                }
            }
        }

        pivot_cols[col] = pivot_row;
        pivot_row++;
    }

    for (int r = pivot_row; r < R; r++) {
        if (mat[r][C]) return -1;
    }

    int free_vars[MAX_BUTTONS];
    int num_free = 0;
    for (int c = 0; c < C; c++) {
        if (pivot_cols[c] == -1) {
            free_vars[num_free++] = c;
        }
    }

    if (num_free > 25) {
        fprintf(stderr, "Warning: %d free variables, brute force may be slow.\n", num_free);
    }

    int min_presses = INT_MAX;
    unsigned long long combinations = 1ULL << num_free;

    int x[MAX_BUTTONS];

    for (unsigned long long i = 0; i < combinations; i++) {
        int current_presses = 0;

        for (int k = 0; k < num_free; k++) {
            if ((i >> k) & 1) {
                x[free_vars[k]] = 1;
                current_presses++;
            } else {
                x[free_vars[k]] = 0;
            }
        }

        for (int c = 0; c < C; c++) {
            if (pivot_cols[c] != -1) {
                int r = pivot_cols[c];
                int val = mat[r][C];
                for (int k = c + 1; k < C; k++) {
                    if (mat[r][k]) {
                        val ^= x[k];
                    }
                }
                x[c] = val;
                if (val) current_presses++;
            }
        }

        if (current_presses < min_presses) {
            min_presses = current_presses;
        }
    }

    return min_presses;
}

int main() {
    FILE *fp = fopen(INPUT_FILE, "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }

    char buffer[2048];
    long long total_presses = 0;
    int machines_solved = 0;

    while (fgets(buffer, sizeof(buffer), fp)) {
        if (strlen(buffer) < 5) continue;

        Machine m;
        if (parse_machine(buffer, &m)) {
            int needed = solve_machine(&m);
            if (needed != -1) {
                total_presses += needed;
                machines_solved++;
            } else {
                printf("Machine with no solution found!\n");
            }
        }
    }

    fclose(fp);

    printf("Solved %d machines.\n", machines_solved);
    printf("Fewest total button presses: %lld\n", total_presses);

    return 0;
}
