/**
 * Adds two or more numbers together.
 * @param {...number} numbers - The numbers to add.
 * @returns {number} The sum of all provided numbers.
 */
function addNumbers(...numbers) {
  return numbers.reduce((sum, num) => sum + num, 0);
}

module.exports = { addNumbers };
