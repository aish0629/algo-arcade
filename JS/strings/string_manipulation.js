// ...existing code...
/**
 * Reverse a string.
 * @param {string|null|undefined} input
 * @returns {string|null}
 */
function reverseString(input) {
  if (input == null) return null;
  return String(input).split('').reverse().join('');
}

/**
 * Check if a string is a palindrome (ignores whitespace and case).
 * @param {string|null|undefined} s
 * @returns {boolean}
 */
function isPalindrome(s) {
  if (s == null) return false;
  const clean = String(s).replace(/\s+/g, '').toLowerCase();
  return clean === clean.split('').reverse().join('');
}

/**
 * Character frequency in a string — returns a Map<char, count>.
 * @param {string|null|undefined} s
 * @returns {Map<string, number>}
 */
function charFrequency(s) {
  const freq = new Map();
  if (s == null) return freq;
  for (const ch of String(s)) {
    freq.set(ch, (freq.get(ch) || 0) + 1);
  }
  return freq;
}

/**
 * Remove duplicates from array while preserving order.
 * @param {Array|null|undefined} arr
 * @returns {Array}
 */
function removeDuplicatesFromArray(arr) {
  if (arr == null) return [];
  return Array.from(new Set(arr));
}

/**
 * Find the second largest distinct number in an array.
 * Returns null if there isn't one.
 * @param {number[]|null|undefined} arr
 * @returns {number|null}
 */
function secondLargest(arr) {
  if (!Array.isArray(arr) || arr.length < 2) return null;
  let max = -Infinity;
  let second = -Infinity;
  for (const n of arr) {
    if (typeof n !== 'number' || Number.isNaN(n)) continue;
    if (n > max) {
      second = max;
      max = n;
    } else if (n < max && n > second) {
      second = n;
    }
  }
  return second === -Infinity ? null : second;
}

/**
 * Check if a string contains only digits.
 * @param {string|null|undefined} s
 * @returns {boolean}
 */
function isNumeric(s) {
  if (s == null) return false;
  return /^[0-9]+$/.test(String(s));
}

/**
 * Reverse the words in a sentence (preserve single spaces between words).
 * @param {string|null|undefined} sentence
 * @returns {string|null}
 */
function reverseWords(sentence) {
  if (sentence == null) return null;
  return String(sentence).trim().split(/\s+/).reverse().join(' ');
}

/**
 * First non-repeating character in a string. Returns the character or null.
 * @param {string|null|undefined} s
 * @returns {string|null}
 */
function firstNonRepeatingChar(s) {
  if (s == null) return null;
  const count = new Map();
  for (const ch of String(s)) {
    count.set(ch, (count.get(ch) || 0) + 1);
  }
  for (const ch of String(s)) {
    if (count.get(ch) === 1) return ch;
  }
  return null;
}

/**
 * Sum array using reduce. Non-number entries are coerced by +
 * @param {number[]|null|undefined} arr
 * @returns {number}
 */
function sumArray(arr) {
  if (!Array.isArray(arr)) return 0;
  return arr.reduce((acc, v) => acc + (typeof v === 'number' ? v : Number(v) || 0), 0);
}

/**
 * Check if array contains duplicates.
 * @param {Array|null|undefined} arr
 * @returns {boolean}
 */
function hasDuplicates(arr) {
  if (!Array.isArray(arr)) return false;
  const seen = new Set();
  for (const v of arr) {
    if (seen.has(v)) return true;
    seen.add(v);
  }
  return false;
}

module.exports = {
  reverseString,
  isPalindrome,
  charFrequency,
  removeDuplicatesFromArray,
  secondLargest,
  isNumeric,
  reverseWords,
  firstNonRepeatingChar,
  sumArray,
  hasDuplicates,
};