#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void) {
    char *envp[] = {
        "NAME=IMRAN",
        "ID=0546",
        NULL
    };

    pid_t pid = fork();

    if (pid == 0) {
        execle("/usr/bin/env", "env", (char *)NULL, envp);

        perror("execle failed");
        _exit(1);
    }

    if (pid > 0) {
        wait(NULL);
    }

    return 0;
}
