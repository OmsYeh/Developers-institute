1. Loop through the array of object
2. If the username is Sarah : say hello to her friends (display the name of her friends)
3. If the username is Dan : change his password to 567
​
--> can use switch
--> for in or for of
​
​
let users = [
    {
        username: "Sarah",
        password: 123,
        friends: ["max", "tom"]
    },
    {
        username: "Dan",
        password: 433
    }
  ]

for (let user of users){
  if (user.username === "Sarah") {
  console.log("Hey Sarahs friends ", user.friends[0],"and",user.friends[1]);
} else {
  console.log("user not online");
}
}
