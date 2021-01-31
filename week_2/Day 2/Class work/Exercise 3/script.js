// a=4

let a = 2 + 2;

// case a will succeed ('Right!')
switch (a) {
  case 4:
    alert('Right!');
    break;

// dev made an or case here
  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}
