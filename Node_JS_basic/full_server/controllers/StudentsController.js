const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const dbPath = process.argv[2];
    readDatabase(dbPath)
      .then((byField) => {
        const fields = Object.keys(byField).sort();
        const lines = ['This is the list of our students'];
        for (const field of fields) {
          const list = byField[field];
          lines.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        }
        res.status(200).send(lines.join('\n'));
      })
      .catch((err) => res.status(500).send(err.message));
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }
    const dbPath = process.argv[2];
    return readDatabase(dbPath)
      .then((byField) => {
        const list = byField[major] || [];
        return res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch((err) => res.status(500).send(err.message));
  }
}

module.exports = StudentsController;
