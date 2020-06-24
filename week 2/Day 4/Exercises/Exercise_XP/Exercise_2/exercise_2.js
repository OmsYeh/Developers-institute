let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

let user_req = checkBasket();
function checkBasket(){
  let user_p = prompt('What package would you like to check?');
  if (user_p == "glasses"){
    console.log('You have ' + amazonBasket.glasses + ' in your basket');
  } else if(user_p == "books"){
    alert('You have ' + amazonBasket.books + ' in your basket');
  } else if(user_p == "floss"){
    alert('You have ' + amazonBasket.floss + ' in your basket');
  } else {
    alert("you do not have this item in your basket");
  }
}
// Alternate way

function checkBasket(item) {
	if (amazonBasket[item] == null) {
		return false;
	}
	return true;
}

console.log(checkBasket(prompt("Enter item")));
