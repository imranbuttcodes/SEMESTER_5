// #include <stdio.h>
// #include <unistd.h>
// #include <sys/wait.h>

// int main() {
//     pid_t pid = fork();

//     if (pid == 0) {
//         printf("Child: I am working.\n");
//         sleep(2);
//         printf("Child: I am terminating.\n");
//     }
//     else if (pid > 0) {
//         printf("Parent: I am working.\n");
//         sleep(4);
//         printf("Parent: I am terminating.\n");
//         int status;
//         pid_t pid = wait(&status);    
//         printf("pid: %d\n", pid);
//         if (WIFEXITED(status)) {
//              printf("Child exit code: %d\n", WEXITSTATUS(status));
//         }
//     }

//     return 0;
// }

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void) {
    pid_t pid = fork();

    if (pid == 0) {
        printf("Child: Working...\n");
        sleep(3);
        printf("Child: Finished!\n");
    }
    else if (pid > 0) {
        printf("Parent: Waiting for child...\n");

        wait(NULL);

        printf("Parent: Child has finished!\n");
    }

    return 0;
}