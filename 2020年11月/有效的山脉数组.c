bool validMountainArray(int* A, int ASize){
    int mount,maxindex,max;
    int i,j;
    if(ASize==0 || ASize==1)
        return false;
    else if(ASize==3){
        if(A[0]<A[1] &&A[1]>A[2]){
            return true;
        }else{
            return false;
        }
    }
    else{
        maxindex=0;
        max=A[0];
        for(i=1;i<ASize;i++){
            if(A[i]>max){
                max=A[i];
                maxindex=i;
            }
        }
        if(maxindex==0 || maxindex==ASize-1)
            return false;
        for(i=0;i<maxindex;i++){
            if(A[i]>=A[i+1]){
                return false;
            }
        }
        for(j=maxindex+1;j<ASize;j++){
            if(A[j-1]<=A[j]){
                return false;
            }
        }
    return true;
    }
}