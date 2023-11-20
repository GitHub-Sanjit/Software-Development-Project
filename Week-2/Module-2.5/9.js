// Implement a function that checks whether a given string is a palindrome (reads the same backward as forward).

function isPalindrome(str) {
  // Check if the input is a string
  if (typeof str !== 'string') {
    throw new Error('Input must be a string');
  }

  // Remove non-alphanumeric characters and convert to lowercase
  const cleanedStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

  // Compare the original string with its reversed version
  return cleanedStr === cleanedStr.split('').reverse().join('');
}

// Example usage:
const testString = "A man, a plan, a canal, Panama!";
const result = isPalindrome(testString);
console.log(result); // Output: true
