// Challenge 1. Prints odds 1-20
for(var i=1; i<=20; i++) {
    if(i % 2 !== 0) {
        console.log(i);
    }
}

// Challenge 2. Decreasing Multiples of 3 from 100-0
for(var i=100; i>=0; i--) {
    if(i % 3 == 0) {
        console.log(i);
    }
}

// Challenge 3. Print the Sequence "4, 2.5, 1, -0.5, -2, -3.5"
arr=[4, 2.5, 1, -0.5, -2, -3.5]
for(var i=0; i<arr.length; i++) {
    console.log(arr[i]);
}

// Challenge 4. Sigma - Print the sum of all values 1-100
var sum = 0
for(var i=0; i<=100; i++) {
    sum += i;
}
console.log(sum)

// Challenge 5. Factorial - multiply all values 1-12 into some variable product
var product = 1
for(var i=1; i<=12; i++) {
    product = i * product;
}
console.log(product)