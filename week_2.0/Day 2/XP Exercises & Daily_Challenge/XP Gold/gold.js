// Exercise 1

let user_input = prompt("Type text", "Here");
let no_v = user_input.replace( /[aeiou]/g, '' );
 console.log(no_v);
let diff_v = user_input.replace( /[aeiou]/g, 'x' );
console.log(diff_v);

// Exercise 2

let user_lang = prompt("Whats your native language?", "Type here...");
switch (user_lang) {
  case "French":
  case "french":
    console.log("Bonjour");
    break;
  case "English":
  case "english":
    console.log("Hello");
    break;
  case "Hebrew":
  case "hebrew":
      console.log("Shalom");
      break;
  default:
  console.log(":)");
}

// Exercise 3

let grade = parseInt(prompt("Type your grade in", "here..."));
if (grade >= 90){
  console.log("A");
} else if(grade >= 80 && grade < 90){
  console.log("B");
} else if (grade >= 70 && grade < 80) {
  console.log("C");
} else if (grade <= 70){
  console.log("D");
}

// Exercise 4

let zipCode = parseInt(prompt("Put Zip Code", "Here..."));
let fiveNum = zipCode.toString().length;
if (fiveNum == 5){
  alert("Valid Zip-Code!")
} else {
  alert("Invalid Zip-Code :(")
}
