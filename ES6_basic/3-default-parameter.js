/**
 * Calculates the sum of an initial number with two expansion values
 * Demonstrates ES6 default parameter functionality
 * 
 * @param {number} initialNumber - The base number to start the calculation
 * @param {number} [expansion1989=89] - First expansion value (defaults to 89)
 * @param {number} [expansion2019=19] - Second expansion value (defaults to 19)
 * @returns {number} The sum of all three numbers
 * 
 * @example
 * getSumOfHoods(100); // Returns 208 (100 + 89 + 19)
 * getSumOfHoods(100, 50); // Returns 169 (100 + 50 + 19)
 * getSumOfHoods(100, 50, 30); // Returns 180 (100 + 50 + 30)
 */
export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  return initialNumber + expansion1989 + expansion2019;
}