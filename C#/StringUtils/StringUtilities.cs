#nullable enable
using System;
using System.Collections.Generic;
using System.Linq;

namespace AlgoArcade.Strings
{
    public static class StringUtilities
    {
        // Reverse a string. Null -> null
        public static string? ReverseString(string? input)
        {
            if (input is null) return null;
            var chars = input.ToCharArray();
            Array.Reverse(chars);
            return new string(chars);
        }

        // Check palindrome ignoring whitespace and case. Null -> false
        public static bool IsPalindrome(string? s)
        {
            if (s is null) return false;
            var cleaned = new string(s.Where(c => !char.IsWhiteSpace(c)).ToArray()).ToLowerInvariant();
            return cleaned.SequenceEqual(cleaned.Reverse());
        }

        // Character frequency
        public static Dictionary<char,int> CharFrequency(string? s)
        {
            var freq = new Dictionary<char,int>();
            if (s is null) return freq;
            foreach (var ch in s)
            {
                if (freq.ContainsKey(ch)) freq[ch]++;
                else freq[ch] = 1;
            }
            return freq;
        }

        // Remove duplicates preserving order
        public static List<T> RemoveDuplicatesFromArray<T>(IEnumerable<T>? arr)
        {
            if (arr is null) return new List<T>();
            var seen = new HashSet<T>();
            var outList = new List<T>();
            foreach (var v in arr)
            {
                if (seen.Add(v)) outList.Add(v);
            }
            return outList;
        }

        // Second largest distinct number. Null or not found -> null
        public static int? SecondLargest(IEnumerable<int>? arr)
        {
            if (arr is null) return null;
            var distinct = arr.Distinct().ToList();
            if (distinct.Count < 2) return null;
            distinct.Sort();
            return distinct[distinct.Count - 2];
        }

        // IsNumeric: only digits 0-9
        public static bool IsNumeric(string? s)
        {
            if (s is null) return false;
            if (s.Length == 0) return false;
            return s.All(char.IsDigit);
        }

        // Reverse words in sentence, preserving single space between words. Null -> null
        public static string? ReverseWords(string? sentence)
        {
            if (sentence is null) return null;
            var words = sentence.Split((char[])null, StringSplitOptions.RemoveEmptyEntries);
            Array.Reverse(words);
            return string.Join(' ', words);
        }

        // First non-repeating character. Null -> null
        public static char? FirstNonRepeatingChar(string? s)
        {
            if (s is null) return null;
            var counts = new Dictionary<char,int>();
            foreach (var ch in s) counts[ch] = counts.GetValueOrDefault(ch) + 1;
            foreach (var ch in s) if (counts[ch] == 1) return ch;
            return null;
        }

        // Sum array of doubles. Null -> 0
        public static double SumArray(IEnumerable<double>? arr)
        {
            if (arr is null) return 0;
            return arr.Sum();
        }

        // Has duplicates
        public static bool HasDuplicates<T>(IEnumerable<T>? arr)
        {
            if (arr is null) return false;
            var set = new HashSet<T>();
            foreach (var v in arr)
            {
                if (!set.Add(v)) return true;
            }
            return false;
        }
    }
}
