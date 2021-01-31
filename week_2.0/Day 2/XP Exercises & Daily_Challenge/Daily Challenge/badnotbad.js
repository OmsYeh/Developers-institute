// Daily challenge : Not Bad

// Create a string that has the word “not” and “bad” inside

// Create another variable that should find the first appearance
// of the substring ‘not’ and ‘bad’.

// If the ‘bad’ follows the ‘not’, then it should replace the whole
// ‘not’…’bad’ substring with ‘good’ than console.log the result.

// If it doesn’t find ‘not’ and ‘bad’ in the right sequence (or at all),
// just console.log the original sentence.


let str = "The dinner was not that bad";

let not = str.indexOf("not");
let bad = str.indexOf("bad");

if (bad > not){
  console.log("The word NOT comes first");
} else {
    console.log("The word BAD comes first");
}
if (bad > not){
  console.log(str.substr(0, not)+ "good");
} else {
  console.log(str);
}
