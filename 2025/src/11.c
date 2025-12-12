#include <stdio.h>
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

// Helper to get ID of a node by name.
int getId(const char *name) {
    for (int i = 0; i < node_count; i++) {
        if (strcmp(nodes[i].name, name) == 0) {
            return i;
        }
    }
    if (node_count >= MAX_NODES) {
        fprintf(stderr, "Error: Max nodes limit reached.\n");
        exit(1);
    }
    strcpy(nodes[node_count].name, name);
    nodes[node_count].neighbor_count = 0;
    return node_count++;
}

// Count paths
long long countPaths(int current_id, int target_id) {
    if (current_id == target_id) return 1;
    if (memo[current_id] != -1) return memo[current_id];

    long long total_paths = 0;

    for (int i = 0; i < nodes[current_id].neighbor_count; i++) {
        int next_id = nodes[current_id].neighbors[i];
        total_paths += countPaths(next_id, target_id);
    }
    memo[current_id] = total_paths;
    return total_paths;
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
            else fprintf(stderr, "Error: Max edges limit reached for %s\n", source_name);
        }
    }
    fclose(fp);

    // Find IDs for start and end
    int start_id = getId("you");
    int end_id = getId("out");

    for (int i = 0; i < MAX_NODES; i++) {
        memo[i] = -1;
    }

    long long result = countPaths(start_id, end_id);
    printf("Total paths from 'you' to 'out': %lld\n", result);
    return 0;
}
