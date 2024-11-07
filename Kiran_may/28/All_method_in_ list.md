### 1. `append(item)`
   - Adds an item to the end of the list.
   ```python
   lst = [1, 2, 3]
   lst.append(4)
   print(lst)  # Output: [1, 2, 3, 4]
   ```
### 2. `extend(iterable)`
   - Extends the list by appending elements from the iterable (e.g., another list, tuple, etc.).
   ```python
   lst = [1, 2, 3]
   lst.extend([4, 5])
   print(lst)  # Output: [1, 2, 3, 4, 5]
   ```

### 3. `insert(index, item)`
   - Inserts an item at the specified index in the list.
   
   ```python
   lst = [1, 2, 3]
   lst.insert(1, 'a')
   print(lst)  # Output: [1, 'a', 2, 3]
   ```

### 4. `remove(item)`
   - Removes the first occurrence of the specified item from the list. Raises `ValueError` if the item is not found.
   
   ```python
   lst = [1, 2, 3, 2]
   lst.remove(2)
   print(lst)  # Output: [1, 3, 2]
   ```

### 5. `pop([index])`
   - Removes and returns the item at the specified index (default is the last item).
   
   ```python
   lst = [1, 2, 3]
   item = lst.pop(1)
   print(item)  # Output: 2
   print(lst)   # Output: [1, 3]
   ```

### 6. `clear()`
   - Removes all items from the list.
   
   ```python
   lst = [1, 2, 3]
   lst.clear()
   print(lst)  # Output: []
   ```

### 7. `index(item, [start], [end])`
   - Returns the index of the first occurrence of the specified item. Raises `ValueError` if the item is not found. Optional `start` and `end` specify the range to search.
   
   ```python
   lst = [1, 2, 3, 2]
   idx = lst.index(2)
   print(idx)  # Output: 1
   ```

### 8. `count(item)`
   - Returns the number of occurrences of the specified item in the list.
   
   ```python
   lst = [1, 2, 2, 3]
   cnt = lst.count(2)
   print(cnt)  # Output: 2
   ```

### 9. `sort(key=None, reverse=False)`
   - Sorts the list in ascending order by default. The `key` argument specifies a function to be called on each list element before sorting. If `reverse=True`, the list is sorted in descending order.
   
   ```python
   lst = [3, 1, 2]
   lst.sort()
   print(lst)  # Output: [1, 2, 3]
   
   lst.sort(reverse=True)
   print(lst)  # Output: [3, 2, 1]
   ```

### 10. `reverse()`
   - Reverses the elements of the list in place.
   
   ```python
   lst = [1, 2, 3]
   lst.reverse()
   print(lst)  # Output: [3, 2, 1]
   ```

### 11. `copy()`
   - Returns a shallow copy of the list.
   
   ```python
   lst = [1, 2, 3]
   new_lst = lst.copy()
   print(new_lst)  # Output: [1, 2, 3]
   ```

### 12. `len()`
   - Returns the number of items in the list.
   
   ```python
   lst = [1, 2, 3]
   print(len(lst))  # Output: 3
   ```

### 13. `max()`
   - Returns the largest item in the list.
   
   ```python
   lst = [1, 2, 3]
   print(max(lst))  # Output: 3
   ```

### 14. `min()`
   - Returns the smallest item in the list.
   
   ```python
   lst = [1, 2, 3]
   print(min(lst))  # Output: 1
   ```

### 15. `sum()`
   - Returns the sum of all items in the list (only works for numeric types).
   
   ```python
   lst = [1, 2, 3]
   print(sum(lst))  # Output: 6
   ```

### 16. `del`
   - Deletes an element or slice from the list.
   
   ```python
   lst = [1, 2, 3]
   del lst[1]
   print(lst)  # Output: [1, 3]
   ```

### 17. `enumerate()`
   - Returns an enumerate object that contains pairs of index and value.
   
   ```python
   lst = ['a', 'b', 'c']
   for idx, val in enumerate(lst):
       print(idx, val)
   # Output: 
   # 0 a
   # 1 b
   # 2 c
   ```

### 18. `zip()`
   - Combines multiple lists into tuples.
   
   ```python
   lst1 = [1, 2, 3]
   lst2 = ['a', 'b', 'c']
   zipped = list(zip(lst1, lst2))
   print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
   ```

### 19. `filter(function, iterable)`
   - Filters the list based on the given function.
   
   ```python
   lst = [1, 2, 3, 4]
   filtered = list(filter(lambda x: x % 2 == 0, lst))
   print(filtered)  # Output: [2, 4]
   ```

### 20. `map(function, iterable)`
   - Applies the given function to all items in the list.
   
   ```python
   lst = [1, 2, 3]
   mapped = list(map(lambda x: x*2, lst))
   print(mapped)  # Output: [2, 4, 6]
   ```

These methods provide powerful ways to manipulate and work with Python lists efficiently.
