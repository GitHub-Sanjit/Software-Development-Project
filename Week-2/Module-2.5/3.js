// Write a function that takes an array of numbers and returns a new array containing only the even numbers.

function filterEvenNumbers(numbers) {
  // Check if the input is an array
  if (!Array.isArray(numbers)) {
    throw new Error("Input must be an array of numbers");
  }

  // Use the filter function to create a new array with only even numbers
  const evenNumbers = numbers.filter((num) => num % 2 === 0);

  return evenNumbers;
}

// Example usage:
const numbersArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const evenNumbersArray = filterEvenNumbers(numbersArray);
console.log(evenNumbersArray); // Output: [2, 4, 6, 8]
