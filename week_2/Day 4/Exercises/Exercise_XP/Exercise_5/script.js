let nightly_cost = 140;
let hotel = hotel_cost();

function hotel_cost() {
  let nights = parseInt(prompt("How many night would you like to stay?"));
  let price = nights * nightly_cost;
  return price;
};

let destination;
let destination_price;
function plane_ride_cost(){
  let desired_destination = prompt("Where would you like to fly to?");
 if (desired_destination == "london"){
  destination_price = 138;
} else if (desired_destination == "Paris"){
  destination_price = 220;
} else if (desired_destination == "") {
  destination_price = 300;
} else {
  prompt("Please input destination city");
} return destination_price;
}
plane_ride_cost();



// alons code

function plane_ride_cost() { //defining function to determine cost of flight
	let dest = {    //creates an object with the destinations and their pricing
		London: 183,
		Paris: 220,
		All_other_destination: 300
	}

//  note that he created the var "choose" and assigned it to prompt, so that the users input is assigned to it,-
// -but also used it to call the value of the items in the object, this is because if the user inputs a-
// -destination that matches one of the items in the object then the input will be able to call the value-
// -of the object that we want i.e the destination that the user inputed.

	let choose = prompt("Enter destination");   // here he defines a var thats assigned to the users destination input
	if (choose === 'undefined') {               // here he creates a conditional that will let activate the function again if the users first input is undefined so that the function may recieve an input that it can work with
		return plane_ride_cost();
	} else if (choose == "London") {          //if user chooses london then the value of london in the object is returned
		return dest[choose];                              // this is where the object item value is called and returned
	} else if (choose == "Paris") {           //  ^^^
		return dest[choose];                              // ^^^
	} else {             //this is for when the user did not choose london or paris
		return dest["All_other_destination"];   //  ^^^
	}
}

function rental_car_cost() {
	let days = Number(prompt("Enter how many days you wnat to rent a car"));
	if (days > 10) {
		return days*40*.95;
	}
	return days*40;
}

function total_vacation_cost() {
	return hotel_cost() + plane_ride_cost() + rental_car_cost();
}

console.log(total_vacation_cost());
