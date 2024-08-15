// Question 2: Largest Number At Least Twice of Others
// Problem Statement:
// In a given integer array nums, find the largest element and check if it is at least twice as much as every other number in the array. If it is, return the index of the largest element; otherwise, return -1.

type Types = (arr: number[]) => number;

const dominant_index: (arr: number[]) => number = (arr) => {
  // brute force

  //   find the index of largest element
  //   let largestIndex = 0;

  //   for (let i = 0; i < arr.length; i++) {
  //     if (arr[i] > arr[largestIndex]) {
  //       largestIndex = i;
  //     }
  //   }

  //   for (let i = 0; i < arr.length; i++) {
  //     if (i !== largestIndex && arr[largestIndex] < 2 * arr[i]) {
  //       return -1;
  //     }
  //   }

  //   return largestIndex;

  if (arr.length < 2) return 0; // Handle cases with less than two elements

  let index = 0;
  let largestValue = -Infinity;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > largestValue) {
      largestValue = arr[i];
    }
  }

  console.log(largestValue);

  return -1;
};

console.log(dominant_index([3, 6, 1, 0])); // Output: 1 (6 is at least twice as much as every other number)
// console.log(dominant_index([1, 2, 3, 4])); // Output: -1 (4 is not at least twice as much as 3)
