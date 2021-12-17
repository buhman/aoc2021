typedef struct vertex {
  int x;
  int y;
} vertex_t;

#define HEAP_LENGTH (100 * 100 * 5 * 5)

#define index_t int
#define priority_t int
#define value_t vertex_t

#define PARENT(_i) (index_t)(((_i) - 1U) >> 1)
#define CHILD_L(_i) (index_t)(((_i) << 1) + 1U)
#define CHILD_R(_i) (index_t)(((_i) << 1) + 2U)

typedef struct {
  priority_t priority;
  value_t value;
} node_t;

typedef struct {
  node_t tree[HEAP_LENGTH];
  index_t index;
} min_heap_t;

void min_heap_insert(min_heap_t * heap, const priority_t priority, const value_t value);
void min_heap_decrease_priority(min_heap_t * heap, const priority_t priority, const value_t value);
void min_heap_extract(min_heap_t * heap, priority_t * key, value_t * value);
