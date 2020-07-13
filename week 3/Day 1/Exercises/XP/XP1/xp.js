// Exercise 1


document.getElementById("navBar").id = "socialNetworkNavigation"
let new_li = document.createElement('li')
let newTextNode = document.createTextNode('Logout')
new_li.appendChild(newTextNode)
let lists = document.getElementById('list').appendChild(new_li)
