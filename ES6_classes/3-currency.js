// Currency class with code and name properties
class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  // Code getter/setter
  get code() { return this._code; }
  set code(v) {
    if (typeof v === 'string') this._code = v;
    else throw new TypeError('Code must be a string');
  }

  // Name getter/setter
  get name() { return this._name; }
  set name(v) {
    if (typeof v === 'string') this._name = v;
    else throw new TypeError('Name must be a string');
  }

  // Display full currency format
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}

export default Currency;