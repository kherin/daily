/** 
 * Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'
*/

function firstNotRepeatingCharacter(s) {
    let sorted = s.split('').sort().join('');
    for(let val of s) {
      if(sorted.indexOf(val + val) == -1 && sorted.indexOf(val) > -1) return val;
    }
    return '_'
  }