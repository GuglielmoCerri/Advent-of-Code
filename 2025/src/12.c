#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_S 10
#define MAX_V 8
#define MAX_PTS 25
#define MAX_DIM 32

typedef struct { int r, c; } Pt;
typedef struct { int w, h, n; Pt p[MAX_PTS]; } Shape;

Shape shapes[MAX_S][MAX_V];
int shape_vars[MAX_S];
int num_shapes = 0;

void normalize(Shape *s) {
    int min_r = 100, min_c = 100, max_r = -1, max_c = -1;
    for (int i = 0; i < s->n; i++) {
        if (s->p[i].r < min_r) min_r = s->p[i].r;
        if (s->p[i].c < min_c) min_c = s->p[i].c;
    }
    for (int i = 0; i < s->n; i++) {
        s->p[i].r -= min_r;
        s->p[i].c -= min_c;
        if (s->p[i].r > max_r) max_r = s->p[i].r;
        if (s->p[i].c > max_c) max_c = s->p[i].c;
    }
    s->h = max_r + 1;
    s->w = max_c + 1;
}

int shape_cmp(Shape *a, Shape *b) {
    if (a->n != b->n || a->w != b->w || a->h != b->h) return 0;
    int match = 0;
    for (int i = 0; i < a->n; i++) {
        int found = 0;
        for (int j = 0; j < b->n; j++) {
            if (a->p[i].r == b->p[j].r && a->p[i].c == b->p[j].c) {
                found = 1; break;
            }
        }
        if (found) match++;
    }
    return match == a->n;
}

void gen_variants(int sid, Shape base) {
    Shape pool[8];
    int cnt = 0;

    pool[0] = base;
    normalize(&pool[0]);
    cnt++;

    for (int r = 1; r < 4; r++) {
        pool[r] = pool[r-1];
        Shape *prev = &pool[r-1];
        Shape *curr = &pool[r];

        for (int i = 0; i < prev->n; i++) {
            curr->p[i].r = prev->p[i].c;
            curr->p[i].c = prev->h - 1 - prev->p[i].r;
        }
        normalize(curr);
        cnt++;
    }

    pool[4] = base;
    for (int i = 0; i < base.n; i++) pool[4].p[i].c = base.w - 1 - base.p[i].c;
    normalize(&pool[4]);
    cnt++;

    for (int r = 5; r < 8; r++) {
        pool[r] = pool[r-1];
        Shape *prev = &pool[r-1];
        Shape *curr = &pool[r];
        for (int i = 0; i < prev->n; i++) {
            curr->p[i].r = prev->p[i].c;
            curr->p[i].c = prev->h - 1 - prev->p[i].r;
        }
        normalize(curr);
        cnt++;
    }

    int u = 0;
    for (int i = 0; i < 8; i++) {
        int is_new = 1;
        for (int j = 0; j < u; j++) {
            if (shape_cmp(&pool[i], &shapes[sid][j])) {
                is_new = 0; break;
            }
        }
        if (is_new) shapes[sid][u++] = pool[i];
    }
    shape_vars[sid] = u;
}

int grid[MAX_DIM][MAX_DIM];
int G_W, G_H;
int counts[MAX_S];
int slack;

int solve() {
    int r = -1, c = -1;
    // Find first empty cell
    for (int i = 0; i < G_H && r == -1; i++) {
        for (int j = 0; j < G_W; j++) {
            if (grid[i][j] == 0) {
                r = i; c = j;
                break;
            }
        }
    }

    if (r == -1) return 1; // Grid full

    for (int id = 0; id < num_shapes; id++) {
        if (counts[id] > 0) {
            for (int v = 0; v < shape_vars[id]; v++) {
                Shape *s = &shapes[id][v];
                // Try aligning each point of shape to (r,c)
                for (int k = 0; k < s->n; k++) {
                    int dr = r - s->p[k].r;
                    int dc = c - s->p[k].c;

                    // Check bounds and collision
                    if (dr < 0 || dc < 0 || dr + s->h > G_H || dc + s->w > G_W) continue;

                    int fit = 1;
                    for (int m = 0; m < s->n; m++) {
                        if (grid[dr + s->p[m].r][dc + s->p[m].c]) {
                            fit = 0; break;
                        }
                    }

                    if (fit) {
                        // Place
                        for (int m = 0; m < s->n; m++) grid[dr + s->p[m].r][dc + s->p[m].c] = id + 1;
                        counts[id]--;

                        if (solve()) return 1;

                        // Backtrack
                        counts[id]++;
                        for (int m = 0; m < s->n; m++) grid[dr + s->p[m].r][dc + s->p[m].c] = 0;
                    }
                }
            }
        }
    }

    // Try leaving it empty
    if (slack > 0) {
        grid[r][c] = 99;
        slack--;
        if (solve()) return 1;
        slack++;
        grid[r][c] = 0;
    }

    return 0;
}

int main() {
    FILE *f = fopen("12.txt", "r");
    if (!f) return 1;

    char line[100];
    Shape current_shape;
    current_shape.n = 0;
    int reading_shape = 0;
    int total_solvable = 0;

    while (fgets(line, sizeof(line), f)) {
        if (strchr(line, 'x') && strchr(line, ':')) {

            int qw, qh;
            char *ptr = line;
            if (sscanf(ptr, "%dx%d:", &qw, &qh) != 2) continue;

            ptr = strchr(ptr, ':') + 1;
            int total_area = 0;
            int req_area = 0;

            for (int i = 0; i < num_shapes; i++) {
                int c;
                sscanf(ptr, "%d", &c);
                counts[i] = c;
                req_area += c * shapes[i][0].n;
                while (*ptr && !isdigit(*ptr)) ptr++;
                while (*ptr && isdigit(*ptr)) ptr++;
            }

            G_W = qw;
            G_H = qh;
            total_area = qw * qh;
            slack = total_area - req_area;

            if (slack >= 0) {
                memset(grid, 0, sizeof(grid));
                if (solve()) total_solvable++;
            }
        } else if (strchr(line, ':')) {
            if (reading_shape) {
                gen_variants(num_shapes, current_shape);
                num_shapes++;
            }
            current_shape.n = 0;
            current_shape.w = 0;
            current_shape.h = 0;
            reading_shape = 1;
        } else {
            int len = strlen(line);
            int has_hash = 0;
            for(int i=0; i<len; i++) if(line[i]=='#') has_hash=1;

            if (has_hash) {
                for (int i = 0; i < len; i++) {
                    if (line[i] == '#') {
                        current_shape.p[current_shape.n].r = current_shape.h;
                        current_shape.p[current_shape.n].c = i;
                        current_shape.n++;
                    }
                }
                current_shape.h++;
                if (len > current_shape.w) current_shape.w = len;
            } else if (reading_shape && current_shape.n > 0) {
                gen_variants(num_shapes, current_shape);
                num_shapes++;
                reading_shape = 0;
            }
        }
    }
    if (reading_shape && current_shape.n > 0) {
         gen_variants(num_shapes, current_shape);
         num_shapes++;
    }
    printf("%d\n", total_solvable);
    fclose(f);
    return 0;
}
