// parensValid(input)
// input is a string
// return true if the input has a valid configuration of parentheses and false
// otherwise. by "return true/false" I mean the boolean value, not a string -
// remember that when you do things like this in the real world, they may
// go through automated testing
// what's valid?
// - no more open parens than close parens or vice versa
// - no close parens that appear before a valid open paren
// - ignore all other characters that are not ( and )
// - '()' -> true
// - ')(' -> false
// - 'hello!' -> true (???)
// - '(())' -> true
// - '(q(a)(x)(!(7(xx)(34)(2, 7, 11))))' -> true
// - '(()' -> false
// - 'hello!()' -> true
// suggestion - don't bother trying to split the string...
// it won't do us any good and just makes things more complicated
// suggestion again - do we have to check every single character in the input?
// hypothetical input: ) followed by one billion characters
// or: a) followed by one billion characters
// or: a37()) followed by one billion characters

function parensValid(input) {
    var openParen = 0
    var closedParen = 0
    for (var i = 0; i < input.length; i++) {
        if (input[i] == ')' && openParen == 0) {
            return false;
        }
        else if (input[i] == '(') {
            openParen++
        }
        else if (input[i] == ')' && openParen > closedParen) {
            closedParen++
        }
    }
    if (openParen == closedParen) {
        return true;
    }
    return false;
}
// get the length and go thru it
// make two temp variables - one to store open parenthesis and one to store closed parenthesis
// be able to check no closed come before an opened (automatic False)

console.log(parensValid('()'));
console.log(parensValid('(())'));
console.log(parensValid('(q(a)(x)(!(7(xx)(34)(2, 7, 11))))'));
console.log(parensValid(')('));
console.log(parensValid('(()'));
console.log(parensValid('hello!'));
// make your own test cases too

// bracesValid(input)
// as above, but for parentheses, curly brackets (or curly braces) and square
// brackets - return true and false
// brackets of different types cannot be interleaved
// '([)]' -> false (?????)
// '()[]{}' -> true
// '(]' -> false
// 'x(37[q{3, 7, 9}{22, 6, 91}])(32q)' -> true
// '()]...' -> false

function bracesValid(input){
    var stack = [];

    for (var i = 0; i < input.length; i++) {
        if (input[i] == '(' || input[i] == '[' || input[i] == '{') {
            stack.push(input[i]);
        }
        else {
            if (input[i] == ')') {
                if (stack[stack.length - 1] == '(') {
                    stack.pop()
                }
                else {
                    return false;
                }
            }

            if (input[i] == ']') {
                if (stack[stack.length - 1] == '[') {
                    stack.pop()
                }
                else {
                    return false;
                }
            }

            if (input[i] == '}') {
                if (stack[stack.length - 1] == '{') {
                    stack.pop()
                }
                else {
                    return false;
                }
            }
        }
    }
    return stack.length == 0;
}

console.log(bracesValid('[(uie])(){}')); // should return false

// bonus: what if we also want to check angle brackets (< and >)? what if
// sometimes we care about curly braces but sometimes we don't?
// suggestion - go back to parensValid/bracesValid and see if they can be
// improved in some way