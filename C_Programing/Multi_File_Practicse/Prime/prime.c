void prime(int x){
    int result=0;
    for(int i = 2; i<x ; i++){
        if (x%i==0)
        result = 1;
        break;
    }
    if (result == 1)
    printf("\nIt is not a prime number.");
    else if (result == 0)
    printf("\nIt is a prime number.");
}