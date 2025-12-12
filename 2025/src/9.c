#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INPUT_FILE "9.txt"

typedef struct {
    long long x;
    long long y;
} Point;

Point *points;
int num_points = 0;

int main() {
    FILE *fp = fopen(INPUT_FILE, "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }

    int capacity = 1000;
    points = malloc(sizeof(Point) * capacity);
    if (!points) {
        perror("Memory allocation failed");
        fclose(fp);
        return 1;
    }

    long long x, y;
    while (fscanf(fp, "%lld,%lld", &x, &y) == 2) {
        if (num_points >= capacity) {
            capacity *= 2;
            points = realloc(points, sizeof(Point) * capacity);
            if (!points) {
                perror("Memory reallocation failed");
                fclose(fp);
                return 1;
            }
        }
        points[num_points].x = x;
        points[num_points].y = y;
        num_points++;
    }
    fclose(fp);

    if (num_points < 2) {
        printf("Not enough tiles to form a rectangle.\n");
        free(points);
        return 0;
    }

    long long max_area = 0;

    for (int i = 0; i < num_points; i++) {
        for (int j = i + 1; j < num_points; j++) {
            long long width = llabs(points[i].x - points[j].x) + 1;
            long long height = llabs(points[i].y - points[j].y) + 1;
            long long area = width * height;

            if (area > max_area) max_area = area;
        }
    }

    printf("Largest Area: %lld\n", max_area);
    free(points);
    return 0;
}
