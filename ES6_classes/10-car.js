// Car class with cloning capability using Symbol.species
class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Species symbol for cloning
  static get [Symbol.species]() {
    return this;
  }

  // Clone car method
  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species(this._brand, this._motor, this._color);
  }
}

export default Car;