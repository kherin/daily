/*Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
*
*/

const countSmileys = (arr) => {
    let count = 0;
    arr.forEach((val) => {
      if(/^[:|;]{1}[-~]{0,1}[D\)]{1}$/.test(val)){
        count++;
      }
    });
    return count;
  }
  
  console.log(countSmileys([':)', ';(', ';}', ':-D']) == 2);
  console.log(countSmileys([';D', ':-(', ':-)', ';~)']) == 3);
  console.log(countSmileys([';]', ':[', ';*', ':$', ';-D']) == 1);
  console.log(countSmileys([';(', ':>', ':}', ':]']) == 0);
  
  
  
  