#include <stdio.h>
#include <ctype.h>

int main() {
	char input[10001];
	int num, i;
	scanf("%d", &num);
	scanf("%s", input);
	for (i = 0; i < num; i++) {
		if (input[i] >= 'A' && input[i] <= 'Z')
			input[i] = tolower(input[i]);
		else if (input[i] >= 'a' && input[i] <= 'z')
			input[i] = toupper(input[i]);
	}
	
	printf("%s\n", input);
	return 0;
}