// Exercise 1

let userWord = prompt("type your word in here");
console.log(userWord.replace(/[aeiou]/ig,''));

// Exercise 2

let userLang = prompt("What language do you speak")

let caseLang = userLang.toLowerCase();

if (caseLang == "french"){
  console.log("Bonjour")
} else if (caseLang == "english") {
  console.log("Hello")
} else if (caseLang == "hebrew"){
  console.log("Shalom")
} else {
  console.log(":)")
}

// Exercise 3

let userGrade = parseInt(prompt("Hey! Whats your Grade?"));

if (userGrade >= 90){
  console.log("You got an 'A'!")
} else if (userGrade >= 80 && userGrade < 90) {
  console.log("You got a 'B'!");
} else if (userGrade >= 70 && userGrade < 80) {
  console.log("You got a 'C'!");
}else {
  console.log("You got a 'D'");
}

// Exercise 4

let zipCode = parseInt(prompt("Enter zip code here"));
let fiveNum = zipCode.toString().length;

if (fiveNum == 5){
  alert("Valid Zip-Code!")
} else {
  alert("Invalid Zip-Code :(")
};
