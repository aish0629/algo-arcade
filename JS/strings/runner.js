// This file imports the functions and runs simple test calls.
// Use: node --experimental-modules runner.js  (or set "type":"module" in package.json)

import * as sm from './string_manipulation.js';

function runStringManipulationTests() {
    console.log('\n--- positive case tests ---');
  console.log('reverseString("hello") ->', sm.reverseString('hello'));
  console.log('isPalindrome("A man a plan a canal Panama") ->', sm.isPalindrome('A man a plan a canal Panama'));
  console.log('charFrequency("abbc") ->', Object.fromEntries(sm.charFrequency('abbc')));
  console.log('removeDuplicatesFromArray([1,2,2,3,"a","a"]) ->', sm.removeDuplicatesFromArray([1,2,2,3,'a','a']));
  console.log('secondLargest([5,1,5,3]) ->', sm.secondLargest([5,1,5,3]));
  console.log('isNumeric("12345") ->', sm.isNumeric('12345'));
  console.log('reverseWords("  hello   world  ") ->', sm.reverseWords('  hello   world  '));
  console.log('firstNonRepeatingChar("swiss") ->', sm.firstNonRepeatingChar('swiss'));
  console.log('sumArray([1,"2",3]) ->', sm.sumArray([1,'2',3]));
  console.log('hasDuplicates([1,2,3,1]) ->', sm.hasDuplicates([1,2,3,1]));

  // negative / edge-case tests
  console.log('\n--- negative / edge-case tests ---');
  function safeCall(fn, label, ...args) {
    try {
      const res = fn(...args);
      console.log(`${label} ->`, res);
    } catch (e) {
      console.log(`${label} -> Error:`, e && e.message ? e.message : e);
    }
  }

  safeCall(sm.reverseString, 'reverseString(null)', null);
  safeCall(sm.reverseString, 'reverseString(123)', 123);
  safeCall(sm.isPalindrome, 'isPalindrome(null)', null);
  safeCall(sm.charFrequency, 'charFrequency(null)', null);
  safeCall(sm.removeDuplicatesFromArray, 'removeDuplicatesFromArray(null)', null);
  safeCall(sm.removeDuplicatesFromArray, 'removeDuplicatesFromArray("not an array")', 'not an array');
  safeCall(sm.secondLargest, 'secondLargest([])', []);
  safeCall(sm.secondLargest, 'secondLargest([1])', [1]);
  safeCall(sm.isNumeric, 'isNumeric("12a3")', '12a3');
  safeCall(sm.reverseWords, 'reverseWords("")', '');
  safeCall(sm.firstNonRepeatingChar, 'firstNonRepeatingChar("")', '');
  safeCall(sm.sumArray, 'sumArray([1,"x",3])', [1,'x',3]);
  safeCall(sm.hasDuplicates, 'hasDuplicates(null)', null);
}

// run when executed directly
runStringManipulationTests();

export { runStringManipulationTests };