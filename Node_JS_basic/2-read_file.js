const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    const data = fs.readFileSync(path, { encoding: 'utf-8' });
    const rows = data.split('\n').filter((l) => l.trim() !== '');
    if (rows.length === 0) {
      console.log('Number of students: 0');
      return;
    }

    const header = rows[0].split(',');
    const idxFn = header.findIndex((h) => h === 'firstname');
    const idxFd = header.findIndex((h) => h === 'field');

    const lines = rows.slice(1);
    const fields = {};
    const students = {};
    let validStudentCount = 0;

    for (const line of lines) {
      const cols = line.split(',');
      const field = cols[idxFd];
      const firstname = cols[idxFn];
      if (!field || !firstname) continue;
      validStudentCount += 1;
      fields[field] = (fields[field] || 0) + 1;
      students[field] = students[field] ? `${students[field]}, ${firstname}` : firstname;
    }

    console.log(`Number of students: ${validStudentCount}`);
    for (const key in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, key)) {
        const count = fields[key];
        console.log(`Number of students in ${key}: ${count}. List: ${students[key]}`);
      }
    }
  } catch {
    throw new Error('Cannot load the database');
  }
};
