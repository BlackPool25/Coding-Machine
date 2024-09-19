int avg(int n, int list[]){
    int sum = 0;
    for(int i = 0; i<n; i++){
    list[i]*=2;
    sum+=list[i];
    }
    return sum/n;
}