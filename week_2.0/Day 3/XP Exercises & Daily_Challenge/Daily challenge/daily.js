const arr = [5,0,9,1,7,4,2,6,3,8];

function bubbleSort(arr){
  const loop = arr.length;
  for (let i = 0; i < loop; i++){
    for (let j = 0; j < loop; j++){
      if (arr[j] > arr[j+1]){
        let temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
    }
  }
  return arr;
}

bubbleSort([5,0,9,1,7,4,2,6,3,8]);
