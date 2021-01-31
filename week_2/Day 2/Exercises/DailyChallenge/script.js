let mystring="This movie was not that bad"

let wordNot = mystring.indexOf("not");
let wordBad = mystring.indexOf("bad");

if (wordBad>wordNot){
  console.log("The word NOT comes first.")
} else {
  console.log("The word BAD comes first.");
}
console.log(mystring.substr(0, wordNot)+ "good");
