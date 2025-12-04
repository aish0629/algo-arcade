package main

import (
    "reflect"
    "testing"
)

func TestReverseString(t *testing.T) {
    s := "abc"
    got := ReverseString(&s)
    if got == nil || *got != "cba" {
        t.Fatalf("ReverseString = %v, want %q", got, "cba")
    }
    if ReverseString(nil) != nil {
        t.Fatalf("ReverseString(nil) should be nil")
    }
}

func TestIsPalindrome(t *testing.T) {
    s := "A man a plan a canal Panama"
    if !IsPalindrome(&s) {
        t.Fatal("expected palindrome")
    }
    if IsPalindrome(nil) {
        t.Fatal("nil should not be palindrome")
    }
}

func TestCharFrequency(t *testing.T) {
    s := "abca"
    got := CharFrequency(&s)
    want := map[rune]int{'a': 2, 'b': 1, 'c': 1}
    if !reflect.DeepEqual(got, want) {
        t.Fatalf("got %v want %v", got, want)
    }
}

func TestRemoveDuplicatesFromArray(t *testing.T) {
    in := []string{"a", "b", "a"}
    got := RemoveDuplicatesFromArray(in)
    want := []string{"a", "b"}
    if !reflect.DeepEqual(got, want) {
        t.Fatalf("got %v want %v", got, want)
    }
}

func TestSecondLargest(t *testing.T) {
    in := []int{5, 1, 5, 3}
    got := SecondLargest(in)
    if got == nil || *got != 3 {
        t.Fatalf("SecondLargest = %v, want 3", got)
    }
    if SecondLargest([]int{1}) != nil {
        t.Fatalf("SecondLargest should be nil for single-element slice")
    }
}

func TestIsNumeric(t *testing.T) {
    s := "12345"
    if !IsNumeric(&s) {
        t.Fatal("expected numeric")
    }
    s2 := "12a3"
    if IsNumeric(&s2) {
        t.Fatal("expected non-numeric")
    }
}

func TestReverseWords(t *testing.T) {
    s := "  hello   world  "
    got := ReverseWords(&s)
    if got == nil || *got != "world hello" {
        t.Fatalf("ReverseWords = %v, want %q", got, "world hello")
    }
}

func TestFirstNonRepeatingChar(t *testing.T) {
    s := "swiss"
    got := FirstNonRepeatingChar(&s)
    if got == nil || *got != 'w' {
        t.Fatalf("FirstNonRepeatingChar = %v, want 'w'", got)
    }
}

func TestSumArray(t *testing.T) {
    got := SumArray([]float64{1.5, 2.5, 3})
    if got != 7.0 {
        t.Fatalf("SumArray = %v, want 7", got)
    }
}

func TestHasDuplicates(t *testing.T) {
    if !HasDuplicates([]string{"a", "b", "a"}) {
        t.Fatal("expected duplicates")
    }
    if HasDuplicates([]string{"a", "b", "c"}) {
        t.Fatal("expected no duplicates")
    }
}
