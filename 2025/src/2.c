#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int is_invalid_id(long long n) {
    char s[64];
    sprintf(s, "%lld", n);
    int len = strlen(s);

    for (int sub_len = 1; sub_len <= len / 2; sub_len++) {
    	if (len % sub_len == 0) {
		int is_pattern = 1;
            	for (int i = sub_len; i < len; i++) {
                if (s[i] != s[i % sub_len]) {
                    is_pattern = 0;
                    break;
                }
            }

            if (is_pattern) return 1;
        }
    }

    return 0;
}

int main() {
    FILE *fp = fopen("2.txt", "r");
    if (fp == NULL) {
        printf("Could not open file 2.txt\n");
        return 1;
    }

    long long start, end;
    long long total_sum = 0;

    while (fscanf(fp, "%lld-%lld", &start, &end) == 2) {
        for (long long i = start; i <= end; i++) {
            if (is_invalid_id(i)) {
                total_sum += i;            
		}
        }

        fgetc(fp);
    }

    printf("Answer Part 2: %lld\n", total_sum);
    fclose(fp);
    return 0;
}
