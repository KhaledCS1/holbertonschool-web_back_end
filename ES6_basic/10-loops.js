// Uses ES6 for...of loop to iterate through array
export default function appendToEachArrayValue(array, appendString) {
  const arr = [];
  // for...of loops through array values directly
  for (const value of array) {
    arr.push(appendString + value);
  }

  return arr;
}