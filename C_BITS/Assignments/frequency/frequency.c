int frequency(int num, int digit){
    int freq = 0;
    char char_num[30];
    char char_digit = digit + '0';

    sprintf(char_num, "%d", num);

    int size = strlen(char_num);
    for(int i=0;i<size;i++){
        if(char_num[i] == char_digit){
            freq++;
        }
    }
    return freq;
}