#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char text[100], key[100];
    int i, j = 0;

    printf("Enter plaintext: ");
    fgets(text, sizeof(text), stdin);

    printf("Enter key: ");
    scanf("%s", key);

    printf("Ciphertext: ");

    for(i = 0; text[i] != '\0'; i++) {
        char ch = text[i];

        if(isalpha(ch)) {
            int shift = toupper(key[j % strlen(key)]) - 'A';

            if(isupper(ch))
                printf("%c", ((ch-'A'+shift)%26)+'A');
            else
                printf("%c", ((ch-'a'+shift)%26)+'a');

            j++;
        }
        else
            printf("%c", ch);
    }

    return 0;
}
