#include <stdio.h>

int main() {
    FILE *f = fopen("1.txt", "r");
    long long a = 0;
    int p = 50, d, t;
    char c;
    while (fscanf(f, " %c%d", &c, &d) == 2) {
        if (c == 'R') {
            a += (p + d) / 100;
            p = (p + d) % 100;
        } else {
            t = p == 0 ? 100 : p;
            if (d >= t) a += 1 + (d - t) / 100;
            p = (p - d % 100 + 100) % 100;
        }
    }
    printf("%lld\n", a);
    return 0;
}
