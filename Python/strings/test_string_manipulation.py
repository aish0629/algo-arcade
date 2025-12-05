"""
Unit tests for string_manipulation module.
"""
import pytest
from string_manipulation import (
    reverse_string,
    is_palindrome,
    char_frequency,
    remove_duplicates_from_array,
    second_largest,
    is_numeric,
    reverse_words,
    first_non_repeating_char,
    sum_array,
    has_duplicates,
)


class TestReverseString:
    """Tests for reverse_string function."""
    
    def test_normal_string(self):
        assert reverse_string("hello") == "olleh"
    
    def test_empty_string(self):
        assert reverse_string("") == ""
    
    def test_single_char(self):
        assert reverse_string("a") == "a"
    
    def test_none_input(self):
        assert reverse_string(None) is None


class TestIsPalindrome:
    """Tests for is_palindrome function."""
    
    def test_palindrome_with_spaces_and_case(self):
        assert is_palindrome("A man a plan a canal Panama") is True
    
    def test_not_palindrome(self):
        assert is_palindrome("hello") is False
    
    def test_single_char(self):
        assert is_palindrome("a") is True
    
    def test_empty_string(self):
        assert is_palindrome("") is True
    
    def test_none_input(self):
        assert is_palindrome(None) is False


class TestCharFrequency:
    """Tests for char_frequency function."""
    
    def test_basic_frequency(self):
        result = char_frequency("abca")
        assert result == {'a': 2, 'b': 1, 'c': 1}
    
    def test_empty_string(self):
        result = char_frequency("")
        assert result == {}
    
    def test_all_same_char(self):
        result = char_frequency("aaaa")
        assert result == {'a': 4}
    
    def test_none_input(self):
        result = char_frequency(None)
        assert result == {}


class TestRemoveDuplicates:
    """Tests for remove_duplicates_from_array function."""
    
    def test_with_duplicates(self):
        result = remove_duplicates_from_array(["a", "b", "a", "c"])
        assert result == ["a", "b", "c"]
    
    def test_no_duplicates(self):
        result = remove_duplicates_from_array(["a", "b", "c"])
        assert result == ["a", "b", "c"]
    
    def test_empty_array(self):
        result = remove_duplicates_from_array([])
        assert result == []
    
    def test_none_input(self):
        result = remove_duplicates_from_array(None)
        assert result == []
    
    def test_preserves_order(self):
        result = remove_duplicates_from_array([3, 1, 2, 1, 3, 2])
        assert result == [3, 1, 2]


class TestSecondLargest:
    """Tests for second_largest function."""
    
    def test_multiple_distinct_numbers(self):
        assert second_largest([5, 1, 5, 3]) == 3
    
    def test_single_element(self):
        assert second_largest([1]) is None
    
    def test_two_elements(self):
        assert second_largest([5, 3]) == 3
    
    def test_none_input(self):
        assert second_largest(None) is None
    
    def test_all_same_numbers(self):
        assert second_largest([5, 5, 5]) is None


class TestIsNumeric:
    """Tests for is_numeric function."""
    
    def test_all_digits(self):
        assert is_numeric("12345") is True
    
    def test_with_letter(self):
        assert is_numeric("12a3") is False
    
    def test_with_space(self):
        assert is_numeric("123 45") is False
    
    def test_empty_string(self):
        assert is_numeric("") is False
    
    def test_none_input(self):
        assert is_numeric(None) is False
    
    def test_single_digit(self):
        assert is_numeric("5") is True


class TestReverseWords:
    """Tests for reverse_words function."""
    
    def test_with_extra_whitespace(self):
        result = reverse_words("  hello   world  ")
        assert result == "world hello"
    
    def test_normal_sentence(self):
        result = reverse_words("hello world")
        assert result == "world hello"
    
    def test_single_word(self):
        result = reverse_words("hello")
        assert result == "hello"
    
    def test_none_input(self):
        assert reverse_words(None) is None
    
    def test_empty_string(self):
        result = reverse_words("")
        assert result == ""


class TestFirstNonRepeatingChar:
    """Tests for first_non_repeating_char function."""
    
    def test_with_non_repeating(self):
        assert first_non_repeating_char("swiss") == "w"
    
    def test_all_repeat(self):
        assert first_non_repeating_char("aabbcc") is None
    
    def test_first_char_non_repeating(self):
        assert first_non_repeating_char("aabbc") == "c"
    
    def test_single_char(self):
        assert first_non_repeating_char("a") == "a"
    
    def test_none_input(self):
        assert first_non_repeating_char(None) is None


class TestSumArray:
    """Tests for sum_array function."""
    
    def test_basic_sum(self):
        result = sum_array([1.5, 2.5, 3])
        assert result == 7.0
    
    def test_empty_array(self):
        assert sum_array([]) == 0
    
    def test_negative_numbers(self):
        assert sum_array([1, -2, 3]) == 2
    
    def test_none_input(self):
        assert sum_array(None) == 0
    
    def test_integers(self):
        assert sum_array([1, 2, 3]) == 6


class TestHasDuplicates:
    """Tests for has_duplicates function."""
    
    def test_with_duplicates(self):
        assert has_duplicates(["a", "b", "a"]) is True
    
    def test_no_duplicates(self):
        assert has_duplicates(["a", "b", "c"]) is False
    
    def test_empty_array(self):
        assert has_duplicates([]) is False
    
    def test_none_input(self):
        assert has_duplicates(None) is False
    
    def test_numeric_duplicates(self):
        assert has_duplicates([1, 2, 1]) is True
