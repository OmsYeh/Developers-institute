// Exercise 1

function checkDriver(){
  let age = prompt("What is your age?");
  if (Number(age) < 18) {
      alert("Sorry, you are too yound to drive this car. Powering off");
  } else if (Number(age) > 18) {
      alert("Powering On. Enjoy the ride!");
  } else if (Number(age) === 18) {
      alert("Congratulations on your first year of driving. Enjoy the ride!");
  }
}
function checkDriverAge(age){
  if (Number(age) < 18) {
      alert("Sorry, you are too yound to drive this car. Powering off");
  } else if (Number(age) > 18) {
      alert("Powering On. Enjoy the ride!");
  } else if (Number(age) === 18) {
      alert("Congratulations on your first year of driving. Enjoy the ride!");
  }
}
checkDriverAge(93);

// Exercise 2

amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
function checkBasket(item){
  if (amazonBasket[item] == null){
    return false;
  }
  return true;
}
console.log(checkBasket(prompt("What would you like to check?")));

// Exercise 3

function my_change(money, total) {
	let my_money = 0;
	let worth = [.25, .10, .05, .01];
	for (let i = 0; i < money.length; i++) {
		my_money += Number(money[i])*Number(worth[i]);
	}
	if (check > total) {
		return true;
	}
	return false;
}
console.log(my_change([2, 100, 0, 0], 14.11));
console.log(my_change([0, 0, 20, 5], 0.75));

// Exercise 4

let shoppingList = ["banana", "orange", "apple"];
let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}
let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}
function myBill(){
  let total = 0;
  for (let i of shoppingList) {
    if (stock[i] > 0 ){
      total += Number(prices[i]);
      stock[i]--;
    }
  }
  return total;
}
console.log(myBill());

// Exercise 5

function randomEven() {
  let rand_num = Math.floor(Math.random() * 100) + 1;
  for (let i = 0; i < rand_num; i++){
    if (i % 2 === 0){
      console.log(i);
    } else {
      continue;
    }
  }
}
randomEven();
