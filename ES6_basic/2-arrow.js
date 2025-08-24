/**
 * Creates a neighborhoods list manager for San Francisco
 * Uses arrow functions to maintain proper 'this' context
 * @returns {Object} An instance with neighborhoods array and add method
 */
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  // Arrow function preserves 'this' context from parent scope
  this.addNeighborhood = (newNeighborhood) => {
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    return this.sanFranciscoNeighborhoods;
  };
}