#include <stdio.h>

void printArray(int arr[], int n) {
    printf("[");                   
    for (int i = 0; i < n; i++) {   
        printf("%d", arr[i]);       
                                    
        if (i < n - 1) {         
            printf(", ");    
        }
    }
    printf("]\n");                
}

void insertAtBeginning(int arr[], int *n, int value) {   
    for (int i = *n - 1; i >= 0; i--) {
        arr[i + 1] = arr[i];   
    }
    arr[0] = value;  
    (*n)++;
}

void insertAtIndex(int arr[], int *n, int pos, int value) {
    for (int i = *n - 1; i >= pos; i--) {
        arr[i + 1] = arr[i];
    }
    arr[pos] = value;
    (*n)++;
}

void insertBeforeIndex(int arr[], int *n, int pos, int value) {
    for (int i = *n - 1; i >= pos; i--) {
        arr[i + 1] = arr[i];
    }
    arr[pos] = value;
    (*n)++;
}
   ->  [10, 20, 55, 30, 40, 50]

void insertAfterIndex(int arr[], int *n, int pos, int value) {
    for (int i = *n - 1; i >= pos + 1; i--) {
        arr[i + 1] = arr[i];
    }
    arr[pos + 1] = value;
    (*n)++;
}

void doubleIt(int *p) {
    *p = *p * 2;
}

int main() { 
    printf("=== Pointer Demo ===\n");
    int x = 5;
    printf("Before doubleIt: x = %d\n", x);  
    doubleIt(&x);
    printf("After doubleIt:  x = %d\n", x); 
    printf("\n");  
    printf("The address of x is: %p\n", (void*)&x);
    printf("The value at that address is: %d\n", x);
    printf("\n");

    int arr[10];
    int n;
  
    printf("=== Scenario 1: Insert at Beginning ===\n");

    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;
    arr[3] = 40;
    arr[4] = 50;
    n = 5;

    printf("Before:  ");
    printArray(arr, n);               
    insertAtBeginning(arr, &n, 5);

    printf("After:   ");
    printArray(arr, n);              
    printf("n is now: %d\n", n);     
    printf("\n");

    printf("=== Scenario 2: Insert at Index ===\n");

    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;
    arr[3] = 40;
    arr[4] = 50;
    n = 5;

    printf("Before:  ");
    printArray(arr, n);

    insertAtIndex(arr, &n, 2, 99);   

    printf("After:   ");
    printArray(arr, n);              
    printf("n is now: %d\n", n);      
    printf("\n");

    printf("=== Scenario 3: Insert Before Index ===\n");

    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;
    arr[3] = 40;
    arr[4] = 50;
    n = 5;

    printf("Before:  ");
    printArray(arr, n);

    insertBeforeIndex(arr, &n, 3, 77);  

    printf("After:   ");
    printArray(arr, n);              
    printf("n is now: %d\n", n);      
    printf("\n");
    
    printf("=== Scenario 4: Insert After Index ===\n");
 
    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;
    arr[3] = 40;
    arr[4] = 50;
    n = 5;

    printf("Before:  ");
    printArray(arr, n);

    insertAfterIndex(arr, &n, 1, 55);   
    printf("After:   ");
    printArray(arr, n);               
    printf("n is now: %d\n", n);      
    printf("\n");

    return 0;   
}
