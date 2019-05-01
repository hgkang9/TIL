// Array Helper Methods

// case 1.
//ES5
// var colors=['red', 'blue', 'green']

// for (var i = 0; i<colors.length; i++){
//     console.log(colors[i]);
// }

//ES6+ - forEach(method 이름)
const colors = ['red', 'blue', 'green']

colors.forEach(function(color){ // callback function
    console.log(color)
})

// case 2.
// ES5
// var numbers = [1,2,3]
// var doublenumbers=[]

// for (var i=0; i<numbers.length; i++){
//     doublenumbers.push(numbers[i]*2)
// }

// console.log(doublenumbers)

//ES6+ - map
const numbers = [1,2,3]
const doublenumbers=numbers.map(function(number){
    return number*2
})

console.log(doublenumbers)

// case 3.
//ES6+ - filter
const products = [
    {name:'cucumber', type:'vegetable'},
    {name:'banana', type:'fruit'},
    {name:'carrot', type:'vegetable'},
    {name:'apple', type:'fruit'},
]

const fruitproducts = products.filter(function(product){
    return product.type==='fruit'   //조건을 return(조건이 참인지 거짓인지를 return)
                                    //해당 조건이 true일 경우, item을 가져와 배열에 넣음
})

console.log(fruitproducts)

// case 4.
//ES6+ - find

const users=[
    {name:'hg'},
    {name:'admin'},
    {name:'zzuli'},
]

const founduser=users.find(function(user){
    return user.name==='admin' //조건을 return
})

console.log(founduser)

// case 5.
//ES6+ - every & some
const computers=[
    {name:'macbook', ram:16},
    {name:'gram', ram:8},
    {name:'series9', ram:32},
]

const everycomputersavailable=computers.every(function(computer){
    return computer.ram>16
})

const somecomputeravailable=computers.some(function(computer){
    return computer.ram>16
})

console.log(everycomputersavailable)
console.log(somecomputeravailable)