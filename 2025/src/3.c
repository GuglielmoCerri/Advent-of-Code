#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define INPUT_FILE "3.txt"
#define MAX_LINE_LENGTH 4096
#define KEEP_COUNT 12

int main() {
    FILE *fp;
    char line[MAX_LINE_LENGTH];
    char digits[MAX_LINE_LENGTH];
    char stack[MAX_LINE_LENGTH];
    unsigned long long total_output_joltage = 0;

    fp = fopen(INPUT_FILE, "r");
    if (fp == NULL) {
        fprintf(stderr, "Error: Could not open file %s\n", INPUT_FILE);
        return 1;
    }

    while (fgets(line, sizeof(line), fp)) {
        int len = 0;
        for (int i = 0; line[i] != '\0'; i++) {
            if (isdigit(line[i])) {
                digits[len++] = line[i];
            }
        }
        digits[len] = '\0';

        if (len < KEEP_COUNT) continue;

        int to_remove = len - KEEP_COUNT;
        int top = 0;

        for (int i = 0; i < len; i++) {
            char c = digits[i];

            while (top > 0 && stack[top - 1] < c && to_remove > 0) {
                top--;
                to_remove--;
            }
            stack[top++] = c;
        }

        char result_str[KEEP_COUNT + 1];
        for (int k = 0; k < KEEP_COUNT; k++) {
            result_str[k] = stack[k];
        }
        result_str[KEEP_COUNT] = '\0';

        char *endptr;
        unsigned long long current_val = strtoull(result_str, &endptr, 10);
        total_output_joltage += current_val;
    }

    fclose(fp);
    printf("Total output joltage: %llu\n", total_output_joltage);
    return 0;
}
