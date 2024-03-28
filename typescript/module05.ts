interface IceCream {
    flavor: string;
    scoops: number;
};

let myIceCream: IceCream = {
    flavor: 'vanilla',
    scoops: 2
}

function tooManyScoops(dessert: IceCream) {
    if (dessert.scoops >= 4) {
        console.log("Too many scoops!");
    } else {
        console.log("That's just right!");
    }
}

console.log('Flavor: ', myIceCream.flavor);
console.log('Scoops: ', myIceCream.scoops);
console.log("Too many scoops?: ", tooManyScoops({ flavor: 'vanilla', scoops: 2 }));