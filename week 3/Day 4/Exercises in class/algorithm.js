function big_num(){
  for (let i in numbers){
    if (numbers[i] > biggest){
      biggest = numbers[i];
    }
  } console.log(biggest);
}
big_num()

function totalOfAll(arr){
  let biggest = 0;
  for (let number of arr){
      biggest += number;
  }
  return biggest;
}
totalOfAll()

function totalOfAll(arr){
  let biggest = 0;
  for (let number of arr){
      let avg = biggest / numbers.length;
  }
  return avg;
}
totalOfAll()
