// #include <stdio.h>
// #include <unistd.h>

// int x = 100;  // Global variable

// int main() {

//     pid_t pid = fork();

//     if (pid == 0) {
//         // Child process
       
//         printf("Child x: %d\n", x);
//     }
//     else if (pid > 0) {
//         // Parent process
//         x = 500;
//         printf("Parent x: %d\n", x);
//     }

//     return 0;
// }



#include <stdio.h>
#include <unistd.h>

int x = 10;

void display(const char* var) {
    printf("Hello from PID: %d\n", getpid());
    printf("%s\n", var);
}

int main() {

    pid_t pid = fork();

    if (pid == 0) {
        // Child
        display("Child");
    }
    else if (pid > 0) {
        // Parent
        display("Parent");
    }

    return 0;
}