#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define SIZE 5

struct Patient {
    int id;
    char name[50];
};

struct Patient queue[SIZE];
int front = -1 , rear = -1;

int isFull() {
    return ((rear + 1) % SIZE == front);
}

int isEmpty() {
    return (front == -1);
}

void registerPatient(int id , char name[]) {
    if(isFull()) {
        printf("\nQueue Full! No more patients can be registered.\n");
        return;
    }
    if(isEmpty()) {
        front = rear = 0;
    } else {
        rear = (rear + 1) % SIZE; 
    }
    queue[rear].id = id;
    strcpy(queue[rear].name , name);
    printf("\nPatient %s (ID: %d) registered successfully.\n", name, id);
}

void servePatient() {
    if(isEmpty()) {
        printf("\nNo patients to serve.\n");
        return;
    }
    printf("\nPatient served: %s (ID: %d)\n", queue[front].name, queue[front].id);

    if(front == rear) {
        front = rear = -1;
    } else {
        front = (front + 1) % SIZE;
    }
}

void displayQueue() {
    if(isEmpty()) {
        printf("No patients in queue.\n");
        return;
    }
    printf("\n...Patients waiting...\n");
    int i = front;
    while(1) {
        printf("ID: %d | Name: %s\n", queue[i].id, queue[i].name);
        if(i == rear) break;
        i = (i + 1) % SIZE;
    }
}

int main() {
    int choice , id;
    char name[50];

    while(1) {
        printf("\n----Hospital Management System----\n");
        printf("1. Register Patient\n");
        printf("2. Serve Patient\n");
        printf("3. Display Queue\n");
        printf("4. Exit\n");
        printf("Enter Choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("Enter Patient ID: ");
                scanf("%d", &id);
                printf("Enter Patient Name: ");
                scanf("%s", name);
                registerPatient(id, name);
                break;

            case 2:
                servePatient();
                break;

            case 3:
                displayQueue();
                break;

            case 4:
                printf("Exiting... Goodbye, Take Care!\n");
                exit(0);

            default:
                printf("Invalid choice! Try again.\n");
        }
    }
    return 0;
}