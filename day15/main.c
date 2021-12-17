#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>
#include <string.h>

#include "dijkstra.h"

void
parse_input(int * buf)
{
  char c;
  ssize_t ret;

  int risk;
  int index = 0;
  while ((ret = read(STDIN_FILENO, &c, 1)) != 0) {
    switch (c) {
    case '\n':
      continue;
    case '1': risk = 1; break;
    case '2': risk = 2; break;
    case '3': risk = 3; break;
    case '4': risk = 4; break;
    case '5': risk = 5; break;
    case '6': risk = 6; break;
    case '7': risk = 7; break;
    case '8': risk = 8; break;
    case '9': risk = 9; break;
    default:
      fprintf(stderr, "input error\n");
      exit(1);
      break;
    }

    buf[index] = risk;

    index++;
  }
}

void
print_buf(const int * buf, int width, int height)
{
  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      fprintf(stderr, "%d", buf[y * width + x]);
    }
    fprintf(stderr, "\n");
  }
}

void
tile_graph(const int * src, int * dst, int width, int height)
{
  for (int ty = 0; ty < 5; ty++) {
    for (int y = 0; y < height; y++) {
      for (int tx = 0; tx < 5; tx++) {
        for (int x = 0; x < width; x++) {
          int next_risk = (src[y * width + x] + (ty + tx));
          while (next_risk > 9)
            next_risk = next_risk - 9;
          assert(next_risk != 0);
          int nx = width * tx + x;
          int ny = height * ty + y;
          fprintf(stderr, "%d %d %d\n", next_risk, nx, ny);
          dst[ny * width + nx] = next_risk;
        }
      }
      return;
    }
  }
}

void
part1(const int * graph, const int width, const int height)
{
  vertex_t path[100 * 100];
  dijkstra(graph,
           width, height,
           width, height,
           (vertex_t){0, 0},
           path);

  vertex_t it = {width - 1, height - 1};
  int sum = 0;
  while (1) {
    //fprintf(stderr, "%d %d\n", it.x, it.y);
    int ix = it.y * width + it.x;
    sum += graph[ix];
    it = path[ix];
    if (it.y == 0 && it.y == 0)
      break;
  }

  fprintf(stderr, "part1 %d\n", sum);
}

void
part2(const int * graph, const int width, const int height)
{
  /*
    part 2
   */

  vertex_t path[100 * 100 * 5 * 5];
  dijkstra(graph,
           width * 5, height * 5,
           width, height,
           (vertex_t){0, 0},
           path);

  vertex_t it = {(width * 5) - 1, (height * 5) - 1};
  int sum = 0;
  while (1) {
    int ix = it.y * (width * 5) + it.x;
    int graph_u = (it.y % height) * width + (it.x % width);
    int graph_offset = it.y / height + it.x / width;
    int risk = graph[graph_u] + graph_offset;
    while (risk > 9)
      risk = risk - 9;

    sum += risk;
    it = path[ix];

    if (it.y == 0 && it.y == 0)
      break;
  }

  fprintf(stderr, "part2 %d\n", sum);
}

int
main(int argc, char * argv[])
{
  if (argc < 3) {
    fprintf(stderr, "argc < 3\n");
    return 1;
  }

  char * end[2];
  long width = strtol(argv[1], &end[0], 10);
  long height = strtol(argv[2], &end[1], 10);
  if (*end[0] != '\0' || *end[0] != '\0') {
    fprintf(stderr, "argv not int \n");
    return 1;
  }

  int graph[height * width];
  parse_input(graph);
  //print_buf(graph, width, height * width);

  part1(graph, width, height);
  part2(graph, width, height);
}
