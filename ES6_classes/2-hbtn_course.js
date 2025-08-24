// Course class with getters and setters validation
class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // Name getter/setter with string validation
  get name() { return this._name; }
  set name(v) {
    if (typeof v !== 'string') throw new TypeError('Name must be a string');
    this._name = v;
  }

  // Length getter/setter with number validation
  get length() { return this._length; }
  set length(v) {
    if (typeof v !== 'number') throw new TypeError('Length must be a number');
    this._length = v;
  }

  // Students getter/setter with array validation
  get students() { return this._students; }
  set students(v) {
    if (!Array.isArray(v) || !v.every((s) => typeof s === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = v;
  }
}

export default HolbertonCourse;