// Creates budget object using ES6 property shorthand
export default function getBudgetObject(income, gdp, capita) {
  // Shorthand: {income} instead of {income: income}
  const budget = {
    income,
    gdp,
    capita,
  };

  return budget;
}