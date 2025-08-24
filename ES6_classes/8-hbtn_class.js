// Class with custom primitive conversion
class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Custom primitive conversion behavior
  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return this._size;      // Number context
    if (hint === 'string') return this._location;  // String context
    return this;
  }
}

export default HolbertonClass;