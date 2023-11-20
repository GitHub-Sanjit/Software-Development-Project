// Implement a function that reverses a given string using loops.

function reverseString(str) {
  // Check if the input is a string
  if (typeof str !== "string") {
    throw new Error("Input must be a string");
  }

  // Initialize an empty string to store the reversed version
  let reversedString = "";

  // Iterate through the string in reverse order and build the reversed string
  for (let i = str.length - 1; i >= 0; i--) {
    reversedString += str[i];
  }

  return reversedString;
}

// Example usage:
const originalString = "Hello, World!";
const reversedString = reverseString(originalString);
console.log(reversedString); // Output: '!dlroW ,olleH'
