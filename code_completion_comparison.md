# Task 1: GitHub Copilot vs Manual Code Completion

## 🔧 The Task  
Sort a list of dictionaries by a specific key (e.g., "age").

## ✍️ Manual Code

```python
def sort_dicts(data, key):
    return sorted(data, key=lambda x: x[key])

# Example to test
data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
print(sort_dicts(data, "age"))


🤖 Copilot Suggested Code
def sort_dicts_by_key(data, key):
    """
    Sorts a list of dictionaries based on a specific key.
    """
    if not data:
        return []
    return sorted(data, key=lambda x: x.get(key, 0))

# Example
users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
print(sort_dicts_by_key(users, "age"))



🧠 Comparison and Analysis
Both functions sort a list of dictionaries by a chosen key.

The manual version is simple and works fine for clean data. But it can break if the key is missing in any dictionary, because it directly accesses x[key].

The Copilot version adds extra safety. It uses .get(key, 0) to avoid errors if the key is missing and includes a docstring for explanation. It also checks if the input list is empty.

Summary:
Copilot is faster and adds protection against common issues, but the logic might silently do the wrong thing if you're not careful.

Manual code gives full control, but assumes you're handling errors yourself.

Final Thought:
Copilot is useful for productivity, but always review the logic before using it in real projects.