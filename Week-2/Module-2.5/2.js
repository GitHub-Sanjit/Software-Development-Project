// Create a function that finds and returns the maximum value in an array of numbers.

function findMaxValue(numbers) {
  // Check if the input is an array
  if (!Array.isArray(numbers)) {
    throw new Error("Input must be an array of numbers");
  }

  // Check if the array is not empty
  if (numbers.length === 0) {
    throw new Error("Array must not be empty");
  }

  // Use the Math.max function along with the spread operator to find the maximum value
  const max = Math.max(...numbers);

  return max;
}

// Example usage:
const numbersArray = [3, 7, 2, 8, 1, 5];
const maxValue = findMaxValue(numbersArray);
console.log(maxValue); // Output: 8
