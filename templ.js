// const temp = (num) => {
//   return num?.toString()?.split("")?.join(" ");
// };

// console.log("32132132132", temp(32132132132));

function vowelAndConsonants(str) {
  let vowels = new Set("aeiouAeiou");
  let vowelCount = 0;
  let consonantsCount = 0;

  for (let i = 0; i < str.length; i++) {
    let char = str[i];

    if ((char >= "A" && char <= "Z") || (char >= "a" && char <= "z")) {
      if (vowels.has(char)) vowelCount++;
    } else {
      consonantsCount++;
    }
  }

  return { vowelCount, consonantsCount };
}

console.log(vowelAndConsonants("abce"));
