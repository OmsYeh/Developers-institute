// Exercise 1
let me = ["my","favorite","color","is","blue"]
let joined = me.toString();
let commaless = joined.replaceAll(","," ");
console.log(commaless);

// Exercise 2

let str1 = "Hey";
let str2 = "Bye";
let first_letter1 = str1.substring(0,1);
console.log(first_letter1);
let last_letter1 = str1.substring(1,3);
console.log(last_letter1);
let first_letter2 = str2.substring(0,1);
console.log(first_letter2);
let last_letter2 = str2.substring(1,3);
console.log(last_letter2);
let new_str = first_letter1 + last_letter2 + " " + first_letter2 +last_letter1;
console.log(new_str);

// Exercise 3

let first_num = parseInt(prompt("Input first number to be calculated"));
let second_num = parseInt(prompt("Input second number to be calculated"));
let sum = alert("Your sum output is: " + (first_num + second_num));
