"""
String and array utility functions.
Mirrors JS implementations with None handling where applicable.
"""
from typing import Optional, List, Dict, Set
import re


def reverse_string(input_str: Optional[str]) -> Optional[str]:
    """
    Reverse a string.
    
    Args:
        input_str: string or None
    
    Returns:
        reversed string or None if input is None
    """
    if input_str is None:
        return None
    return input_str[::-1]


def is_palindrome(s: Optional[str]) -> bool:
    """
    Check if a string is a palindrome (ignores whitespace and case).
    
    Args:
        s: string or None
    
    Returns:
        True if palindrome, False otherwise (None returns False)
    """
    if s is None:
        return False
    clean = re.sub(r'\s+', '', s).lower()
    return clean == clean[::-1]


def char_frequency(s: Optional[str]) -> Dict[str, int]:
    """
    Return character frequency count in a string.
    
    Args:
        s: string or None
    
    Returns:
        Dict with character -> count mapping
    """
    freq = {}
    if s is None:
        return freq
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


def remove_duplicates_from_array(arr: Optional[List]) -> List:
    """
    Remove duplicates from array while preserving order.
    
    Args:
        arr: list or None
    
    Returns:
        list with duplicates removed
    """
    if arr is None:
        return []
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def second_largest(arr: Optional[List[int]]) -> Optional[int]:
    """
    Find the second largest distinct number in an array.
    
    Args:
        arr: list of numbers or None
    
    Returns:
        second largest number or None if not found
    """
    if not isinstance(arr, list) or len(arr) < 2:
        return None
    
    distinct = list(set(arr))
    if len(distinct) < 2:
        return None
    
    distinct.sort(reverse=True)
    return distinct[1]


def is_numeric(s: Optional[str]) -> bool:
    """
    Check if a string contains only digits.
    
    Args:
        s: string or None
    
    Returns:
        True if all characters are digits, False otherwise
    """
    if s is None:
        return False
    return bool(re.match(r'^[0-9]+$', s))


def reverse_words(sentence: Optional[str]) -> Optional[str]:
    """
    Reverse the words in a sentence (preserve single spaces between words).
    
    Args:
        sentence: string or None
    
    Returns:
        string with reversed word order or None if input is None
    """
    if sentence is None:
        return None
    words = sentence.strip().split()
    return ' '.join(reversed(words))


def first_non_repeating_char(s: Optional[str]) -> Optional[str]:
    """
    Find the first non-repeating character in a string.
    
    Args:
        s: string or None
    
    Returns:
        first non-repeating character or None if not found
    """
    if s is None:
        return None
    
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    
    for ch in s:
        if count[ch] == 1:
            return ch
    
    return None


def sum_array(arr: Optional[List]) -> float:
    """
    Sum array of numbers. Non-numeric entries are coerced to 0.
    
    Args:
        arr: list of numbers or None
    
    Returns:
        sum of array elements, 0 if None or empty
    """
    if not isinstance(arr, list):
        return 0
    
    total = 0.0
    for v in arr:
        try:
            total += float(v) if isinstance(v, (int, float)) else 0
        except (ValueError, TypeError):
            pass
    return total


def has_duplicates(arr: Optional[List]) -> bool:
    """
    Check if array contains duplicate elements.
    
    Args:
        arr: list or None
    
    Returns:
        True if duplicates found, False otherwise
    """
    if not isinstance(arr, list):
        return False
    return len(arr) != len(set(arr))
