//Write a function that takes an array as input and returns a new array with duplicate elements removed.

function removeDuplicates(inputArray) {
  // Check if the input is an array
  if (!Array.isArray(inputArray)) {
    throw new Error("Input must be an array");
  }

  // Use a Set to store unique values and then convert it back to an array
  const uniqueArray = [...new Set(inputArray)];

  return uniqueArray;
}

// Example usage:
const arrayWithDuplicates = [1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 3];
const arrayWithoutDuplicates = removeDuplicates(arrayWithDuplicates);
console.log(arrayWithoutDuplicates); // Output: [1, 2, 3, 4, 5, 6, 7, 8]
