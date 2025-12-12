#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INPUT_FILE "8.txt"

typedef struct {
    long long x, y, z;
} Point;

typedef struct {
    int u;          
    int v;          
    long long dist_sq;
} Edge;

Point *points;
int num_points = 0;
Edge *edges;
long long num_edges = 0;

int *parent;
int *sz; // Size of each component

// sorting edges by distance
int compare_edges(const void *a, const void *b) {
    Edge *edgeA = (Edge *)a;
    Edge *edgeB = (Edge *)b;
    if (edgeA->dist_sq < edgeB->dist_sq) return -1;
    if (edgeA->dist_sq > edgeB->dist_sq) return 1;
    return 0;
}

// sorting sizes descending
int compare_sizes(const void *a, const void *b) {
    int sizeA = *(int *)a;
    int sizeB = *(int *)b;
    return sizeB - sizeA;
}

void make_set(int v) {
    parent[v] = v;
    sz[v] = 1;
}

int find_set(int v) {
    if (v == parent[v]) return v;
    return parent[v] = find_set(parent[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (sz[a] < sz[b]) {
            int temp = a; a = b; b = temp;
        }
        parent[b] = a;
        sz[a] += sz[b];
    }
}

int main() {
    FILE *fp = fopen(INPUT_FILE, "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }
    int capacity = 1000;
    points = malloc(sizeof(Point) * capacity);

    long long x, y, z;

    while (fscanf(fp, "%lld,%lld,%lld", &x, &y, &z) == 3) {
        if (num_points >= capacity) {
            capacity *= 2;
            points = realloc(points, sizeof(Point) * capacity);
        }
        points[num_points].x = x;
        points[num_points].y = y;
        points[num_points].z = z;
        num_points++;
    }
    fclose(fp);

    long long max_edges = (long long)num_points * (num_points - 1) / 2;
    edges = malloc(sizeof(Edge) * max_edges);

    int edge_idx = 0;
    for (int i = 0; i < num_points; i++) {
        for (int j = i + 1; j < num_points; j++) {
            long long dx = points[i].x - points[j].x;
            long long dy = points[i].y - points[j].y;
            long long dz = points[i].z - points[j].z;

            edges[edge_idx].u = i;
            edges[edge_idx].v = j;
            edges[edge_idx].dist_sq = dx*dx + dy*dy + dz*dz;
            edge_idx++;
        }
    }
    num_edges = edge_idx;
    qsort(edges, num_edges, sizeof(Edge), compare_edges);
    parent = malloc(sizeof(int) * num_points);
    sz = malloc(sizeof(int) * num_points);
    for (int i = 0; i < num_points; i++) make_set(i);

    int limit = 1000;
    if (limit > num_edges) limit = num_edges;
    for (int i = 0; i < limit; i++) union_sets(edges[i].u, edges[i].v);

    int *final_sizes = malloc(sizeof(int) * num_points);
    int fs_count = 0;

    for (int i = 0; i < num_points; i++) {
        if (parent[i] == i) final_sizes[fs_count++] = sz[i];
    }
    
    qsort(final_sizes, fs_count, sizeof(int), compare_sizes);

    long long result = 1;
    int count_to_multiply = (fs_count < 3) ? fs_count : 3;

    for (int i = 0; i < count_to_multiply; i++) result *= final_sizes[i];

    printf("Result: %lld\n", result);

    free(points);
    free(edges);
    free(parent);
    free(sz);
    free(final_sizes);

    return 0;
}
