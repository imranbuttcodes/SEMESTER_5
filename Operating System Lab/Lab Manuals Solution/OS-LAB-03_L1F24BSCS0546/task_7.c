
#include <stdio.h>

struct Employee {
    int id;
    char name[50];
    int age;
    float pay;
};

int main() {
    struct Employee e;

    printf("Enter employee ID: ");
    scanf("%d", &e.id);

    printf("Enter employee name: ");
    scanf("%49s", e.name);

    printf("Enter employee age: ");
    scanf("%d", &e.age);

    printf("Enter employee pay: ");
    scanf("%f", &e.pay);

    printf("\n--- Employee Information ---\n");
    printf("ID: %d\n", e.id);
    printf("Name: %s\n", e.name);
    printf("Age: %d\n", e.age);
    e.pay = 1.21222222;
    printf("Pay: %.2f\n", e.pay);

    return 0;
}
