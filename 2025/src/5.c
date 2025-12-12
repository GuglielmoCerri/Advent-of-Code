#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 128
#define MAX_RANGES 10000

typedef struct {
    long start;
    long end;
} Range;

int main() {
    FILE *file = fopen("5.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    Range ranges[MAX_RANGES];
    int range_count = 0;

    char line[MAX_LINE_LENGTH];
    int parsing_ranges = 1;
    int fresh_count = 0;

    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\r\n")] = 0;

        if (strlen(line) == 0) {
            parsing_ranges = 0;
            continue;
        }

        if (parsing_ranges) {
            if (range_count >= MAX_RANGES) {
                fprintf(stderr, "Error: Too many ranges in input file.\n");
                fclose(file);
                return 1;
            }

            if (sscanf(line, "%ld-%ld", &ranges[range_count].start, &ranges[range_count].end) == 2) {
                range_count++;
            }
        } else {
            long id;
            if (sscanf(line, "%ld", &id) == 1) {
                int is_fresh = 0;

                for (int i = 0; i < range_count; i++) {
                    if (id >= ranges[i].start && id <= ranges[i].end) {
                        is_fresh = 1;
                        break;
                    }
                }

                if (is_fresh) fresh_count++;
            }
        }
    }

    fclose(file);
    printf("Number of fresh ingredient IDs: %d\n", fresh_count);
    return 0;
}
