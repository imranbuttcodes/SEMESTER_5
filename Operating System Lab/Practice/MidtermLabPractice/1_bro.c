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
    // if (fork() || fork()) {
    //     printf("A\n");
    // }

    // printf("B\n");

    // if (0 || 1 && 0) {
    //     printf("A");
    // }

    // printf("BRO");
        // execlp("./a.out", NULL);

        // execlp("ls", "ls", "-a", NULL);
        execlp("./a.out", "./a.out", NULL);

    return 0;
}