
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MAX = 100;

struct Employee {
    char id[10];
    char name[30];
    char gender;
    char position[30];
    int experience;
    float pay;
};

int loadEmployees(struct Employee e[]) {
    FILE *fp = fopen("task1.txt", "r");
    int count = 0;

    if (fp == NULL) {
        return 0;
    }

    while (count < MAX &&
           fscanf(fp, "%9s %29s %c %29s %d %f",
                  e[count].id,
                  e[count].name,
                  &e[count].gender,
                  e[count].position,
                  &e[count].experience,
                  &e[count].pay) == 6) {
        count++;
    }

    fclose(fp);
    return count;
}

void saveEmployees(struct Employee e[], int count) {
    FILE *fp = fopen("task1.txt", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }

    for (int i = 0; i < count; i++) {
        fprintf(fp, "%s %s %c %s %d %.2f\n",
                e[i].id,
                e[i].name,
                e[i].gender,
                e[i].position,
                e[i].experience,
                e[i].pay);
    }

    fclose(fp);
}

void displayEmployees(struct Employee e[], int count) {
    if (count == 0) {
        printf("No employee records found.\n");
        return;
    }

    printf("\nID\tName\tGender\tPosition\tExperience\tPay\n");

    for (int i = 0; i < count; i++) {
        printf("%s\t%s\t%c\t%s\t\t%d\t\t%.2f\n",
               e[i].id,
               e[i].name,
               e[i].gender,
               e[i].position,
               e[i].experience,
               e[i].pay);
    }
}

void addEmployee(struct Employee e[], int *count) {
    if (*count >= MAX) {
        printf("Maximum employee limit reached.\n");
        return;
    }

    printf("Enter employee ID: ");
    scanf("%9s", e[*count].id);

    printf("Enter name: ");
    scanf("%29s", e[*count].name);

    printf("Enter gender (m/f): ");
    scanf(" %c", &e[*count].gender);

    printf("Enter job position: ");
    scanf("%29s", e[*count].position);

    printf("Enter experience in years: ");
    scanf("%d", &e[*count].experience);

    printf("Enter pay: ");
    scanf("%f", &e[*count].pay);

    (*count)++;
    saveEmployees(e, *count);

    printf("Employee added successfully.\n");
}

void searchEmployee(struct Employee e[], int count) {
    char searchID[10];

    printf("Enter employee ID to search: ");
    scanf("%9s", searchID);

    for (int i = 0; i < count; i++) {
        if (strcmp(e[i].id, searchID) == 0) {
            printf("\nEmployee Found:\n");
            printf("ID: %s\n", e[i].id);
            printf("Name: %s\n", e[i].name);
            printf("Gender: %c\n", e[i].gender);
            printf("Position: %s\n", e[i].position);
            printf("Experience: %d years\n", e[i].experience);
            printf("Pay: %.2f\n", e[i].pay);
            return;
        }
    }

    printf("Employee not found.\n");
}

int main() {
    struct Employee employees[MAX];
    int count = loadEmployees(employees);
    int choice;

    do {
        printf("\n===== Employee Management System =====\n");
        printf("1. Display all employees\n");
        printf("2. Add employee\n");
        printf("3. Search employee by ID\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                displayEmployees(employees, count);
                break;

            case 2:
                addEmployee(employees, &count);
                break;

            case 3:
                searchEmployee(employees, count);
                break;

            case 4:
                printf("Exiting program.\n");
                break;

            default:
                printf("Invalid choice. Try again.\n");
        }

    } while (choice != 4);

    return 0;
}
