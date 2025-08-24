/**
 * Counts the number of arguments passed to the function
 * Demonstrates ES6 rest parameter (...) syntax
 * 
 * The rest parameter (...theArgs) collects all arguments into an array,
 * allowing the function to accept any number of arguments dynamically
 * 
 * @param {...*} theArgs - Rest parameter that collects all arguments into an array
 * @returns {number} The total number of arguments passed to the function
 * 
 * @example
 * returnHowManyArguments(); // Returns 0
 * returnHowManyArguments(1); // Returns 1
 * returnHowManyArguments(1, 2, 3); // Returns 3
 * returnHowManyArguments('a', 'b', 'c', 'd', 'e'); // Returns 5
 */
export default function returnHowManyArguments(...theArgs) {
  // The rest parameter (...theArgs) creates an array containing all passed arguments
  // We return the length property to count how many arguments were provided
  return theArgs.length;
}