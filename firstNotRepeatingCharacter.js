/** 
 * Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'
*/

function firstNotRepeatingCharacter(s) {
    let alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
    let sorted = s.split('').sort().join('');
    for(let val of s) {
      if(sorted.indexOf(val + val) == -1 && sorted.indexOf(val) > -1) return val;
    }
    return '_'
  }