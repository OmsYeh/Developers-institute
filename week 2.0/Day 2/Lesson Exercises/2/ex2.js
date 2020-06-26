let a = 2 + 2;  // var decleration

switch (a) {
  case 3:
    alert( 'Too small' ); // case 3 is smaller than the expression so alert("too small")
    break;
  case 4:
    alert( 'Exactly!' );  // case 4 is exact to the expression so alert("Exactly")
    break;
  case 5:
    alert( 'Too large' );  // case 5 is larger than the expression so alert("too large")
    break;
  default:
    alert( "I don't know such values" );  // when the expression matches none of
}                                         //the cases the default is run
