// #include <stdio.h>
// #include <unistd.h>
// #include <stdlib.h>
// #include <sys/types.h>
// #include <fcntl.h>
// #include <sys/stat.h>


// int main() {
// int fd = open("output.txt", O_WRONLY | O_CREAT);

// printf("%d\n", fd);
// int new_fd = dup2(fd, 1);

// printf("%s\n", "BRO BUTT");
// printf("%s\n", "BRO THIS IS IMRAN");

// }



#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main() {

    int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

    if (fd == -1) {
        perror("open");
        return 1;
    }

    dup2(fd, STDOUT_FILENO);

    close(fd);

    printf("Hello from Operating Systems!\n");
    printf("This output goes into a file.\n");

    return 0;
}