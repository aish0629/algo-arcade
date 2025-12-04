package main

import (
    "regexp"
    "strings"
    "unicode"
)

// ReverseString returns a new string with characters reversed.
// If input is nil, returns nil.
func ReverseString(s *string) *string {
    if s == nil {
        return nil
    }
    runes := []rune(*s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    res := string(runes)
    return &res
}

// IsPalindrome checks whether s is a palindrome ignoring whitespace and case.
// Nil input returns false.
func IsPalindrome(s *string) bool {
    if s == nil {
        return false
    }
    // remove whitespace and lower-case
    var b []rune
    for _, r := range *s {
        if unicode.IsSpace(r) {
            continue
        }
        b = append(b, unicode.ToLower(r))
    }
    for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
        if b[i] != b[j] {
            return false
        }
    }
    return true
}

// CharFrequency returns a map[rune]int with counts of each character in the string.
// Nil input returns an empty map.
func CharFrequency(s *string) map[rune]int {
    freq := make(map[rune]int)
    if s == nil {
        return freq
    }
    for _, r := range *s {
        freq[r]++
    }
    return freq
}

// RemoveDuplicatesFromArray removes duplicate strings while preserving order.
// Nil input returns an empty slice.
func RemoveDuplicatesFromArray(arr []string) []string {
    if arr == nil {
        return []string{}
    }
    seen := make(map[string]bool)
    var out []string
    for _, v := range arr {
        if !seen[v] {
            seen[v] = true
            out = append(out, v)
        }
    }
    return out
}

// SecondLargest returns a pointer to the second largest distinct number in the slice.
// Returns nil if not found.
func SecondLargest(arr []int) *int {
    if len(arr) < 2 {
        return nil
    }
    var max, second *int
    for _, v := range arr {
        if max == nil || v > *max {
            if max == nil || *max != v {
                second = max
            }
            tmp := v
            max = &tmp
        } else if v != *max && (second == nil || v > *second) {
            tmp := v
            second = &tmp
        }
    }
    return second
}

// IsNumeric returns true if the string contains only digits (0-9). Nil input -> false.
func IsNumeric(s *string) bool {
    if s == nil {
        return false
    }
    re := regexp.MustCompile(`^[0-9]+$`)
    return re.MatchString(*s)
}

// ReverseWords reverses the words in a sentence, preserving a single space between words.
// Nil input returns nil.
func ReverseWords(sentence *string) *string {
    if sentence == nil {
        return nil
    }
    fields := strings.Fields(*sentence)
    for i, j := 0, len(fields)-1; i < j; i, j = i+1, j-1 {
        fields[i], fields[j] = fields[j], fields[i]
    }
    res := strings.Join(fields, " ")
    return &res
}

// FirstNonRepeatingChar returns the first character that does not repeat, or nil if none.
func FirstNonRepeatingChar(s *string) *rune {
    if s == nil {
        return nil
    }
    count := make(map[rune]int)
    for _, r := range *s {
        count[r]++
    }
    for _, r := range *s {
        if count[r] == 1 {
            tmp := r
            return &tmp
        }
    }
    return nil
}

// SumArray sums a slice of floats. Nil slice returns 0.
func SumArray(arr []float64) float64 {
    if arr == nil {
        return 0
    }
    sum := 0.0
    for _, v := range arr {
        sum += v
    }
    return sum
}

// HasDuplicates returns true if the slice contains duplicate strings.
func HasDuplicates(arr []string) bool {
    if arr == nil {
        return false
    }
    seen := make(map[string]bool)
    for _, v := range arr {
        if seen[v] {
            return true
        }
        seen[v] = true
    }
    return false
}
