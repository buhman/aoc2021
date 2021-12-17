#include <stddef.h>

#include "min_heap.h"

#define NEIGHBORS_LENGTH 4
static const vertex_t neighbors[NEIGHBORS_LENGTH] = {
  {-1,  0},
  { 1,  0},
  { 0, -1},
  { 0,  1},
};

void dijkstra(const int * graph,
              const int width, const int height,
              const int tile_width, const int tile_height,
              const vertex_t source,
              vertex_t * previous)
{
  int distance[width * height];
  distance[source.y * width + source.x] = 0;

  min_heap_t priority_queue;
  priority_queue.index = 0;

  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      if (!(y == source.y && x == source.x)) {
        distance[y * width + x] = 0x7fffffff;
        previous[y * width + x] = (vertex_t){0x7fffffff, 0x7fffffff};
      }

      min_heap_insert(&priority_queue, distance[y * width + x], (vertex_t){x, y});
    }
  }

  while (priority_queue.index != 0) {
    priority_t u_priority;
    vertex_t u_vertex;
    min_heap_extract(&priority_queue, &u_priority, &u_vertex);

    for (int i = 0; i < NEIGHBORS_LENGTH; i++) {
      vertex_t n_vertex = (vertex_t){
        u_vertex.x + neighbors[i].x,
        u_vertex.y + neighbors[i].y
      };

      if (n_vertex.x < 0 || n_vertex.y < 0)
        continue;
      if (n_vertex.x > (width - 1) || n_vertex.y > (height - 1))
        continue;

      ptrdiff_t ix_u = u_vertex.y * width + u_vertex.x;
      ptrdiff_t graph_u = (u_vertex.y % tile_height) * tile_width + (u_vertex.x % tile_width);
      ptrdiff_t graph_offset = u_vertex.y / tile_height + u_vertex.x / tile_width;

      int risk = graph[graph_u] + graph_offset;
      while (risk > 9)
        risk = risk - 9;

      ptrdiff_t ix_n = n_vertex.y * width + n_vertex.x;
      int alt_distance = distance[ix_u] + risk;
      if (alt_distance < distance[ix_n]) {
        distance[ix_n] = alt_distance;
        previous[ix_n] = u_vertex;
        min_heap_decrease_priority(&priority_queue, alt_distance, n_vertex);
      }
    }
  }
}
