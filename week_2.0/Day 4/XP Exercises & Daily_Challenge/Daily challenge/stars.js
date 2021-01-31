function getLongestWord(array){
	let longest = 0;
	for (word of array) {
		if (words.length > longest) {
			longest = word.length
		}
	}
	return longest;
}
let sentence = prompt("Enter some words (coma separated)")
console.log(sentence);
let words = sentence.split(",");
for (i in words) {
	words[i] = words[i].trim();
}
let longest = getLongestWord(words);
let starFrame = "*".repeat(longest + 4);
console.log(starFrame);
for (word of words) {
	let line = ("* " + word + " ".repeat(longest-words.length + 1) + "*");
	console.log(line);
}
console.log(starFrame);

// i have a problem with 2 letter words where the star is not in line with the others
