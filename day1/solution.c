#include <limits.h>
#include <stdio.h>
#include <time.h>

#include "input.h"

int parse_base10_int(const char ** buf)
{
  int n = 0;

  while (**buf >= 48 && **buf <= 57) {
    n *= 10;
    switch (*(*buf)++) {
    case '0': break;
    case '1': n += 1; break;
    case '2': n += 2; break;
    case '3': n += 3; break;
    case '4': n += 4; break;
    case '5': n += 5; break;
    case '6': n += 6; break;
    case '7': n += 7; break;
    case '8': n += 8; break;
    case '9': n += 9; break;
    }
  }

 return n;
}

void solution(int * part1, int * part2)
{
  const char * bufi = (void *)&_binary_input_txt_start;
  const char * end = (void *)&_binary_input_txt_end;

  int a, b, c;
  a = parse_base10_int(&bufi);
  bufi++;
  b = parse_base10_int(&bufi);
  bufi++;
  c = parse_base10_int(&bufi);
  bufi++;
  int sum = a + b + c;
  int next_sum;
  int next_num;

  *part1 = 0;
  *part2 = 0;

  *part1 += (a < b) + (b < c);

  while (bufi < end) {
    next_num = parse_base10_int(&bufi);
    bufi++;

    // part1
    *part1 += c < next_num;

    // part2
    next_sum = (sum - a) + next_num;
    *part2 += sum < next_sum;
    a = b;
    b = c;
    c = next_num;
  }
}

void bench()
{
  clock_t start, end;
  double elapsed;
  int part1, part2;

  start = clock();
  for (int i = 0; i < 10000; i++) {
    solution(&part1, &part2);
    (void)part1;
    (void)part2;
  }
  end = clock();

  elapsed = ((double) (end - start)) / CLOCKS_PER_SEC;
  printf("time: %f\n", elapsed);
}

int main()
{
  int part1, part2;
  solution(&part1, &part2);
  printf("part1: %d\n", part1);
  printf("part2: %d\n", part2);

  bench();

  return 0;
}
