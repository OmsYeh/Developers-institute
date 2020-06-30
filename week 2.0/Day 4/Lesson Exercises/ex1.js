// Exercise 1

let myAge = 23;
function age_calc(myAge){
  let moms_age = (myAge *2)
  console.log(`Mom is ${moms_age} years old`);
  let dads_age = (moms_age * 1.2);
  let dad = Math.floor(dads_age);
  console.log(`Dad is ${dad} years old`);
}
age_calc(myAge);

// Exercise 2

let myAge1 = 23;
function age_calc(myAge1){
  let moms_age = (myAge1 *2)
  return moms_age;
}
age_calc(myAge1);
console.log(age_calc(myAge1));
