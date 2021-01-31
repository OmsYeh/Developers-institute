// Exercise 1

const GUEST_LIST = {
  Randy: "Germany",
  Karla: "France",
  Wendy: "Japan",
  Norman: "England",
  Sam: "Argentina"
}
let student_name = prompt("Hey!, what's your name?", "Type it in here...");
if (student_name in GUEST_LIST) {
	console.log(`Hi! I'm ${student_name}, and I'm from ${GUEST_LIST[student_name]}`);
} else {
	console.log("Hi! I'm a guest.");
}
// Exercise 2

const family = {
  Kobi: 48,
  Hildie: 46,
  Omri: 23
}
console.log(Object.keys(family));
console.log(Object.values(family));

// Exercise 3
let building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent: {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}
console.log(building.number_levels);
console.log(building.number_of_apt_by_level["1"] + " and " + building.number_of_apt_by_level["3"]);
console.log(building.name_of_tenants[1] + building.number_of_rooms_and_rent["Dan"][0]);
let rent_for_sarah_david = building.number_of_rooms_and_rent["Sarah"][1] + building.number_of_rooms_and_rent["David"][1];
console.log(rent_for_sarah_david);
if (rent_for_sarah_david > building.number_of_rooms_and_rent["Dan"][1]){
  console.log(`You gotta increase ${building.name_of_tenants[1]}s rent!`);
} else {
  console.log(false);
}
building.number_of_rooms_and_rent["Dan"][1] = 2200;
console.log(building.number_of_rooms_and_rent["Dan"][1]);

// Exercise 4

let bmi_omri = {
  fullName: "Omri Yehudai",
  mass: 62,
  height: 184,
  BMI: function() {
		return this.mass / this.height^2
	}
}
let bmi_other = {
  fullName: "Jack Felix",
  mass: 80,
  height: 190,
  BMI: function() {
		return this.mass / this.height^2
	}
}
function BMI_CALC(){
  if (bmi_omri.BMI() > bmi_other.BMI()) {
	   console.log(`${bmi_omri.fullName} has a higher Body Mass Index`);
  } else {
	   console.log(`${bmi_other.fullName} has a higher Body Mass Index`);
   }
}
BMI_CALC();
