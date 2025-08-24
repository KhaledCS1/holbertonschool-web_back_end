// Abstract building class with square footage
class Building {
  constructor(sqft) {
    // Check if subclass implements required method
    if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  // Square footage getter
  get sqft() {
    return this._sqft;
  }
}

export default Building;