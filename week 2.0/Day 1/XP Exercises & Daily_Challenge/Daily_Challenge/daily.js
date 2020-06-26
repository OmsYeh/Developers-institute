var array = ["Banana", "Apples", "Oranges", "Blueberries"];
let arr_banana = array.splice(0,1);
console.log(arr_banana);
array.sort();
array.push("Kiwi");
array.splice(0,1);
array.reverse();
console.log(array);


// 2

var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(array2[1][1][0]);
