const http = require('http');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
      if (err) return reject(Error('Cannot load the database'));

      const rows = data.split('\n').filter((l) => l.trim() !== '');
      if (rows.length === 0) {
        return resolve({ numberStudents: 'Number of students: 0\n', listStudents: [] });
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

      const all = {
        numberStudents: `Number of students: ${lines.length}\n`,
        listStudents: [],
      };
      for (const key in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, key)) {
          all.listStudents.push(`Number of students in ${key}: ${fields[key]}. List: ${students[key]}`);
        }
      }
      return resolve(all);
    });
  });
}

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') res.end('Hello Holberton School!');
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(process.argv[2])
      .then((data) => {
        res.write(data.numberStudents);
        res.write(data.listStudents.join('\n'));
        res.end();
      })
      .catch((err) => {
        res.end(err.message);
      });
  }
});

if (process.env.NODE_ENV !== 'test') {
  app.listen(port, hostname);
}

module.exports = app;