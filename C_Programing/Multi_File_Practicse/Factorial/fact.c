
int fact(int a){
    int result = 1;
    for(int i = a; i>=1; i--){
        result *= i;
    }
    return result;
}