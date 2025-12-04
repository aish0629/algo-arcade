package main

import (
    "fmt"
)

// ScenarioRunner runs positive and negative test scenarios for the utilities.
type ScenarioRunner struct{}

func (r *ScenarioRunner) Run() {
    fmt.Println("--- ReverseString ---")
    pos := "hello"
    neg := (*string)(nil)
    fmt.Println("positive:", *ReverseString(&pos))
    fmt.Println("negative:", ReverseString(neg) == nil)

    fmt.Println("--- IsPalindrome ---")
    pal := "A man a plan a canal Panama"
    notpal := "hello"
    fmt.Println("positive:", IsPalindrome(&pal))
    fmt.Println("negative:", IsPalindrome(&notpal))

    fmt.Println("--- CharFrequency ---")
    s := "abca"
    fmt.Println("positive:", CharFrequency(&s))
    fmt.Println("negative (nil):", CharFrequency(nil))

    fmt.Println("--- RemoveDuplicatesFromArray ---")
    arr := []string{"a", "b", "a", "c"}
    fmt.Println("positive:", RemoveDuplicatesFromArray(arr))
    fmt.Println("negative (nil):", RemoveDuplicatesFromArray(nil))

    fmt.Println("--- SecondLargest ---")
    nums := []int{5, 1, 5, 3}
    nums2 := []int{1}
    if v := SecondLargest(nums); v != nil {
        fmt.Println("positive:", *v)
    } else {
        fmt.Println("positive: nil")
    }
    fmt.Println("negative:", SecondLargest(nums2) == nil)

    fmt.Println("--- IsNumeric ---")
    n := "12345"
    notn := "12a3"
    fmt.Println("positive:", IsNumeric(&n))
    fmt.Println("negative:", IsNumeric(&notn))

    fmt.Println("--- ReverseWords ---")
    sent := "  hello   world  "
    fmt.Println("positive:", *ReverseWords(&sent))
    fmt.Println("negative (nil):", ReverseWords(nil) == nil)

    fmt.Println("--- FirstNonRepeatingChar ---")
    f := "swiss"
    if r := FirstNonRepeatingChar(&f); r != nil {
        fmt.Printf("positive: %q\n", *r)
    } else {
        fmt.Println("positive: nil")
    }
    fmt.Println("negative (nil):", FirstNonRepeatingChar(nil) == nil)

    fmt.Println("--- SumArray ---")
    floats := []float64{1.5, 2.5, 3}
    fmt.Println("positive:", SumArray(floats))
    fmt.Println("negative (nil):", SumArray(nil))

    fmt.Println("--- HasDuplicates ---")
    dup := []string{"a", "b", "a"}
    nodup := []string{"a", "b", "c"}
    fmt.Println("positive:", HasDuplicates(dup))
    fmt.Println("negative:", HasDuplicates(nodup))
}

func main() {
    var r ScenarioRunner
    r.Run()
}
