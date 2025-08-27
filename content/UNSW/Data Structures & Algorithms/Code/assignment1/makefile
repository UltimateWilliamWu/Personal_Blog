charstack : charStack.o stackTester.o
	gcc -o charstack charStack.o stackTester.o

charStack.o : charStack.c charStack.h
	gcc -Wall -Werror -std=c11 -c charStack.c

stackTester.o : stackTester.c charStack.h
	gcc -Wall -Werror -std=c11 -c stackTester.c

numerals : stack.o numerals.o
	gcc -o numerals stack.o numerals.o

stack.o : stack.c stack.h
	gcc -Wall -Werror -std=c11 -c stack.c

numerals.o : numerals.c stack.h
	gcc -Wall -Werror -std=c11 -c numerals.c
	