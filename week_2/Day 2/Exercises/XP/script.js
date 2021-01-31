// Exercise 1

let x=1
let y=2

if (x<y){
  console.log(y);
} else{
  console.log("smaller number");
}
 // Exercise 2

 let newDog="Chihuahua"
 let dogLength=newDog.length;
 console.log(dogLength);
 let caps=newDog.toUpperCase();
 console.log(caps);
 let lower=newDog.toLowerCase();
 console.log(lower);

if (newDog === "Chihuahua"){
  console.log("I LOVE Chihuahua, it’s my favorite dog")
} else{
  console.log("I dont care, I prefer CATS");
}
// Exercise 3

let usrNum=prompt("Type a number here");
console.log(usrNum);
let integer=parseInt(usrNum,10);
console.log(integer);


if(integer % 2 == 0) {
  console.log(`${usrNum} IS EVEN!`)
} else {
  console.log(`${usrNum} IS NOT EVEN!`)
}
// Exercise 4

// console.log(users.length);

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];


if (users.length==0) {
  console.log("no one online")
} else if (users.length==1) {
  console.log(users[0] + " online")
} else if (users.length== 2) {
   console.log(users[0] + ' and ' + users[1] + " are online")
}else {
    console.log(users[0] + ', ' + users[1] + " and " + (users.length-2).toString() + " more online")
}
