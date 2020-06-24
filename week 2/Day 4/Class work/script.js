// function add_two_numbers(n,n) {
//   console.log(n + n);
// }
// add_two_numbers(5,5);


// function odd_or_even(number) {
//   if (number % 2 == 0) {
//     console.log(number + ` IS EVEN!`)
//   } else {
//     console.log(number + ` IS NOT EVEN!`)
//   }
// }
// odd_or_even();

function whats_your_age(){
  return parseInt(prompt("What is your age?"));
}
function double(number){
  return number * 2;
}
console.log("Double your age is " + double(whats_your_age()));
