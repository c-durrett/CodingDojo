// bookIndex(input)
// input is an array of integers (in order) representing pages in a book
// where a given term is found, and the output is a string suitable
// for printing in a book's index
// if the input is [58, 104, 105, 106, 192, 194, 195, 196]
// the output is: "58, 104-106, 192, 194-196"
// if the input is [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18]
// the output is: "1-5, 8-12, 15, 17-18"

// suggestion: break this into two parts, or maybe even two
// functions - get your array of integers and turn it into an array
// of strings, then turn that array of strings into a single string
// [58, 104, 105, 106, 192, 194, 195, 196]
// ["58", "104-106", "192", "194-196"]
// "58, 104-106, 192, 194-196"

// does not handle:
// [ix, x, xi, 1, 2, 3, 7, 8, 9, 32a, 47b, 48b]
// also a suggestion: remember that you can modify your for loop iterator
// during your loop! you can add to or subtract from i at any point

function bookIndex(input) {
    var newIndex = [];
    for(var i=0; i<input.length; i++) {
        startNumber =input[i];
        if(startNumber + 1 == input[i + 1]) {
            endNumber = null;
            while(input[i] + 1 == input[i +1]) {
                endNumber = input[i + 1];
                i++;
            }
            newIndex.push(startNumber + "-" + endNumber);
        }
        else {
            newIndex.push(input[i].toString())
        }
    }
    return newIndex.join(", ");
}

console.log(bookIndex([58, 104, 105, 106, 107, 192, 194, 195, 201]));
console.log(bookIndex([1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18]));
console.log(bookIndex([1, 2, 3, 4, 5]));
console.log(bookIndex([202]));
// console.log(bookIndex([ix, x, xi, 1, 2, 3, 7, 8, 9, 32a, 47b, 48b]))