const nums = [3, 5, 2, 7, 8, 78, 1];
debugger;

const bubble_sort = (nums: number[]) => {
  let n = nums.length;

  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (nums[j] > nums[j + 1]) {
        let temp = nums[j];
        nums[j] = nums[j + 1];
        nums[j + 1] = temp;
      }
    }
  }
  return nums;
};

console.log(bubble_sort(nums));
