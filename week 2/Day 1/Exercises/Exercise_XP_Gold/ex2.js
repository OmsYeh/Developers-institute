let string1="hello";
let string2="goodbye"
let abc1=string1.substring(0,1);
console.log(abc1);
let def1=string1.substring(1,5);
console.log(def1);
let abc2=string2.substring(0,1);
let def2=string2.substring(1,7);
console.log(abc2);
console.log(def2);
let newWord=(`${abc2}${def1} ${abc1}${def2}`);
console.log(newWord);
