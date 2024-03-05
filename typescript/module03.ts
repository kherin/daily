interface Employee {
    name: string;
    age: number;
}

interface Manager {
    stockPlan: boolean;
}

const executive: Employee & Manager = {
    name: 'Jhon',
    age: 24,
    stockPlan: true
};

console.log(executive);
