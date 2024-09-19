#include<stdio.h>

int min_num(int array[], int size){
    int min = array[0], pos = 0;
    for(int i=0;i<size;i++){
        if(array[i] < min){
            min = array[i];
            pos = i;
        }
    }
    printf("%d %d", min, pos);
}


int main(){
    int size;
    printf("Enter the size of the array: ");
    scanf("%d", &size);
    int arr[size];
    printf("Enter the elements of the array: ");
    for(int i = 0;i<size;i++){
        scanf("%d", &arr[i]);
    }
    min_num(arr, size);
}