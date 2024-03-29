interface Sundae extends IceCream {
    sauce: 'chocolate' | 'caramel' | 'strawberry';
    nuts?: boolean;
    whippedCream?: boolean;
    instructions?: boolean;
}


interface IceCreamArray {
    [index: number]: string;
}

let myIceCreamList: IceCreamArray;

myIceCreamList = ['chocolate', 'caramel', 'strawberry'];

let myStr: string = myIceCreamList[0];
console.log({ myStr });