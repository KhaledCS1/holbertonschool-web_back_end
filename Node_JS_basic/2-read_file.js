const fs = require('fs');

function countStudents(path) {
  try {
    const fileContent = fs.readFileSync(path, 'utf-8');
    
    const rows = fileContent.trim().split('\n');
    
    const header = rows[0].split(',');
    const studentRows = rows.slice(1).filter(row => row.trim());
    
    const firstNameIndex = header.indexOf('firstname');
    const fieldIndex = header.indexOf('field');
    
    const fieldGroups = {};
    let totalStudents = 0;
    
    studentRows.forEach(row => {
      const columns = row.split(',');
      const firstName = columns[firstNameIndex];
      const field = columns[fieldIndex];
      
      if (firstName && field) {
        if (!fieldGroups[field]) {
          fieldGroups[field] = [];
        }
        fieldGroups[field].push(firstName);
        totalStudents++;
      }
    });
    
    console.log(`Number of students: ${totalStudents}`);
    
    for (const [field, names] of Object.entries(fieldGroups)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
    
  } catch {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;