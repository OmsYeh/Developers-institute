let Book1 = {
	title: "Of Blood And Bone",
	author: "Nora Roberts",
	image: "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1542605841l/42863006._SY475_.jpg",
	alreadyRead: true
}


let Book2 = {
	title: "Year One",
	author: "Nora Roberts",
	image: "https://kbimages1-a.akamaihd.net/3dd442a4-0bac-4e7a-9161-dd7a2d06b469/1200/1200/False/year-one-3.jpg",
	alreadyRead: true
}


let allBooks = [Book1, Book2];


// this creates a table that has 4 rows and one column
let table = document.createElement('table');
for (let i = 0; i < (allBooks.length*2); i ++) {
	let row = document.createElement('tr');
	let column = document.createElement('td');

	table.appendChild(row);
	table.children[i].appendChild(column);
}


document.body.appendChild(table);


// this put the books(objects that were created) into the table
function add_book(bookNumber, bookrow) {
	let table = document.getElementsByTagName('table')[0];
	table.children[bookrow].firstChild.innerHTML = `${allBooks[bookNumber].title} written by ${allBooks[bookNumber].auther}`;
	let image = document.createElement('img');
	image.src = allBooks[bookNumber].image;
	image.style.width = "100px";
	table.children[bookrow+1].firstChild.appendChild(image);
}


for (let i = 0; i < allBooks.length; i++) {
	add_book(i, i*2);
}


// theres an issue here where the first bool of true turns red but the other doesnt.
for (let i in allBooks) {
	if (allBooks[i].alreadyRead == true) {
		table.children[i].style.color = "red";
	}
}
