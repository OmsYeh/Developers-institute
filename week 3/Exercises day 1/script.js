// let numbers = [10, 20, 30]
// --> Use 3 differents for loops to add 5 to each number
// --> console.log the Array
// --> the result is :  [15, 25, 35]

let numbers = [10, 20, 30];

for (let i = 0; i < numbers.length; i++){
  console.log(numbers[i] + 5);
}

for (let element in numbers){
  console.log(numbers[element] + 5);
}

for (let element of numbers){
  console.log(element + 5);
}
////////////////////////////
// 1
let details = {
    phoneNumber: "03574847382",
    address: "menachem begin",
    level: 2,
    rooms: ["bathroom", 'livingroom'],
    married: true
}

// 2
let details = {
    phoneNumber: "03574847382",
    address: "menachem begin",
    level: 2,
    rooms: {
      "bathroom",
      "livingroom"},
    married: true
}
// --> Use a for loop to display the name of the rooms

// 1
for(let items of details["rooms"]){
  console.log(items);
}

// 2
for (let items in details["rooms"]) {
    console.log(details["rooms"][items])
}
