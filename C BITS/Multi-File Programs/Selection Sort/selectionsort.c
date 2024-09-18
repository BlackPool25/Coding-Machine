void selectionsort(int arr[], int n)
{
   int i,j,min;
   for(i=0;i<n-1;i++){
    min = i;
    for(j=i+1;j<n;j++){
        if(arr[j] < arr[min])
        min=j;
    }

    int temp = arr[min];
    arr[min] = arr[i];
    arr[i]= temp;
   } 
}
