## Top 20 DSA Python Interview Questions

### **Arrays and Lists**

### 1. **Two Sum Problem**
```python
def two_sum(nums, target):
    """Find two numbers that add up to target"""
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Example: [2, 7, 11, 15], target = 9 → [0, 1]
```
**Concepts:** Hash Map, Array traversal **Time:** O(n) **Space:** O(n)[1][2]

---

### 2. **Maximum Subarray (Kadane's Algorithm)**
```python
def max_subarray(nums):
    """Find maximum sum of contiguous subarray"""
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example: [-2,1,-3,4,-1,2,1,-5,4] → 6
```
**Concepts:** Dynamic Programming, Greedy **Time:** O(n) **Space:** O(1)[1]

***

### 3. **Rotate Array**
```python
def rotate_array(nums, k):
    """Rotate array to right by k steps"""
    n = len(nums)
    k = k % n
    
    # Reverse entire array
    nums.reverse()
    # Reverse first k elements
    nums[:k] = reversed(nums[:k])
    # Reverse remaining elements
    nums[k:] = reversed(nums[k:])
    
    return nums

# Example: [1,2,3,4,5,6,7], k=3 → [5,6,7,1,2,3,4]
```
**Concepts:** Array manipulation, In-place reversal **Time:** O(n) **Space:** O(1)[3]

***

### 4. **Contains Duplicate**
```python
def contains_duplicate(nums):
    """Check if array contains duplicates"""
    return len(nums) != len(set(nums))
    
# Alternative approach
def contains_duplicate_v2(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```
**Concepts:** Set operations, Hash table **Time:** O(n) **Space:** O(n)[3]

---

### 5. **Product of Array Except Self**
```python
def product_except_self(nums):
    """Return array where each element is product of all others"""
    n = len(nums)
    result = [1] * n
    
    # Left products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Right products
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# Example: [1,2,3,4] → [24,12,8,6]
```
**Concepts:** Prefix/Suffix products **Time:** O(n) **Space:** O(1)[1]

---

### **Strings**

### 6. **Valid Palindrome**
```python
def is_palindrome(s):
    """Check if string is palindrome (ignore case, non-alphanumeric)"""
    # Clean string
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Two pointer approach
def is_palindrome_v2(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```
**Concepts:** Two pointers, String processing **Time:** O(n) **Space:** O(1)[4][3]

---

### 7. **Longest Substring Without Repeating Characters**
```python
def length_of_longest_substring(s):
    """Find length of longest substring without repeating chars"""
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example: "abcabcbb" → 3 ("abc")
```
**Concepts:** Sliding window, Hash set **Time:** O(n) **Space:** O(min(m,n))[5]

---

### 8. **Group Anagrams**
```python
def group_anagrams(strs):
    """Group strings that are anagrams"""
    from collections import defaultdict
    
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Sort characters as key
        key = ''.join(sorted(s))
        anagram_map[key].append(s)
    
    return list(anagram_map.values())

# Example: ["eat","tea","tan","ate","nat","bat"] 
# → [["eat","tea","ate"],["tan","nat"],["bat"]]
```
**Concepts:** Hash map, String sorting **Time:** O(n * m log m) **Space:** O(n * m)[4]

---

### **Linked Lists**

### 9. **Reverse Linked List**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    """Reverse a linked list"""
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```
**Concepts:** Linked list traversal, Pointer manipulation **Time:** O(n) **Space:** O(1)[6]

---

### 10. **Merge Two Sorted Lists**
```python
def merge_two_lists(list1, list2):
    """Merge two sorted linked lists"""
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append remaining nodes
    current.next = list1 or list2
    
    return dummy.next
```
**Concepts:** Two pointers, Linked list merging **Time:** O(n + m) **Space:** O(1)[6]

---

### **Stack and Queue**

### 11. **Valid Parentheses**
```python
def is_valid(s):
    """Check if parentheses are valid"""
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

# Example: "()[]{}" → True, "([)]" → False
```
**Concepts:** Stack, Hash map **Time:** O(n) **Space:** O(n)[7]

---

### 12. **Implement Queue using Stacks**
```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, x):
        self.in_stack.append(x)
    
    def pop(self):
        self._move()
        return self.out_stack.pop()
    
    def peek(self):
        self._move()
        return self.out_stack[-1]
    
    def empty(self):
        return not self.in_stack and not self.out_stack
    
    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```
**Concepts:** Stack operations, Amortized analysis **Time:** O(1) amortized **Space:** O(n)[7]

---

### **Trees and Binary Search**

### 13. **Maximum Depth of Binary Tree**
```python
def max_depth(root):
    """Find maximum depth of binary tree"""
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Iterative approach
def max_depth_iterative(root):
    if not root:
        return 0
    
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    
    return max_depth
```
**Concepts:** Tree traversal, Recursion, DFS **Time:** O(n) **Space:** O(h)[3]

---

### 14. **Binary Tree Level Order Traversal**
```python
def level_order(root):
    """Level order traversal of binary tree"""
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```
**Concepts:** BFS, Queue, Tree traversal **Time:** O(n) **Space:** O(w)[6]

---

### **Two Pointers**

### 15. **Container With Most Water**
```python
def max_area(height):
    """Find container that holds most water"""
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        current_water = width * min(height[left], height[right])
        max_water = max(max_water, current_water)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```
**Concepts:** Two pointers, Greedy **Time:** O(n) **Space:** O(1)[1]

---

### 16. **3Sum**
```python
def three_sum(nums):
    """Find all unique triplets that sum to zero"""
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
```
**Concepts:** Two pointers, Sorting, Duplicate handling **Time:** O(n²) **Space:** O(1)[2]

---

### **Dynamic Programming**

### 17. **Climbing Stairs**
```python
def climb_stairs(n):
    """Number of ways to climb n stairs (1 or 2 steps at a time)"""
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

# Fibonacci sequence: f(n) = f(n-1) + f(n-2)
```
**Concepts:** Dynamic Programming, Fibonacci **Time:** O(n) **Space:** O(1)[1]

---

### 18. **House Robber**
```python
def rob(nums):
    """Maximum money that can be robbed without robbing adjacent houses"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    
    return prev1
```
**Concepts:** Dynamic Programming, Optimization **Time:** O(n) **Space:** O(1)[1]

***

### **Hash Maps**

### 19. **First Unique Character**
```python
def first_uniq_char(s):
    """Find first non-repeating character in string"""
    from collections import Counter
    
    char_count = Counter(s)
    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

# Two-pass approach
def first_uniq_char_v2(s):
    char_count = {}
    
    # Count frequencies
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first unique
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1
```
**Concepts:** Hash map, String traversal **Time:** O(n) **Space:** O(1)[4]

---

### 20. **Intersection of Two Arrays**
```python
def intersection(nums1, nums2):
    """Find intersection of two arrays"""
    return list(set(nums1) & set(nums2))

# Alternative approach for counting
def intersect(nums1, nums2):
    """Find intersection with duplicates"""
    from collections import Counter
    
    count1 = Counter(nums1)
    result = []
    
    for num in nums2:
        if count1[num] > 0:
            result.append(num)
            count1[num] -= 1
    
    return result
```
**Concepts:** Set operations, Hash map **Time:** O(n + m) **Space:** O(min(n, m))[1]

---

## **Interview Tips:**

 **Yeh DSA questions master kar le:**
- **Time Complexity** analysis kar interview me
- **Space optimization** ka dhyan rakh 
- **Edge cases** handle kar (empty arrays, single elements)
- **Multiple approaches** bata (brute force → optimized)
- **Dry run** kar examples pe
-  **Practice consistently karte reh - LeetCode, GeeksforGeeks pe!**

