let startingPosition1 = 21; // failing test case
let startingRate1 = 6;

let startingPosition2 = 47;
let startingRate2 = 3;

const kangaroo = () => {

    let doesSync = false;
    let gaps = [];

    while (true) {
        startingPosition1 = startingPosition1 + startingRate1;
        startingPosition2 = startingPosition2 + startingRate2;

        if (startingPosition1 == startingPosition2) {
            doesSync = true;
            break;
        }

        gaps.push(Math.abs(startingPosition2 - startingPosition1));

        if (gaps.length == 2 && (gaps[1] - gaps[0]) >= 0) {
            break;
        }

    }

    return doesSync;
}

const result = kangaroo() ? "YES" : "NO";
console.log(result);