// Write a function to calculate the factorial of a given number using loops.

function calculateFactorial(number) {
  // Check if the input is a non-negative integer
  if (typeof number !== 'number' || number < 0 || !Number.isInteger(number)) {
    throw new Error('Input must be a non-negative integer');
  }

  // Initialize the factorial variable to 1
  let factorial = 1;

  // Calculate the factorial using a loop
  for (let i = 2; i <= number; i++) {
    factorial *= i;
  }

  return factorial;
}

// Example usage:
const inputNumber = 5;
const result = calculateFactorial(inputNumber);
console.log(`The factorial of ${inputNumber} is: ${result}`); // Output: 120
