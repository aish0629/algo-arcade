# Python String Utilities

A Python implementation of string and array manipulation utilities with comprehensive test coverage.

## Overview

This package provides 10 utility functions for string and array operations:
- `reverse_string()` - Reverse a string
- `is_palindrome()` - Check if string is a palindrome (ignores whitespace and case)
- `char_frequency()` - Get character frequency count
- `remove_duplicates_from_array()` - Remove duplicates while preserving order
- `second_largest()` - Find second largest distinct number
- `is_numeric()` - Check if string contains only digits
- `reverse_words()` - Reverse word order in a sentence
- `first_non_repeating_char()` - Find first non-repeating character
- `sum_array()` - Sum array of numbers
- `has_duplicates()` - Check if array contains duplicates

## Project Structure

```
Python/strings/
├── string_manipulation.py          # Core utility functions
├── runner.py                       # ScenarioCaller class with positive/negative scenarios
├── test_string_manipulation.py     # Unit tests (49 tests)
├── go.mod                          # (Optional) Module file for Go version
└── README.md                       # This file
```

## Dependencies

### Python Version
- **Python 3.7+** (tested with Python 3.13)

### Required Packages
- **pytest** (for running tests)
  - Install with: `pip install pytest`

### Standard Library
- `re` (regular expressions) - Built-in, no installation needed
- `typing` - Built-in, no installation needed

## Installation & Setup

### 1. Install Python
Ensure you have Python 3.7 or higher installed. Check your version:
```powershell
python --version
```

### 2. Navigate to Project Directory
```powershell
cd "d:\src\playwright\Aishwarya\Aish First Plywright\algo-arcade\Python\strings"
```

### 3. Install Dependencies
Install pytest for running the test suite:
```powershell
pip install pytest
```

Or install from a requirements file (if you create one):
```powershell
pip install -r requirements.txt
```

## Running the Code

### Option 1: Run Scenario Demonstrations
Executes positive and negative test scenarios for all functions with console output:

```powershell
python runner.py
```

**Expected Output:**
```
--- reverse_string ---
positive (normal): 'olleh' (expected: 'olleh')
positive (empty): '' (expected: '')
negative (None): None (expected: None)

--- is_palindrome ---
positive (palindrome): True (expected: True)
...
```

### Option 2: Run Unit Tests
Execute all 49 unit tests with pytest:

```powershell
python -m pytest test_string_manipulation.py -v
```

**Options:**
- `-v` - Verbose output (shows each test)
- `-q` - Quiet output (summary only)
- `-k test_name` - Run specific test by name
- `--tb=short` - Show short traceback on failures

**Example - Run only reverse_string tests:**
```powershell
python -m pytest test_string_manipulation.py -v -k "TestReverseString"
```

### Option 3: Run Tests with Coverage
Generate test coverage report:

```powershell
pip install pytest-cov
python -m pytest test_string_manipulation.py --cov=string_manipulation
```

### Option 4: Import and Use in Python
```python
from string_manipulation import reverse_string, is_palindrome, char_frequency

# Use the functions
result = reverse_string("hello")
print(result)  # Output: olleh

is_pal = is_palindrome("A man a plan a canal Panama")
print(is_pal)  # Output: True

freq = char_frequency("abca")
print(freq)  # Output: {'a': 2, 'b': 1, 'c': 1}
```

## Function Documentation

### `reverse_string(input_str: Optional[str]) -> Optional[str]`
Reverses a string. Returns None if input is None.
```python
reverse_string("hello")  # "olleh"
reverse_string(None)     # None
```

### `is_palindrome(s: Optional[str]) -> bool`
Checks if string is palindrome, ignoring whitespace and case. Returns False if input is None.
```python
is_palindrome("A man a plan a canal Panama")  # True
is_palindrome("hello")                        # False
```

### `char_frequency(s: Optional[str]) -> Dict[str, int]`
Returns dictionary with character counts. Empty dict if input is None.
```python
char_frequency("abca")  # {'a': 2, 'b': 1, 'c': 1}
char_frequency(None)    # {}
```

### `remove_duplicates_from_array(arr: Optional[List]) -> List`
Removes duplicates while preserving order. Returns empty list if input is None.
```python
remove_duplicates_from_array(["a", "b", "a"])  # ["a", "b"]
remove_duplicates_from_array(None)             # []
```

### `second_largest(arr: Optional[List[int]]) -> Optional[int]`
Finds second largest distinct number. Returns None if not found or less than 2 distinct elements.
```python
second_largest([5, 1, 5, 3])  # 3
second_largest([1])           # None
```

### `is_numeric(s: Optional[str]) -> bool`
Checks if string contains only digits (0-9). Returns False if input is None.
```python
is_numeric("12345")  # True
is_numeric("12a3")   # False
```

### `reverse_words(sentence: Optional[str]) -> Optional[str]`
Reverses word order in sentence, preserving single spaces. Returns None if input is None.
```python
reverse_words("  hello   world  ")  # "world hello"
reverse_words(None)                 # None
```

### `first_non_repeating_char(s: Optional[str]) -> Optional[str]`
Finds first character that doesn't repeat. Returns None if not found or input is None.
```python
first_non_repeating_char("swiss")  # "w"
first_non_repeating_char("aabbcc") # None
```

### `sum_array(arr: Optional[List]) -> float`
Sums array of numbers. Non-numeric entries coerced to 0. Returns 0 if input is None or empty.
```python
sum_array([1.5, 2.5, 3])  # 7.0
sum_array(None)           # 0
```

### `has_duplicates(arr: Optional[List]) -> bool`
Checks if array contains any duplicate elements. Returns False if input is None.
```python
has_duplicates(["a", "b", "a"])  # True
has_duplicates(["a", "b", "c"])  # False
```

## Test Coverage

The project includes **49 comprehensive unit tests** organized by function:
- **TestReverseString** (4 tests)
- **TestIsPalindrome** (5 tests)
- **TestCharFrequency** (4 tests)
- **TestRemoveDuplicates** (5 tests)
- **TestSecondLargest** (5 tests)
- **TestIsNumeric** (6 tests)
- **TestReverseWords** (5 tests)
- **TestFirstNonRepeatingChar** (5 tests)
- **TestSumArray** (5 tests)
- **TestHasDuplicates** (5 tests)

All tests cover:
- ✅ Positive/happy path scenarios
- ✅ Edge cases (empty strings, single elements, None values)
- ✅ Boundary conditions
- ✅ Data type handling

**Run all tests:**
```powershell
python -m pytest test_string_manipulation.py -v
```

## ScenarioCaller Class

The `ScenarioCaller` class demonstrates all functions with positive and negative scenarios:

```python
from runner import ScenarioCaller

caller = ScenarioCaller()
caller.run()  # Prints all scenario results
```

Or run directly from command line:
```powershell
python runner.py
```

## Troubleshooting

### pytest not found
```powershell
pip install pytest
```

### Import errors when running tests
Ensure you're running commands from the correct directory:
```powershell
cd "d:\src\playwright\Aishwarya\Aish First Plywright\algo-arcade\Python\strings"
python -m pytest test_string_manipulation.py -v
```

### ModuleNotFoundError when importing
Verify the Python path includes the current directory. When importing in code:
```python
import sys
sys.path.insert(0, 'd:\\src\\playwright\\Aishwarya\\Aish First Plywright\\algo-arcade\\Python\\strings')

from string_manipulation import reverse_string
```

## Creating a requirements.txt (Optional)

To make dependencies easy to install for others:

```powershell
pip freeze > requirements.txt
```

Then others can install with:
```powershell
pip install -r requirements.txt
```

**Or manually create `requirements.txt`:**
```
pytest>=9.0.0
```

## License

This project is part of algo-arcade repository.

## Related Implementations

Similar implementations also available in:
- **JavaScript** - `JS/strings/string_manipulation.js`
- **Go** - `JS/strings/GO/string_manipulation.go`
