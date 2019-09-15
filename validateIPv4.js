function isValidIP(str) {
    let isValid = false;
    let octets = str.split('.');
    if(octets.length == 4) {
      isValid = octets.every((octet) => {
        if(octet.length > 1 && octet.startsWith('0')) return false;
        if(octet.indexOf(' ') > -1 || octet.indexOf('\n') > -1 || /[a-z]/i.test(octet)) return false;
        let octet_int = Number.parseInt(octet);
        if(Number.isNaN(octet_int)) return false;
        return octet_int >= 0 && octet_int <= 255;
      });
    }
    return isValid;
  }