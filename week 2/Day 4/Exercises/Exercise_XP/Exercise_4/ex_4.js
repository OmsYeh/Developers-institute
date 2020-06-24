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
