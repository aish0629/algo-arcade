using System;
using System.Collections.Generic;
using AlgoArcade.Strings;

class Program
{
    static void Main()
    {
        Console.WriteLine("--- ReverseString ---");
        string pos = "hello";
        string? neg = null;
        Console.WriteLine($"positive: {StringUtilities.ReverseString(pos)}");
        Console.WriteLine($"negative: {StringUtilities.ReverseString(neg) == null}");

        Console.WriteLine("--- IsPalindrome ---");
        var pal = "A man a plan a canal Panama";
        var notpal = "hello";
        Console.WriteLine($"positive: {StringUtilities.IsPalindrome(pal)}");
        Console.WriteLine($"negative: {StringUtilities.IsPalindrome(notpal)}");

        Console.WriteLine("--- CharFrequency ---");
        var s = "abca";
        var freq = StringUtilities.CharFrequency(s);
        Console.WriteLine("positive: ");
        foreach (var kv in freq) Console.WriteLine($"  {kv.Key}: {kv.Value}");
        Console.WriteLine("negative (null): " + (StringUtilities.CharFrequency(null).Count == 0));

        Console.WriteLine("--- RemoveDuplicatesFromArray ---");
        var arr = new List<string>{"a","b","a","c"};
        Console.WriteLine("positive: " + string.Join(",", StringUtilities.RemoveDuplicatesFromArray(arr)));
        Console.WriteLine("negative (null): " + (StringUtilities.RemoveDuplicatesFromArray<string>(null).Count == 0));

        Console.WriteLine("--- SecondLargest ---");
        var nums = new List<int>{5,1,5,3};
        var second = StringUtilities.SecondLargest(nums);
        Console.WriteLine("positive: " + (second.HasValue ? second.Value.ToString() : "null"));
        Console.WriteLine("negative: " + (StringUtilities.SecondLargest(new List<int>{1}) == null));

        Console.WriteLine("--- IsNumeric ---");
        Console.WriteLine("positive: " + StringUtilities.IsNumeric("12345"));
        Console.WriteLine("negative: " + StringUtilities.IsNumeric("12a3"));

        Console.WriteLine("--- ReverseWords ---");
        Console.WriteLine("positive: '" + StringUtilities.ReverseWords("  hello   world  ") + "'");
        Console.WriteLine("negative (null): " + (StringUtilities.ReverseWords(null) == null));

        Console.WriteLine("--- FirstNonRepeatingChar ---");
        var f = StringUtilities.FirstNonRepeatingChar("swiss");
        Console.WriteLine("positive: " + (f.HasValue ? f.Value.ToString() : "null"));
        Console.WriteLine("negative (null): " + (StringUtilities.FirstNonRepeatingChar(null) == null));

        Console.WriteLine("--- SumArray ---");
        var floats = new List<double>{1.5,2.5,3};
        Console.WriteLine("positive: " + StringUtilities.SumArray(floats));
        Console.WriteLine("negative (null): " + StringUtilities.SumArray(null));

        Console.WriteLine("--- HasDuplicates ---");
        var dup = new List<string>{"a","b","a"};
        var nodup = new List<string>{"a","b","c"};
        Console.WriteLine("positive: " + StringUtilities.HasDuplicates(dup));
        Console.WriteLine("negative: " + StringUtilities.HasDuplicates(nodup));
    }
}
