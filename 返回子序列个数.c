//�������ַ�����һ����Ϊsource�ַ�����һ����Ϊtarget�ַ��� 
//������target�ַ����ܲ�����source�ַ����������й���
//���磬source�ַ�����abc target�ַ�����abbac
//��ôtarget������ab b ac���ɣ�ab b ac�ֱ���abc��������
//����Ҫ���������еĸ���3
//������ source�ַ�����abc target�ַ�����abdc  
//target������abc�������й��� ��� ����Ҫ����-1 
#include<stdio.h>
#include<string.h>
int main(){
	char s[20]="xyz";
	char m[20]="xzyxz";
	int i,j,k,l;
	int count=0;
	int p=0;
	k=strlen(s);
	l=strlen(m);
	int a[20]={0};
	int b[20]={0};
	for(i=1;i<k;i++){
		for(j=0;j<i;j++){
			if(s[i]==s[j]){
			a[i]=a[j];
			break;
		}
}
		if(j==i)
			a[i]=++count;
		else
			continue;
	}
//	 for(i=0;i<k;i++)
//	 	printf("%d",a[i]);
	 	
	for(i=0;i<l;i++){
		for(j=0;j<k;j++){
			if(m[i]==s[j]){
				b[i]=a[j];
				break;
			}
		}
		if(j==k)
			return -1;
		else
			continue;
	}
	
	for(i=1;i<l;i++){
		if(b[i]<b[i-1]){
			p++;
		}
	}
	p=p+1;

printf("%d",p);
	
//	for(i=0;i<l;i++)
//		printf("%d",b[i]);
		
		 
/**	for(i=0;i<l;i++){
		for(j=0;j<k;j++)
		{
			if(m[i]==s[j])
			break;
		}
		if(j==k)
			putchar(m[i]);
		else
			continue; 
	}**/
	return 0;
} 
