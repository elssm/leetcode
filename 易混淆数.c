bool confusingNumber(int N) {
    int a[1000];
    int c=0;
    int sum=0;
    int t=N;
    int i;
    while(N){
        i=N%10;
        if(i==0||i==1||i==6||i==8||i==9){
            a[c++]=i;
            N=N/10;
        }
        else
            return false;
    }
    for(i=0;i<c;i++){
        if(a[i]==0)
            sum=sum*10+0;
        else if(a[i]==1)
            sum=sum*10+1;
        else if(a[i]==6)
            sum=sum*10+9;
        else if(a[i]==8)
            sum=sum*10+8;
        else if(a[i]==9)
            sum=sum*10+6;
    }
    if(sum==t)
        return false;
    else 
        return true;
    
}
