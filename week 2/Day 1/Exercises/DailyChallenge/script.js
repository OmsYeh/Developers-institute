var array = ["Banana", "Apples", "Oranges", "Blueberries"];
array.splice(0,1);
console.log(array);
array.sort();
console.log(array);
let kiwiFruit = array.push("kiwi");
console.log(array);
let noApple = array.splice(0,1);
console.log(array);
let rev = array.reverse();
console.log(array);


var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let findOranges = array2[1][1][0];
console.log(findOranges);
