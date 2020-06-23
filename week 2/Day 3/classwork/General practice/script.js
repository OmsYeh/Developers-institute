let family = {
    members: ["mom", "dad"],
    numberMembers: 2,
    familyName: "Smith",
    hasPet: true
}
//We go over the keys of the object family
for (let property in family) {
    //We check if there is an existing property with a name of familyName
    if (property === "familyName") {
        // If a property has a name of familyName, we check if the value is Smith
        // If the value is Smith
        if (family[property] === "Smith") {
            console.log("Hello the Smith Family")
            // If the value is not Smith
        } else {
            console.log("I don't know you")
        }
        //if there is no existing property with a name of familyName, we enter the else
    } else {
        console.log("No FamilyName")
    }
  }
