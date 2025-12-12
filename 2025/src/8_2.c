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
int *sz;

int compare_edges(const void *a, const void *b) {
    Edge *edgeA = (Edge *)a;
    Edge *edgeB = (Edge *)b;
    if (edgeA->dist_sq < edgeB->dist_sq) return -1;
    if (edgeA->dist_sq > edgeB->dist_sq) return 1;
    return 0;
}

void make_set(int v) {
    parent[v] = v;
    sz[v] = 1;
}

int find_set(int v) {
    if (v == parent[v]) return v;
    return parent[v] = find_set(parent[v]);
}

int union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (sz[a] < sz[b]) {
            int temp = a; a = b; b = temp;
        }
        parent[b] = a;
        sz[a] += sz[b];
        return 1;
    }
    return 0; 
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
    
    if (num_points < 2) {
        printf("Not enough points to form connections.\n");
        return 0;
    }

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
    
    int num_components = num_points;
    long long result = 0;
    int found = 0;

    for (int i = 0; i < num_edges; i++) {
        int u = edges[i].u;
        int v = edges[i].v;

        if (union_sets(u, v)) {
            num_components--;
            
            if (num_components == 1) {
                printf("Graph fully connected at edge between index %d and %d\n", u, v);
                printf("Point 1 X: %lld, Point 2 X: %lld\n", points[u].x, points[v].x);
                
                result = points[u].x * points[v].x;
                found = 1;
                break;
            }
        }
    }

    if (found) printf("Result: %lld\n", result);
    else printf("Could not fully connect the graph.\n");
    
    free(points);
    free(edges);
    free(parent);
    free(sz);

    return 0;
}
