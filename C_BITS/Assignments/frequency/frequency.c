int frequency(int num, int target){
    int freq = 0;
    char char_num[30];
    char char_target = target + '0';

    sprintf(char_num, "%d", num);

    int size = strlen(char_num);
    for(int i=0;i<size;i++){
        if(char_num[i] == char_target){
            freq++;
        }
    }
    return freq;
}