OBJ = dijkstra.o main.o min_heap.o
CFLAGS = -Wall -Werror -O3

all: solution

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

solution: $(OBJ)
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -f *.o solution
