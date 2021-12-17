#include <assert.h>

#include "min_heap.h"

#define _HEAP_UP \
  while (ix != 0) { \
    index_t parent_ix = PARENT(ix); \
    if (heap->tree[ix].priority > heap->tree[parent_ix].priority) \
      break; \
    \
    node_t tmp = heap->tree[ix]; \
    heap->tree[ix] = heap->tree[parent_ix]; \
    heap->tree[parent_ix] = tmp; \
    ix = parent_ix; \
  }

void min_heap_insert(min_heap_t * heap, const priority_t priority, const value_t value)
{
  assert(heap->index < HEAP_LENGTH);

  index_t ix = heap->index;
  heap->tree[heap->index++] = (node_t){priority, value};

  _HEAP_UP
}

void min_heap_decrease_priority(min_heap_t * heap, const priority_t priority, const value_t value)
{
  index_t ix;

  for (ix = 0; ix < heap->index; ix++) {
    if (heap->tree[ix].value.x == value.x && heap->tree[ix].value.y == value.y)
      break;
  }

  if (ix == heap->index) {
    assert(0);
  }

  assert(priority < heap->tree[ix].priority);
  heap->tree[ix].priority = priority;

  _HEAP_UP
}

void min_heap_extract(min_heap_t * heap, priority_t * priority, value_t * value)
{
  index_t ix = 0;
  *value = heap->tree[ix].value;
  *priority = heap->tree[ix].priority;

  if (heap->index == 0)
    return;

  heap->tree[ix] = heap->tree[--heap->index];

  while (1) {
    index_t swap_ix = CHILD_L(ix);
    if (swap_ix >= heap->index)
      break;
    index_t child_r_ix = CHILD_R(ix);
    if ((child_r_ix < heap->index) && (heap->tree[child_r_ix].priority < heap->tree[swap_ix].priority))
      swap_ix = child_r_ix;

    if (heap->tree[swap_ix].priority > heap->tree[ix].priority)
      break;

    node_t tmp = heap->tree[ix];
    heap->tree[ix] = heap->tree[swap_ix];
    heap->tree[swap_ix] = tmp;
    ix = swap_ix;
  }
}
