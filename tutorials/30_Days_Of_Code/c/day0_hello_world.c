#include <stdio.h>
#include <stdlib.h>

int main() {
    // Declare a variable named 'input_string' to hold our input.
    char input_string[100] = {'\0'};
    
    // Read a full line of input from stdin and save it to our variable, input_string.
    scanf("%[^\n]s", input_string); // reads till newline
    //fgets(input, sizeof(input), stdin); // using fgets
    // scanf("%99[^\n]", input); // safer option for the second. Size minus the terminating NULL character

    // Print a string literal saying "Hello, World." to stdout using printf.
    printf("Hello, World.\n");
    
    // TODO: Write a line of code here that prints the contents of input_string to stdout.
    printf("%s", input_string);
    
    return 0;
}

