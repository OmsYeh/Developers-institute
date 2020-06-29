// var names= ["john", "sarah", 23, "Rudolf",34]
//
// 1. Write a JavaScript for loop that will go through the variable names.
//
// if the item is not a string, pass.
// if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names
//
// if the item is not a string, go out of the loop.
// if the item is a string, display it.

// 1
var names= ["john", "sarah", 23, "Rudolf",34]

for (let i of names){
  if (typeof(i) != 'string'){
    continue;
  } else {
    console.log(i);
  }
}
if (names[i][0] !== names[i][0].toUpperCase()){
  names[i][0].toUpperCase();
}


 newArr[i] = newArr[i].charAt(0).toUpperCase();

var names= ["john", "sarah", 23, "Rudolf",34]
for (let i in names){
if (names[i] !== names[i].charAt(0).toUpperCase()){
  names[i] = names[i].charAt(0).toUpperCase()
}
} 
