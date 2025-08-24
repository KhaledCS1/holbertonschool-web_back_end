// Helper function - returns current year
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

// Creates budget object with year-specific property names using ES6 computed properties
export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {
    [`income-${getCurrentYear()}`]: income,   // 'income-2025'
    [`gdp-${getCurrentYear()}`]: gdp,         // 'gdp-2025'
    [`capita-${getCurrentYear()}`]: capita,   // 'capita-2025'
  };

  return budget;
}