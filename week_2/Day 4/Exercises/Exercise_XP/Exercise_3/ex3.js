function change_calc(coin_array, amount_due){
	let money = 0;
	money += coin_array[0]*0.25;
	money += coin_array[1]*0.1;
	money += coin_array[2]*0.05;
	money += coin_array[3]*0.01;
	if (money >= amount_due) {
		return true
	} else {
		return false
	}
}
change_calc([5, 50, 7, 10], 12.75);
change_calc([0, 1, 3, 6, 2], 12.75);
change_calc([5, 50, 7, 10], 12.75);

// Alternate solution

function changeEnough(money, total) {
	let check = 0;
	let worth = [.25, .10, .05, .01];
	for (let i = 0; i < money.length; i++) {
		check += Number(money[i])*Number(worth[i]);
	}
	if (check > total) {
		return true;
	}
	return false;
}

console.log(changeEnough([2, 100, 0, 0], 14.11));
console.log(changeEnough([0, 0, 20, 5], 0.75));
