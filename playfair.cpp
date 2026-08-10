#include <stdio.h>
#include <string.h>
#include <ctype.h>

char matrix[5][5];

void generateMatrix(char key[]) {
    char alphabet[] = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    int used[26] = {0};
    int i, j = 0, k = 0;

    used['J'-'A'] = 1;

    for(i=0; key[i]; i++) {
        char ch = toupper(key[i]);
        if(ch=='J') ch='I';

        if(ch>='A' && ch<='Z' && !used[ch-'A']) {
            matrix[j][k++] = ch;
            used[ch-'A'] = 1;
            if(k==5){k=0;j++;}
        }
    }

    for(i=0; alphabet[i]; i++) {
        char ch=alphabet[i];
        if(!used[ch-'A']) {
            matrix[j][k++] = ch;
            used[ch-'A']=1;
            if(k==5){k=0;j++;}
        }
    }
}

void findPosition(char ch,int *row,int *col){
    if(ch=='J') ch='I';

    for(int i=0;i<5;i++)
        for(int j=0;j<5;j++)
            if(matrix[i][j]==ch){
                *row=i;
                *col=j;
                return;
            }
}

int main(){
    char key[50], text[100];

    printf("Enter key: ");
    scanf("%s",key);

    generateMatrix(key);

    printf("Enter plaintext (uppercase): ");
    scanf("%s",text);

    printf("Ciphertext: ");

    for(int i=0;text[i];i+=2){
        char a=text[i];
        char b=text[i+1];

        if(b=='\0') b='X';

        int r1,c1,r2,c2;

        findPosition(a,&r1,&c1);
        findPosition(b,&r2,&c2);

        if(r1==r2){
            printf("%c%c",matrix[r1][(c1+1)%5],matrix[r2][(c2+1)%5]);
        }
        else if(c1==c2){
            printf("%c%c",matrix[(r1+1)%5][c1],matrix[(r2+1)%5][c2]);
        }
        else{
            printf("%c%c",matrix[r1][c2],matrix[r2][c1]);
        }
    }
    return 0;
}
