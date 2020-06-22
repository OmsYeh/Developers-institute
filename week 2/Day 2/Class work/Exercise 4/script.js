1. get the numberPets
2. get the 2nd type of pet
3; What is the favorite food of the cat
​
let users = [
    {
        username: "Sarah",
        password: 123,
        friends: ["max", "tom"],
        pets : {
            numberPets : 2,
            typePets : ["dog", "cat"],
            favoriteFood : {
                dog : "candy",
                cat : "milk"
            }
        }
    }
]


// 1.
console.log(users[0].pets.numberPets);

// 2.
console.log(users[0].pets.typePets[1]);

// 3.
console.log(users[0].pets.favoriteFood.cat);
