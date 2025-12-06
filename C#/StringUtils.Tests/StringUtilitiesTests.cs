using System;
using System.Collections.Generic;
using Xunit;
using AlgoArcade.Strings;

namespace AlgoArcade.Strings.Tests
{
    public class ReverseStringTests
    {
        [Fact]
        public void NormalString()
        {
            Assert.Equal("olleh", StringUtilities.ReverseString("hello"));
        }

        [Fact]
        public void EmptyString()
        {
            Assert.Equal(string.Empty, StringUtilities.ReverseString(""));
        }

        [Fact]
        public void SingleChar()
        {
            Assert.Equal("a", StringUtilities.ReverseString("a"));
        }

        [Fact]
        public void NullInput()
        {
            Assert.Null(StringUtilities.ReverseString(null));
        }
    }

    public class IsPalindromeTests
    {
        [Fact]
        public void PalindromeWithSpacesAndCase()
        {
            Assert.True(StringUtilities.IsPalindrome("A man a plan a canal Panama"));
        }

        [Fact]
        public void NotPalindrome()
        {
            Assert.False(StringUtilities.IsPalindrome("hello"));
        }

        [Fact]
        public void SingleChar()
        {
            Assert.True(StringUtilities.IsPalindrome("a"));
        }

        [Fact]
        public void EmptyString()
        {
            Assert.True(StringUtilities.IsPalindrome(""));
        }

        [Fact]
        public void NullInput()
        {
            Assert.False(StringUtilities.IsPalindrome(null));
        }
    }

    public class CharFrequencyTests
    {
        [Fact]
        public void BasicFrequency()
        {
            var got = StringUtilities.CharFrequency("abca");
            var want = new Dictionary<char,int>{{'a',2},{'b',1},{'c',1}};
            Assert.Equal(want, got);
        }

        [Fact]
        public void EmptyString()
        {
            var got = StringUtilities.CharFrequency("");
            Assert.Empty(got);
        }

        [Fact]
        public void AllSameChar()
        {
            var got = StringUtilities.CharFrequency("aaaa");
            Assert.Equal(4, got['a']);
        }

        [Fact]
        public void NullInput()
        {
            var got = StringUtilities.CharFrequency(null);
            Assert.Empty(got);
        }
    }

    public class RemoveDuplicatesTests
    {
        [Fact]
        public void WithDuplicates()
        {
            var got = StringUtilities.RemoveDuplicatesFromArray(new List<string>{"a","b","a","c"});
            Assert.Equal(new List<string>{"a","b","c"}, got);
        }

        [Fact]
        public void NoDuplicates()
        {
            var got = StringUtilities.RemoveDuplicatesFromArray(new List<string>{"a","b","c"});
            Assert.Equal(new List<string>{"a","b","c"}, got);
        }

        [Fact]
        public void EmptyArray()
        {
            var got = StringUtilities.RemoveDuplicatesFromArray(new List<string>());
            Assert.Empty(got);
        }

        [Fact]
        public void NullInput()
        {
            var got = StringUtilities.RemoveDuplicatesFromArray<string>(null);
            Assert.Empty(got);
        }

        [Fact]
        public void PreservesOrder()
        {
            var got = StringUtilities.RemoveDuplicatesFromArray(new List<int>{3,1,2,1,3,2});
            Assert.Equal(new List<int>{3,1,2}, got);
        }
    }

    public class SecondLargestTests
    {
        [Fact]
        public void MultipleDistinctNumbers()
        {
            Assert.Equal(3, StringUtilities.SecondLargest(new List<int>{5,1,5,3}));
        }

        [Fact]
        public void SingleElement()
        {
            Assert.Null(StringUtilities.SecondLargest(new List<int>{1}));
        }

        [Fact]
        public void TwoElements()
        {
            Assert.Equal(3, StringUtilities.SecondLargest(new List<int>{5,3}));
        }

        [Fact]
        public void NullInput()
        {
            Assert.Null(StringUtilities.SecondLargest(null));
        }

        [Fact]
        public void AllSameNumbers()
        {
            Assert.Null(StringUtilities.SecondLargest(new List<int>{5,5,5}));
        }
    }

    public class IsNumericTests
    {
        [Fact]
        public void AllDigits()
        {
            Assert.True(StringUtilities.IsNumeric("12345"));
        }

        [Fact]
        public void WithLetter()
        {
            Assert.False(StringUtilities.IsNumeric("12a3"));
        }

        [Fact]
        public void WithSpace()
        {
            Assert.False(StringUtilities.IsNumeric("123 45"));
        }

        [Fact]
        public void EmptyString()
        {
            Assert.False(StringUtilities.IsNumeric(""));
        }

        [Fact]
        public void NullInput()
        {
            Assert.False(StringUtilities.IsNumeric(null));
        }

        [Fact]
        public void SingleDigit()
        {
            Assert.True(StringUtilities.IsNumeric("5"));
        }
    }

    public class ReverseWordsTests
    {
        [Fact]
        public void WithExtraWhitespace()
        {
            Assert.Equal("world hello", StringUtilities.ReverseWords("  hello   world  "));
        }

        [Fact]
        public void NormalSentence()
        {
            Assert.Equal("world hello", StringUtilities.ReverseWords("hello world"));
        }

        [Fact]
        public void SingleWord()
        {
            Assert.Equal("hello", StringUtilities.ReverseWords("hello"));
        }

        [Fact]
        public void NullInput()
        {
            Assert.Null(StringUtilities.ReverseWords(null));
        }

        [Fact]
        public void EmptyString()
        {
            Assert.Equal(string.Empty, StringUtilities.ReverseWords(""));
        }
    }

    public class FirstNonRepeatingCharTests
    {
        [Fact]
        public void WithNonRepeating()
        {
            Assert.Equal('w', StringUtilities.FirstNonRepeatingChar("swiss"));
        }

        [Fact]
        public void AllRepeat()
        {
            Assert.Null(StringUtilities.FirstNonRepeatingChar("aabbcc"));
        }

        [Fact]
        public void FirstCharNonRepeating()
        {
            Assert.Equal('c', StringUtilities.FirstNonRepeatingChar("aabbc"));
        }

        [Fact]
        public void SingleChar()
        {
            Assert.Equal('a', StringUtilities.FirstNonRepeatingChar("a"));
        }

        [Fact]
        public void NullInput()
        {
            Assert.Null(StringUtilities.FirstNonRepeatingChar(null));
        }
    }

    public class SumArrayTests
    {
        [Fact]
        public void BasicSum()
        {
            Assert.Equal(7.0, StringUtilities.SumArray(new List<double>{1.5,2.5,3}));
        }

        [Fact]
        public void EmptyArray()
        {
            Assert.Equal(0, StringUtilities.SumArray(new List<double>()));
        }

        [Fact]
        public void NegativeNumbers()
        {
            Assert.Equal(2, StringUtilities.SumArray(new List<double>{1,-2,3}));
        }

        [Fact]
        public void NullInput()
        {
            Assert.Equal(0, StringUtilities.SumArray(null));
        }

        [Fact]
        public void Integers()
        {
            Assert.Equal(6, StringUtilities.SumArray(new List<double>{1,2,3}));
        }
    }

    public class HasDuplicatesTests
    {
        [Fact]
        public void WithDuplicates()
        {
            Assert.True(StringUtilities.HasDuplicates(new List<string>{"a","b","a"}));
        }

        [Fact]
        public void NoDuplicates()
        {
            Assert.False(StringUtilities.HasDuplicates(new List<string>{"a","b","c"}));
        }

        [Fact]
        public void EmptyArray()
        {
            Assert.False(StringUtilities.HasDuplicates(new List<string>()));
        }

        [Fact]
        public void NullInput()
        {
            Assert.False(StringUtilities.HasDuplicates<string>(null));
        }

        [Fact]
        public void NumericDuplicates()
        {
            Assert.True(StringUtilities.HasDuplicates(new List<int>{1,2,1}));
        }
    }
}
