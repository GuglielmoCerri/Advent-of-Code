#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Optimization for speed
#pragma GCC optimize("O3")

#define INPUT_FILE "9.txt"

typedef struct {
    long long x;
    long long y;
} Point;

Point *points;
int num_points = 0;

int is_valid_rect(Point p1, Point p2) {
    long long min_x = (p1.x < p2.x) ? p1.x : p2.x;
    long long max_x = (p1.x > p2.x) ? p1.x : p2.x;
    long long min_y = (p1.y < p2.y) ? p1.y : p2.y;
    long long max_y = (p1.y > p2.y) ? p1.y : p2.y;
    double mid_x = (min_x + max_x) / 2.0;
    double mid_y = (min_y + max_y) / 2.0;

    int crossings = 0;
    for (int i = 0; i < num_points; i++) {
        Point a = points[i];
        Point b = points[(i + 1) % num_points];

        if (((a.y > mid_y) != (b.y > mid_y))) {
            double intersect_x = (double)(b.x - a.x) * (mid_y - a.y) / (double)(b.y - a.y) + a.x;
            if (intersect_x > mid_x) crossings++;
        }
    }
    // The rectangle must be Inside (Odd crossings).
    if (crossings % 2 == 0) return 0;

    for (int i = 0; i < num_points; i++) {
        Point a = points[i];
        Point b = points[(i + 1) % num_points];

        if (a.x == b.x) { 
            // Vertical Edge
            long long edge_x = a.x;
            long long y_s = (a.y < b.y) ? a.y : b.y;
            long long y_e = (a.y > b.y) ? a.y : b.y;

            if (edge_x > min_x && edge_x < max_x) {
                long long overlap_start = (min_y > y_s) ? min_y : y_s;
                long long overlap_end   = (max_y < y_e) ? max_y : y_e;
                
                if (overlap_start < overlap_end) return 0;
            }
        } else {
            long long edge_y = a.y;
            long long x_s = (a.x < b.x) ? a.x : b.x;
            long long x_e = (a.x > b.x) ? a.x : b.x;

            if (edge_y > min_y && edge_y < max_y) {
                long long overlap_start = (min_x > x_s) ? min_x : x_s;
                long long overlap_end   = (max_x < x_e) ? max_x : x_e;
                
                if (overlap_start < overlap_end) return 0;
            }
        }
    }

    return 1;
}

int main() {
    FILE *fp = fopen(INPUT_FILE, "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }

    int capacity = 2000;
    points = malloc(sizeof(Point) * capacity);

    long long x_in, y_in;

    while (fscanf(fp, "%lld,%lld", &x_in, &y_in) == 2) {
        if (num_points >= capacity) {
            capacity *= 2;
            points = realloc(points, sizeof(Point) * capacity);
        }
        points[num_points].x = x_in;
        points[num_points].y = y_in;
        num_points++;
    }
    fclose(fp);

    if (num_points < 2) return 0;

    long long max_area = 0;

    for (int i = 0; i < num_points; i++) {
        for (int j = i + 1; j < num_points; j++) {
            long long width = llabs(points[i].x - points[j].x) + 1;
            long long height = llabs(points[i].y - points[j].y) + 1;
            long long area = width * height;

            if (area <= max_area) continue;

            if (is_valid_rect(points[i], points[j])) max_area = area;
        }
    }

    printf("Largest Valid Area: %lld\n", max_area);
    free(points);
    return 0;
}
