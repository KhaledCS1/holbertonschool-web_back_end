const fs = require('fs');

/**
 * Reads the database CSV and returns a map of field -> array of firstnames.
 * @param {string} filePath
 * @returns {Promise<Record<string, string[]>>}
 */
function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
      if (err) return reject(new Error('Cannot load the database'));

      const rows = data.split('\n').filter((l) => l.trim() !== '');
      if (rows.length <= 1) return resolve({});

      const header = rows[0].split(',');
      const idxFn = header.findIndex((h) => h === 'firstname');
      const idxFd = header.findIndex((h) => h === 'field');

      const byField = {};
      for (const row of rows.slice(1)) {
        const cols = row.split(',');
        const field = cols[idxFd];
        const firstname = cols[idxFn];
        if (!field || !firstname) continue;
        if (!byField[field]) byField[field] = [];
        byField[field].push(firstname);
      }

      resolve(byField);
    });
  });
}

module.exports = readDatabase;
