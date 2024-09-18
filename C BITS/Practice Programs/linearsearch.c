#include<stdio.h>

int main(){
    int arr[20];
    int size, search, loc=-1;
    printf("\nEnter the size of the array (less than 20): ");
    scanf("%d", &size);
    printf("\nEnter the elements: ");
    for(int i=0;i<size;i++)
    scanf("%d", &arr[i]);
    printf("\nEnter the searching element: ");
    scanf("%d", &search);

    for(int i=0;i<size;i++){
        if(search==arr[i]){
            loc = i;
            break;
        }
    }

    if (loc>-1)
    printf("\nThe searching element %d is at the location %d", search, loc);

    else
    printf("\nThe element does not exsist in the array.");

    return 0;
}