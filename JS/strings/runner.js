// This file imports the functions and runs simple test calls.
// Use: node --experimental-modules runner.js  (or set "type":"module" in package.json)

import * as sm from './string_manipulation.js';

function runStringManipulationTests() {
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
}

// run when executed directly
runStringManipulationTests();

export { runStringManipulationTests };