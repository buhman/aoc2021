.SUFFIXES:

OBJCOPY = objcopy
LD = ld
CC = gcc

CFLAGS = -Wall -Werror -O3

%.txt.o: %.txt
	$(LD) -r -b binary $< -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

solution: input.txt.o solution.o
	$(CC) $(CFLAGS) $^ -o $@
