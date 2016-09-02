int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int i = 0, j = numbersSize-1;
    *returnSize = 2;
    int *result = (int*)calloc(2, sizeof(int));
    
    while(i<j){
        if(numbers[i] + numbers[j] == target){
            result[0] = i+1;
            result[1] = j+1;
            return result;
        } 
        if((numbers[i] + numbers[j]) > target){
            j--;
        }
        else{
            i++;
        }
    }
    return result;
}
