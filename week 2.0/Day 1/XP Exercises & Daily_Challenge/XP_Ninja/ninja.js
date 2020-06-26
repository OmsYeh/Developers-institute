// Exercise 1

5 >= 1  // true
0 === 1  // false
4 <= 1  // false
1 != 1  // false
"A" > "B"  // false WHY?
"B" < "C"  // true WHY?
"a" > "A"  // true
"b" < "A"  // false
true === false  //false
true != true  //false

// Exercise 2

let c;  //undefined
 let a = 34;  //a = 34
 let b = 21;  //b = 21
 a = 2;  //a is reassigned to the number 2 from its first decleration of 34
 a + b  // = 23
// What will return a + b?  = 23
// What is the variable c equal to? = undefined
// Analyse the code below without running it, what will be the output ?
console.log(3 + 4 + '5'); // output will be "75"

//Exercise 3

let user_numbers = prompt("Input your numbers here");
console.log(user_numbers);
if (user_numbers.indexOf(", ")){
  user_numbers = user_numbers.replaceAll(", ", "*")
}
console.log(user_numbers);
console.log(eval(user_numbers));

// Bonus

let usr_num = parseInt(prompt("input a number"));
let out_num;
if (usr_num < 2) {
  out_num = "boom";
} else {
  out_num = "b" + "o".repeat(usr_num) + "m"
}
if (usr_num % 2 == 0){
  out_num = out_num + "!";
}
if (usr_num % 5 == 0){
  out_num = out_num.toUpperCase();
}
console.log(out_num);
