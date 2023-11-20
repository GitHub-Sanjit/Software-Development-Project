// Write a function that takes two arrays as input and
// returns a new array containing elements that are common to both arrays.

function findCommonElements(array1, array2) {
  // Check if the inputs are arrays
  if (!Array.isArray(array1) || !Array.isArray(array2)) {
    throw new Error("Both inputs must be arrays");
  }

  // Use the filter method to create a new array with common elements
  const commonElements = array1.filter((element) => array2.includes(element));

  return commonElements;
}

// Example usage:
const arrayA = [1, 2, 3, 4, 5];
const arrayB = [3, 4, 5, 6, 7];
const commonElementsArray = findCommonElements(arrayA, arrayB);
console.log(commonElementsArray); // Output: [3, 4, 5]
