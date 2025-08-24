// Import the getBudgetObject function from the previous module
import getBudgetObject from './7-getBudgetObject';

// Creates enhanced budget object with ES6 method shorthand and spread operator
export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  
  const fullBudget = {
    ...budget,  // Spread operator copies all properties
    // ES6 method shorthand syntax
    getIncomeInDollars(income) {
      return `$${income}`;
    },
    getIncomeInEuros(income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}