// Exercise 1

let x = 5;
let y = 6;

if (x > y){
  console.log(x);
} else {
  console.log(y);
}

// Exercise 2

let newDog = "Chihuahua";
let length = newDog.length;
console.log(length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog === "Chihuahua"){
  console.log("I LOVE Chihuahua, it’s my favorite dog");
} else{
  console.log("I dont care, I prefer CATS");
}

// Exercise 3

let variable = Number(prompt("Input number", "Here!"));
let output;
if (variable % 2 == 0){
  output = variable + " is an even number";
} else {
  output = variable + " is not an even number";
}
console.log(alert(output));

// Exercise 4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
if (users.length === 0){
  console.log(users[0] + " is online");
} else if (users.length === 1) {
  console.log(users[0] + " " + users[1] + " are online");
} else if (users.length > 2){
  console.log(users[0] + " " + users[1] + " and " + users.length + " more online");
} else {
  console.log("No one is online");
}
