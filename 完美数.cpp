#incldue<stdio.h>
bool checkPerfectNumber(int num) {
    int i,sum=1;
    for(i=2;i<=num/2;i++){
        if(num%i==0){
            sum=sum+i;  //1~e的8次方中有5个完美数 
        }				//6，28，496，8128，33550336 
    }
    if(sum==num&&sum!=1)
        return true;
    else
        return false;
}
int main(void){
	checkPerfectNumber(5);
}
