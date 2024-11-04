#include<stdio.h>

void selection_sort(int[],int);

void selection_sort(int arr[], int size){

    for(int i=0;i<size-1;i++){
        int min = i;
        for(int j = i+1;j<size;j++){
            if(arr[j]<arr[min]){
                min = j;
            }
        }

        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
    for(int i=0;i<size;i++){
        printf("%d ", arr[i]);
    }
}

int main(){
    int arr[] = {12, 2, 4 ,2 , 4 ,6 , 4 ,33,8, 33};
    selection_sort(arr, sizeof(arr)/sizeof(arr[0]));
    return 0;
}