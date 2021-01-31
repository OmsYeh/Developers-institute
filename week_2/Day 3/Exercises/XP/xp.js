// Exercise 1

let colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink", "white"];

// for (let i = 0; i < colors.length; i++) {
//   console.log('My #' + (i + 1) + ' choice is ' + colors[i]);
// }

// ALTERNATE WAY TO EXECUTE

for (i in colors){
  console.log("My #" + (Number(i)+1) + " color is " + colors[i]);
}
for (let i = 0; i < colors.length; i++) {
  let placeNum = i + 1;
  let suffix;
  if (placeNum == 1){
    suffix = "st";
  } else if (placeNum == 2){
    suffix = "nd";
  } else if (placeNum == 3) {
    suffix = "rd";
  } else {
    suffix = "th";
  }
console.log('My ' + placeNum + suffix + ' favorite color is ' + colors[i]);
}

// Exercise 2

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let secret = "";
names.sort();
// for (let i = 0; i < names.length; i++){
//   place += names[i][0]
// }
// console.log(place);

// ALTERNA SOLUTION
for (name of names){
  secret += name.charAt(0);
}
console.log(secret);

// Exercise 3

let number = parseInt(prompt("Give me a number"));

while (number < 10){
  number = parseInt(prompt("Give me a new number"));
}
console.log(number);

// Exercise 4

let people = ["Greg", "Mary", "Devon", "James"];
for (let i = 0; i < people.length; i++){

//1
  console.log(people[i]);
}
// ALTERNATE SOLUTION
for (person of people){
  console.log(person);
}

//2
let searchItem = 'Greg';
for (let i = people.length - 1; i >= 0; i--) {
    if (people[i] === searchItem) {
        people.splice(i, 1);
        break;
    }
}
  console.log(people);
// ALTERNATE SOLUTION

people.shift();
console.log(people);

//////////////////////////////////////////////////
// 3
for (i = 0; i < people.length; i++){
    people.splice(2, 1, "Jason");
  }
    console.log(people);
//////////////////////////////////////////////////
// ALTERNATE SOLUTION

peopl[3 = "jason"]; //or
people.splice(2, 1, "Jason");
console.log(people);

//////////////////////////////////////////////////
// 4

for (i = 0; i < people.length; i++){
    people.push("Omri");
    break;
  }
    console.log(people);

// 5
for (i = 0; i < people.length; i++){
  console.log(people[0]);
}
//////////////////////////////////////////////////

for (person of people){
  console.log(person);   //<--- console.log(); over here prints bob and mary
  if (person == "Mary"){
                        //<--- console.log(); over here prints mary only
    break;
  }
                        //<--- console.log(); over here prints bob only
}

let people = ["Greg", "Mary", "Devon", "James"];
//6
let people_copy = people.slice(0, people.indexOf("Mary)")) + people.slice(people.indexOf("Mary")) + 1

//7
indexOf

//8

//9
people[people.length -1]);
