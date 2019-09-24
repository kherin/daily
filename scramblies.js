var chai = require('chai');
var assert = chai.assert;

const scramble = (str1, str2) => {
  let isScramble = true;
  let letters = str2.split('');
  let letters1 =  str1.split('');

  for(let index = 0; index < letters.length;index++) {
    let target = letters1.indexOf(letters[index]);
    if(target == -1) {
      isScramble = false;
      break;
    }else {
      letters1[target] = undefined;
    }
  }
  return isScramble;
}



assert.equal(scramble('rkqodlw','world'),true);
assert.equal(scramble('cedewaraaossoqqyt','codewars'),true);
assert.equal(scramble('katas','steak'),false);
assert.equal(scramble('scriptjava','javascript'),true);
assert.equal(scramble('scriptingjava','javascript'),true);
assert.equal(scramble('scriptsjava','javascripts'),true);
assert.equal(scramble('jscripts','javascript'),false);
assert.equal(scramble('aabbcamaomsccdd','commas'),true);