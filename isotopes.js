/**
 * @param {number} protonsStart The initial number of protons
 * @param {number} neutronsStart The initial number of neutrons
 * @param {number} protonsTarget The desired number of protons
 * @param {number} neutronsTarget The desired number of neutrons
 * @return {string[]}
 */
function solve(protonsStart, neutronsStart, protonsTarget, neutronsTarget) {
  let recipe = [];
  const proton = () => {
    currentProton += 1;
    let tempString = "PROTON";
    recipe.push(tempString);
  };

  const neutron = () => {
    currentNeutron += 1;
    let tempString = "NEUTRON";
    recipe.push(tempString);
  };

  const alpha = () => {
    currentProton -= 2;
    currentNeutron -= 2;
    let tempString = "ALPHA";
    recipe.push(tempString);
  };

  let currentProton = protonsStart;
  let currentNeutron = neutronsStart;

  while (
    !(currentProton == protonsTarget && currentNeutron == neutronsTarget)
  ) {
    if (currentProton > protonsTarget) {
      alpha();
    } else if (currentNeutron > neutronsTarget) {
      alpha();
    } else if (currentProton != protonsTarget) {
      proton();
    } else if (currentNeutron != neutronsTarget) {
      neutron();
    }
  }

  return recipe;
}

const result = solve(2, 2, 3, 3);
console.log("Result: ", result);
