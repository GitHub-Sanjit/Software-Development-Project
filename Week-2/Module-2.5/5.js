// Create a function that determines if a given number is prime.
// The function should return true for prime numbers and false for non - prime numbers.

function isPrime(number) {
  // Check if the input is a positive integer greater than 1
  if (typeof number !== "number" || number <= 1 || !Number.isInteger(number)) {
    throw new Error("Input must be a positive integer greater than 1");
  }

  // Check for divisibility by numbers from 2 to the square root of the given number
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      // If the number is divisible by any number in the range, it's not prime
      return false;
    }
  }

  // If the loop completes without finding a divisor, the number is prime
  return true;
}

// Example usage:
const testNumber = 17;
const isTestNumberPrime = isPrime(testNumber);
console.log(isTestNumberPrime); // Output: true
