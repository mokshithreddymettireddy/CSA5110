#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char plain[100];
    char key[27];

    printf("Enter substitution key (26 unique letters): ");
    scanf("%s", key);

    getchar();

    printf("Enter plaintext: ");
    fgets(plain, sizeof(plain), stdin);

    printf("Ciphertext: ");

    for(int i = 0; plain[i] != '\0'; i++) {
        char ch = plain[i];

        if(isupper(ch))
            printf("%c", toupper(key[ch - 'A']));
        else if(islower(ch))
            printf("%c", tolower(key[ch - 'a']));
        else
            printf("%c", ch);
    }

    return 0;
}
