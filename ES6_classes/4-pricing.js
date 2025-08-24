// Pricing class with amount and currency
import Currency from './3-currency';

class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  // Amount getter/setter with number validation
  get amount() {
    return this._amount;
  }

  set amount(amount) {
    if (typeof amount === 'number') this._amount = amount;
  }

  // Currency getter/setter with Currency instance validation
  get currency() {
    return this._currency;
  }

  set currency(currency) {
    if (currency instanceof Currency) this._currency = currency;
  }

  // Display full price format
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  // Static method for currency conversion
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}

export default Pricing;