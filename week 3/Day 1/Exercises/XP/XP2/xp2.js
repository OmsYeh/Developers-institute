// Exercise 2

document.body.children[1].lastElementChild.innerHTML = "Richard";
let li1 = document.getElementsByClassName('list')[0].firstElementChild;
let li2 = document.getElementsByClassName('list')[1].firstElementChild;
li1.innerHTML = "Omri";
li2.innerHTML = "Omri";
// I struggled to find a way replace both firstElementChild in one line of code
let new_li = document.createElement('li');
let new_textnode = document.createTextNode('Hey students');
let new_li_2 = document.createElement('li');
let new_textnode_2 = document.createTextNode('Hey students');
new_li.appendChild(new_textnode);
new_li_2.appendChild(new_textnode_2);
let lists = document.getElementsByClassName('list')[0].appendChild(new_li);
let lists2 = document.getElementsByClassName('list')[1].appendChild(new_li_2);
// this is very repetative, i know.

let uList = document.getElementsByClassName('list')[1].children[1];
let parentElem = document.getElementsByClassName('list')[1];
parentElem.removeChild(uList);
