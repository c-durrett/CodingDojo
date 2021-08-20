// reverseString(input) - your input is a string, and the output
// of the function should be that string, but backwards
// this will be a new string, as strings are immutable
// don't use any built-in functions for reversing a string/array
// in fact, turning the string into an array is unnecessary
// "hello" as your input should return "olleh"
// "Hello!" -> "!olleH"
// "I like to pet cats..." -> "...stac tep ot ekil I"
// "a" -> "a"
// "" -> ""

function reverseString(input) {
    var newString = "";
    for ( var x = input.length - 1; x >= 0; x--){
        newString += input[x];
    }
    return newString;
}

var x = "hello!";
console.log(reverseString(x));