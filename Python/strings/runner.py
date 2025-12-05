"""
ScenarioCaller: runs positive and negative test scenarios for string utilities.
"""
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


class ScenarioCaller:
    """Executes positive and negative test scenarios for all string utility functions."""
    
    def run(self):
        """Execute all scenarios and print results to console."""
        self.run_reverse_string_scenarios()
        self.run_is_palindrome_scenarios()
        self.run_char_frequency_scenarios()
        self.run_remove_duplicates_scenarios()
        self.run_second_largest_scenarios()
        self.run_is_numeric_scenarios()
        self.run_reverse_words_scenarios()
        self.run_first_non_repeating_char_scenarios()
        self.run_sum_array_scenarios()
        self.run_has_duplicates_scenarios()
    
    def run_reverse_string_scenarios(self):
        """Test reverse_string with positive and negative scenarios."""
        print("\n--- reverse_string ---")
        # Positive: normal string
        result = reverse_string("hello")
        print(f"positive (normal): {result!r} (expected: 'olleh')")
        
        # Positive: empty string
        result = reverse_string("")
        print(f"positive (empty): {result!r} (expected: '')")
        
        # Negative: None
        result = reverse_string(None)
        print(f"negative (None): {result!r} (expected: None)")
    
    def run_is_palindrome_scenarios(self):
        """Test is_palindrome with positive and negative scenarios."""
        print("\n--- is_palindrome ---")
        # Positive: palindrome with whitespace and case
        result = is_palindrome("A man a plan a canal Panama")
        print(f"positive (palindrome): {result} (expected: True)")
        
        # Negative: not a palindrome
        result = is_palindrome("hello")
        print(f"negative (not palindrome): {result} (expected: False)")
        
        # Negative: None
        result = is_palindrome(None)
        print(f"negative (None): {result} (expected: False)")
    
    def run_char_frequency_scenarios(self):
        """Test char_frequency with positive and negative scenarios."""
        print("\n--- char_frequency ---")
        # Positive: normal string
        result = char_frequency("abca")
        print(f"positive: {result} (expected: {{'a': 2, 'b': 1, 'c': 1}})")
        
        # Negative: None
        result = char_frequency(None)
        print(f"negative (None): {result} (expected: {{}})")
    
    def run_remove_duplicates_scenarios(self):
        """Test remove_duplicates_from_array with positive and negative scenarios."""
        print("\n--- remove_duplicates_from_array ---")
        # Positive: array with duplicates
        result = remove_duplicates_from_array(["a", "b", "a", "c"])
        print(f"positive: {result} (expected: ['a', 'b', 'c'])")
        
        # Negative: None
        result = remove_duplicates_from_array(None)
        print(f"negative (None): {result} (expected: [])")
    
    def run_second_largest_scenarios(self):
        """Test second_largest with positive and negative scenarios."""
        print("\n--- second_largest ---")
        # Positive: multiple distinct numbers
        result = second_largest([5, 1, 5, 3])
        print(f"positive: {result} (expected: 3)")
        
        # Negative: fewer than 2 elements
        result = second_largest([1])
        print(f"negative (single element): {result} (expected: None)")
        
        # Negative: None
        result = second_largest(None)
        print(f"negative (None): {result} (expected: None)")
    
    def run_is_numeric_scenarios(self):
        """Test is_numeric with positive and negative scenarios."""
        print("\n--- is_numeric ---")
        # Positive: all digits
        result = is_numeric("12345")
        print(f"positive: {result} (expected: True)")
        
        # Negative: contains non-digit
        result = is_numeric("12a3")
        print(f"negative (with letter): {result} (expected: False)")
        
        # Negative: None
        result = is_numeric(None)
        print(f"negative (None): {result} (expected: False)")
    
    def run_reverse_words_scenarios(self):
        """Test reverse_words with positive and negative scenarios."""
        print("\n--- reverse_words ---")
        # Positive: sentence with extra whitespace
        result = reverse_words("  hello   world  ")
        print(f"positive: {result!r} (expected: 'world hello')")
        
        # Negative: None
        result = reverse_words(None)
        print(f"negative (None): {result!r} (expected: None)")
    
    def run_first_non_repeating_char_scenarios(self):
        """Test first_non_repeating_char with positive and negative scenarios."""
        print("\n--- first_non_repeating_char ---")
        # Positive: string with non-repeating char
        result = first_non_repeating_char("swiss")
        print(f"positive: {result!r} (expected: 'w')")
        
        # Negative: all chars repeat
        result = first_non_repeating_char("aabbcc")
        print(f"negative (all repeat): {result!r} (expected: None)")
        
        # Negative: None
        result = first_non_repeating_char(None)
        print(f"negative (None): {result!r} (expected: None)")
    
    def run_sum_array_scenarios(self):
        """Test sum_array with positive and negative scenarios."""
        print("\n--- sum_array ---")
        # Positive: array of numbers
        result = sum_array([1.5, 2.5, 3])
        print(f"positive: {result} (expected: 7.0)")
        
        # Negative: None
        result = sum_array(None)
        print(f"negative (None): {result} (expected: 0)")
        
        # Negative: empty array
        result = sum_array([])
        print(f"negative (empty): {result} (expected: 0)")
    
    def run_has_duplicates_scenarios(self):
        """Test has_duplicates with positive and negative scenarios."""
        print("\n--- has_duplicates ---")
        # Positive: array with duplicates
        result = has_duplicates(["a", "b", "a"])
        print(f"positive (has duplicates): {result} (expected: True)")
        
        # Negative: no duplicates
        result = has_duplicates(["a", "b", "c"])
        print(f"negative (no duplicates): {result} (expected: False)")
        
        # Negative: None
        result = has_duplicates(None)
        print(f"negative (None): {result} (expected: False)")


if __name__ == "__main__":
    caller = ScenarioCaller()
    caller.run()
