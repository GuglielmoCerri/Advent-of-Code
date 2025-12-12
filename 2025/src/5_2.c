#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 128
#define MAX_RANGES 10000

typedef struct {
    long start;
    long end;
} Range;

int compareRanges(const void *a, const void *b) {
    Range *r1 = (Range *)a;
    Range *r2 = (Range *)b;
    if (r1->start < r2->start) return -1;
    if (r1->start > r2->start) return 1;
    return 0;
}

int main() {
    FILE *file = fopen("5.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    Range ranges[MAX_RANGES];
    int range_count = 0;
    char line[MAX_LINE_LENGTH];

    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\r\n")] = 0;

        if (strlen(line) == 0) break;

        if (range_count >= MAX_RANGES) {
            fprintf(stderr, "Error: Too many ranges.\n");
            break;
        }

        if (sscanf(line, "%ld-%ld", &ranges[range_count].start, &ranges[range_count].end) == 2) range_count++;
    }
    fclose(file);

    if (range_count == 0) {
        printf("No ranges found.\n");
        return 0;
    }

    qsort(ranges, range_count, sizeof(Range), compareRanges);

    long total_fresh_ids = 0;
    long current_start = ranges[0].start;
    long current_end = ranges[0].end;

    for (int i = 1; i < range_count; i++) {
    	if (ranges[i].start <= current_end) {
            if (ranges[i].end > current_end) current_end = ranges[i].end;
        } else {
            total_fresh_ids += (current_end - current_start + 1);
            current_start = ranges[i].start;
            current_end = ranges[i].end;
        }
    }

    total_fresh_ids += (current_end - current_start + 1);
    printf("Total unique fresh ingredient IDs: %ld\n", total_fresh_ids);
    return 0;
}
