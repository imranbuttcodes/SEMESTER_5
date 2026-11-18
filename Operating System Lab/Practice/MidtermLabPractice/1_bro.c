// #include <stdio.h>
// #include <unistd.h>

// int main() {
//     fork() && fork();

//     printf("Hello\n");

//     return 0;
// }


#include <stdio.h>
#include <unistd.h>

int main() {
    if (fork() || fork()) {
        printf("A\n");
    }

    printf("B\n");

    return 0;
}