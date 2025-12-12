ù#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NODES 5000
#define MAX_EDGES 50
#define NAME_LEN 50
#define LINE_BUF 1024

typedef struct {
    char name[NAME_LEN];
    int neighbors[MAX_EDGES];
    int neighbor_count;
} Node;

Node nodes[MAX_NODES];
int node_count = 0;
long long memo[MAX_NODES];

int getId(const char *name) {
    for (int i = 0; i < node_count; i++) {
        if (strcmp(nodes[i].name, name) == 0) return i;
    }
    
    if (node_count >= MAX_NODES) {
        fprintf(stderr, "Error: Max nodes limit reached.\n");
        exit(1);
    }
    
    strcpy(nodes[node_count].name, name);
    nodes[node_count].neighbor_count = 0;
    return node_count++;
}

long long dfs(int u, int target_id) {
    if (u == target_id) return 1;
    if (memo[u] != -1) return memo[u];

    long long total_paths = 0;

    for (int i = 0; i < nodes[u].neighbor_count; i++) {
        int next_id = nodes[u].neighbors[i];
        total_paths += dfs(next_id, target_id);
    }

    memo[u] = total_paths;
    return total_paths;
}

long long countPaths(int start, int end) {
    if (start == -1 || end == -1) return 0;
    for (int i = 0; i < MAX_NODES; i++) memo[i] = -1;
    return dfs(start, end);
}

int main() {
    FILE *fp = fopen("11.txt", "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }

    char line[LINE_BUF];

    while (fgets(line, sizeof(line), fp)) {
        line[strcspn(line, "\r\n")] = 0;
        if (strlen(line) == 0) continue;

        char *token = strtok(line, " ");
        if (!token) continue;

        char source_name[NAME_LEN];
        strncpy(source_name, token, NAME_LEN);
        char *colon_pos = strchr(source_name, ':');
        if (colon_pos) *colon_pos = '\0';

        int u = getId(source_name);

        while ((token = strtok(NULL, " ")) != NULL) {
            int v = getId(token);
            if (nodes[u].neighbor_count < MAX_EDGES) nodes[u].neighbors[nodes[u].neighbor_count++] = v;
        }
    }
    fclose(fp);

    int svr = getId("svr");
    int out = getId("out");
    int dac = getId("dac");
    int fft = getId("fft");

    printf("Nodes found - svr: %d, out: %d, dac: %d, fft: %d\n", svr, out, dac, fft);

    long long s1_a = countPaths(svr, dac);
    long long s1_b = countPaths(dac, fft);
    long long s1_c = countPaths(fft, out);
    long long paths_via_dac_then_fft = s1_a * s1_b * s1_c;

    long long s2_a = countPaths(svr, fft);
    long long s2_b = countPaths(fft, dac);
    long long s2_c = countPaths(dac, out);
    long long paths_via_fft_then_dac = s2_a * s2_b * s2_c;

    printf("\nPath Calculations:\n");
    printf("1. svr -> dac -> fft -> out: %lld * %lld * %lld = %lld\n", 
           s1_a, s1_b, s1_c, paths_via_dac_then_fft);
    printf("2. svr -> fft -> dac -> out: %lld * %lld * %lld = %lld\n", 
           s2_a, s2_b, s2_c, paths_via_fft_then_dac);

    long long total = paths_via_dac_then_fft + paths_via_fft_then_dac;
    printf("\nTotal paths from 'svr' to 'out' visiting both 'dac' and 'fft': %lld\n", total);
    return 0;
}
