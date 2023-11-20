// Write a function that takes an array of numbers as input and returns the sum of all the elements.

function sumArray(numbers) {
  // Check if the input is an array
  if (!Array.isArray(numbers)) {
    throw new Error("Input must be an array of numbers");
  }

  // Use the reduce function to calculate the sum
  const sum = numbers.reduce((acc, num) => acc + num, 0);

  return sum;
}

// Example usage:
const numbersArray = [1, 2, 3, 4, 5];
const result = sumArray(numbersArray);
console.log(result); // Output: 15
