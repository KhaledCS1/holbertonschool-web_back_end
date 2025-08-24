// Skyscraper class extending Building
import Building from './5-building';

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Call parent constructor
    this._floors = floors;
  }

  // Floors getter
  get floors() {
    return this._floors;
  }

  // Required method implementation
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}

export default SkyHighBuilding;