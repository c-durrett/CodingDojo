// 1
console.log(hello);                                   
var hello = 'world';                                 
// var hello;
// console.log(hello); // logs undefined
// hello = 'world';


// 2
var needle = 'haystack';
test();
function test(){
    var needle = 'magnet';
    console.log(needle);
}
// var needle;
// function test(){ 
// var needle;
// needle = 'magnet';
// console.log(needle); // logs 'magnet'
// test();  // test is called, the first console log runs
// needle = 'haystack';


// 3
var brendan = 'super cool';
function print(){
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);

// var brendan;
// function print();
// var brendan;
// brendan = 'only okay';
// console.log(brendan);
// brendan = 'super cool';
// console.log(brendan); // logs 'super cool'


// 4
var food = 'chicken';
console.log(food);
eat();
function eat(){
    food = 'half-chicken';
    console.log(food);
    var food = 'gone';
}
// var food;
// food = 'chicken';
// console.log(food); // console logs 'chicken'
// fucntion eat(){ 
// var food;
// var food;
// console.log(food); // logs 'half-chicken'
// food = 'half-chicken';
// food = 'gone';
// eat(); // eat is called,  second console.log runs


// 5
mean();
console.log(food);
var mean = function() {
    food = "chicken";
    console.log(food);
    var food = "fish";
    console.log(food);
}
console.log(food);

// error - mean isnt defined
// 


// 7 
console.log(genre);
var genre = "disco";
rewind();
function rewind() {
    genre = "rock";
    console.log(genre);
    var genre = "r&b";
    console.log(genre);
}
console.log(genre);

//
//

// 8 - Bonus ES6: const
console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));
function makeDojo(name, students){
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if(dojo.students > 50){
        dojo.hiring = true;
    }
    else if(dojo.students <= 0){
        dojo = "closed for now";
    }
    return dojo;
}
//