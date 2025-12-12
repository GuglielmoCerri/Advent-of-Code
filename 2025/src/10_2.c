#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define INPUT_FILE "10.txt"
#define MAX_ROWS 64
#define MAX_COLS 64

typedef struct {
    long long target[MAX_ROWS];
    int num_rows;
    int buttons[MAX_COLS][MAX_ROWS];
    int num_buttons;
} Machine;

long long min_total_presses;

double my_fabs(double x) {
    return (x < 0) ? -x : x;
}

long long my_round(double x) {
    return (long long)(x + 0.5);
}

void parse_indices(char *start, char *end, int *out_arr, int *count) {
    *count = 0;
    char *curr = start;
    while (curr < end) {
        if (isdigit(*curr)) {
            out_arr[(*count)++] = (int)strtol(curr, &curr, 10);
        } else {
            curr++;
        }
    }
}

int parse_machine(char *line, Machine *m) {
    memset(m, 0, sizeof(Machine));

    char *brace_start = strchr(line, '{');
    char *brace_end = strchr(line, '}');
    if (!brace_start || !brace_end) return 0;

    int t_idx = 0;
    char *ptr = brace_start + 1;
    while (ptr < brace_end) {
        if (isdigit(*ptr) || *ptr == '-') {
            m->target[t_idx++] = strtoll(ptr, &ptr, 10);
        } else {
            ptr++;
        }
    }
    m->num_rows = t_idx;

    ptr = line;
    char *paren_start = strchr(ptr, '(');

    while (paren_start && paren_start < brace_start) {
        char *paren_end = strchr(paren_start, ')');
        if (!paren_end) break;

        int indices[MAX_ROWS];
        int count = 0;
        parse_indices(paren_start + 1, paren_end, indices, &count);

        for (int i = 0; i < count; i++) {
            if (indices[i] < m->num_rows) {
                m->buttons[m->num_buttons][indices[i]] = 1;
            }
        }
        m->num_buttons++;

        ptr = paren_end + 1;
        paren_start = strchr(ptr, '(');
    }

    return 1;
}

void search(int free_idx, int num_free, int *free_cols, long long *free_vals,
            int num_rows, int num_cols, double **mat,
            long long current_sum) {

    if (min_total_presses != -1 && current_sum >= min_total_presses) return;

    if (free_idx == num_free) {
        long long pivot_sum = 0;
        int valid = 1;

        for (int r = 0; r < num_rows; r++) {
            int p_col = -1;
            for (int c = 0; c < num_cols; c++) {
                if (my_fabs(mat[r][c]) > 1e-9) {
                    p_col = c;
                    break;
                }
            }

            if (p_col == -1) {
                if (my_fabs(mat[r][num_cols]) > 1e-4) { valid = 0; break; }
                continue;
            }

            double val = mat[r][num_cols];

            for (int f = 0; f < num_free; f++) {
                int f_col = free_cols[f];
                if (my_fabs(mat[r][f_col]) > 1e-9) {
                    val -= mat[r][f_col] * free_vals[f];
                }
            }

            if (val < -1e-4) { valid = 0; break; }
            long long rounded = my_round(val);
            if (my_fabs(val - rounded) > 1e-4) { valid = 0; break; }

            pivot_sum += rounded;
        }

        if (valid) {
            long long total = current_sum + pivot_sum;
            if (min_total_presses == -1 || total < min_total_presses) {
                min_total_presses = total;
            }
        }
        return;
    }

    for (int v = 0; v <= 5000; v++) {
        free_vals[free_idx] = v;
        search(free_idx + 1, num_free, free_cols, free_vals,
               num_rows, num_cols, mat, current_sum + v);
    }
}

long long solve_machine(Machine *m) {
    int R = m->num_rows;
    int C = m->num_buttons;

    double **mat = malloc(R * sizeof(double*));
    for (int i = 0; i < R; i++) {
        mat[i] = calloc(C + 1, sizeof(double));
        for (int j = 0; j < C; j++) mat[i][j] = (double)m->buttons[j][i];
        mat[i][C] = (double)m->target[i];
    }

    int pivot_row = 0;
    int col_is_pivot[MAX_COLS];
    for(int i=0; i<MAX_COLS; i++) col_is_pivot[i] = 0;

    for (int col = 0; col < C && pivot_row < R; col++) {
        int sel = -1;
        double max_val = 0;

        for (int r = pivot_row; r < R; r++) {
            if (my_fabs(mat[r][col]) > max_val) {
                max_val = my_fabs(mat[r][col]);
                sel = r;
            }
        }

        if (max_val < 1e-9) continue;

        if (sel != pivot_row) {
            double *tmp = mat[pivot_row];
            mat[pivot_row] = mat[sel];
            mat[sel] = tmp;
        }

        double div = mat[pivot_row][col];
        for (int j = col; j <= C; j++) mat[pivot_row][j] /= div;

        for (int r = 0; r < R; r++) {
            if (r != pivot_row && my_fabs(mat[r][col]) > 1e-9) {
                double factor = mat[r][col];
                for (int j = col; j <= C; j++) mat[r][j] -= factor * mat[pivot_row][j];
            }
        }

        col_is_pivot[col] = 1;
        pivot_row++;
    }

    for (int r = pivot_row; r < R; r++) {
        if (my_fabs(mat[r][C]) > 1e-4) {
            for(int i=0; i<R; i++) free(mat[i]);
            free(mat);
            return -1;
        }
    }

    int free_cols[MAX_COLS];
    int num_free = 0;
    for (int c = 0; c < C; c++) {
        if (!col_is_pivot[c]) free_cols[num_free++] = c;
    }

    min_total_presses = -1;
    long long *free_vals = calloc(num_free + 1, sizeof(long long));

    search(0, num_free, free_cols, free_vals, R, C, mat, 0);

    free(free_vals);
    for(int i=0; i<R; i++) free(mat[i]);
    free(mat);

    return min_total_presses;
}

int main() {
    FILE *fp = fopen(INPUT_FILE, "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }

    char buffer[4096];
    long long grand_total = 0;
    int solved = 0;

    while (fgets(buffer, sizeof(buffer), fp)) {
        if (strlen(buffer) < 5) continue;
        Machine m;
        if (parse_machine(buffer, &m)) {
            long long res = solve_machine(&m);
            if (res != -1) {
                grand_total += res;
                solved++;
            }
        }
    }

    fclose(fp);
    printf("Solved %d machines.\n", solved);
    printf("Result: %lld\n", grand_total);

    return 0;
}
