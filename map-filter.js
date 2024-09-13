let numbers = [10,20,30,40,50]; 
let divideBy5 = numbers.map((e) => {
    return e / 5;
})
console.log(divideBy5)
//-----------------------------
let lessThan30 = numbers.filter((e) => 
    {
        return e < 30;
    }
)
console.log(lessThan30)
//-----------------------------------
let employees = [
    {name:'dravid',sal:20000},
    {name:'rohit',sal:30000},
    {name:'dhoni',sal:25000}
];
let names = employees.map((emp) => {
    return emp.name
})
console.log(names)

let filteredEmps = employees.filter((emp) => {
    return emp.sal <= 25000
})
console.log(filteredEmps)

let totalSal = employees.reduce((sum, emp) => {
    return sum + emp.sal
},0)
console.log("total salary",totalSal)