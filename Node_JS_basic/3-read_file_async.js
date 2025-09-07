const fs = require('fs');

module.exports = function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
      if (err) return reject(Error('Cannot load the database'));

      const rows = data.split('\n').filter((l) => l.trim() !== '');
      if (rows.length === 0) {
        console.log('Number of students: 0');
        return resolve();
      }

      const header = rows[0].split(',');
      const idxFn = header.findIndex((h) => h === 'firstname');
      const idxFd = header.findIndex((h) => h === 'field');

      const lines = rows.slice(1);
      const fields = {};
      const students = {};

      for (const line of lines) {
        const cols = line.split(',');
        const field = cols[idxFd];
        const firstname = cols[idxFn];
        if (!field || !firstname) continue;
        fields[field] = (fields[field] || 0) + 1;
        students[field] = students[field] ? `${students[field]}, ${firstname}` : firstname;
      }

      console.log(`Number of students: ${lines.length}`);
      for (const key in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, key)) {
          const count = fields[key];
          console.log(`Number of students in ${key}: ${count}. List: ${students[key]}`);
        }
      }
      return resolve();
    });
  });
};