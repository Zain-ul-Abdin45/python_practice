from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
print(counts)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})

# Applications:

# Counting occurrences of elements in a list, tuple, or string.
# Finding the most common elements.
# Performing set-like operations on counts (e.g., finding intersections or unions of counted elements).
# Common Use Cases:

# Word frequency analysis in text processing.
# Inventory management (where counting the number of each item is needed).
# Histogram data.


from collections import deque
d = deque([1, 2, 3, 4])
d.appendleft(0)  # deque([0, 1, 2, 3, 4])
d.pop()          # deque([0, 1, 2, 3])



# Applications:

# Implementing efficient queues and stacks.
# Maintaining a history of recent events (like browser history).
# Sliding window algorithms (useful in data stream processing).
# Common Use Cases:

# Breadth-first search (BFS) in graph algorithms.
# Real-time event or task queues.
# Maintaining recent logs in a fixed-size deque.



from collections import defaultdict
dd = defaultdict(int)  # Default value is 0 for missing keys
dd['a'] += 1  # Output: defaultdict(<class 'int'>, {'a': 1})


# Applications:

# Counting items without checking for key existence.
# Grouping items or building data structures dynamically (e.g., lists, sets).
# Simplifying nested dictionary structures where missing keys might occur.
# Common Use Cases:

# Counting words or objects (works like Counter but more flexible).
# Creating adjacency lists for graphs.
# Aggregating data where you need to group values under keys (e.g., categorizing data).


from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od.move_to_end('a')  # Moves 'a' to the end
print(od)  # Output: OrderedDict([('b', 2), ('a', 1)])



# Applications:

# Keeping track of the insertion order of elements.
# Implementing LRU (Least Recently Used) caches, where you can reorder and discard elements efficiently.
# Creating structures where both element order and fast lookups are essential.
# Common Use Cases:

# Implementing priority queues or LRU caches.
# Maintaining sorted elements based on insertion order.
# Working with datasets where order matters (e.g., logs or sequences of events).


from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x)  # Output: 10


# Applications:

# Creating lightweight, immutable objects with named attributes.
# Replacing dictionaries or classes when you need minimal and immutable data structures.
# Organizing data with descriptive field names instead of relying on index-based access (like tuples).
# Common Use Cases:

# Storing coordinate points, vectors, or records (e.g., x, y positions).
# Returning multiple values from functions with descriptive names.
# Representing immutable data records in a clear, concise way.


from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(chain['b'])  # Output: 2 (from dict1, since it comes first)


# Applications:

# Merging multiple dictionaries without creating a new copy.
# Layering configurations (e.g., defaults, environment variables, user overrides).
# Accessing multiple scopes of variables in a single lookup.
# Common Use Cases:

# Combining environment variables with default settings.
# Layering different levels of configurations or settings in applications.
# Avoiding deep copies when merging dictionaries.


from collections import UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

my_dict = MyDict()
my_dict['a'] = 3
print(my_dict)  # Output: {'a': 6}



# Applications:

# Extending and customizing dictionary, list, or string behavior.
# Providing additional functionality while still using these core data types.
# Common Use Cases:

# Adding validation, logging, or transformations when elements are added or accessed in lists/dictionaries.
# Creating domain-specific versions of common types (e.g., a case-insensitive dictionary).
