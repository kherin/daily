// Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(num) {
    let initial =  num;
    let temp = 0;
    let numDecimal = Math.floor(Math.log10(num));
    if(num < 0) return false;
    while(num > 0) {
        let remainder = num % 10;
        temp += remainder * Math.pow(10, numDecimal--);
        num = num - remainder;
        num = num / 10;
  }
  return temp == initial;
};