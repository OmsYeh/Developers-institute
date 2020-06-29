// Exercise 1 : Your favorite colors

let color = ["blue", "green", "brown", "yellow", "red"];

for (i in color){
  console.log("My #" + (Number(i)+1) + " color is " + color[i]);
}
for (let i = 0; i < color.length; i++) {
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
console.log('My ' + placeNum + suffix + ' favorite color is ' + color[i]);
}

// Exercise 2 : Secret Group

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let secret = "";
let sorted_names = names.sort();
for (let i in sorted_names){
  secret += sorted_names[i][0];
}
console.log(secret);

// Exercise 3

let usrNum = Number(prompt("Type a number in", "Here"));
if (usrNum < 10){
  console.log(Number(prompt("Type another number in", "Here")));
}

// Exercise 4

let people = ["Greg", "Mary", "Devon", "James"];
for (i in people){
  console.log(people[i]);
}
people.shift();
people.splice(2,1,"Jason");
people.push("Omri")
console.log(people);
for (person of people){
  console.log(person);
  if (person == "Mary"){
    break;
  }
}
let newArr = people.splice(1,2);
console.log(newArr);
let wheres_mary = people.indexOf("Mary");
console.log(wheres_mary);
let wheres_foo = people.indexOf("Foo");
console.log(wheres_foo);
let last = people.pop();
console.log(last);

// Exercise 5

let age = [20,5,12,43,98,55];
let sum = 0;
for(let i in age){
   sum += age[i];
 }
console.log(sum);
for (let i in age){
  if (age[i] % 2 === 0){
  console.log(age[i]);
  }
}
let largest = Math.max.apply(Math, age);
console.log(largest);
