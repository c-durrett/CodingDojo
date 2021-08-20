class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// a stack! last in, first out
// we add/remove from the top of a stack
// what's going to be the "top" of our stack here?

class SLLStack {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    // push(value) - adds the given value to the stack
    push(value) {
        var newNode = new ListNode(value);

        if (this.head == null && this.tail == null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            newNode.next = this.head;
            this.head = newNode;
        }
    }
    

    // pop() - removes the top value from stack and returns it
    pop() {
        if (this.head == null && this.tail == null) {
            return undefined;
        }
        if (this.head == this.tail) {
            var temp = this.head;
            this.head = temp.next;
            temp.next = null;
            return temp.value;
        }
        else{
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }
    }

    // top() - returns the top value without removing it
    top() {
        if (this.head == null && this.tail == null) {
            return undefined;
        }
        return this.head.value;
    }

    // contains(target) - returns true if the target value is in the stack,
    // false if not
    contains(target) {
        var runner = this.head;

        while (runner != null) {
            if (runner.value == target) {
                return true;
            }
            runner = runner.next;
        }
        return false;
    }

    // isEmpty() - returns true if the stack is empty, false otherwise
    isEmpty() {
        if (this.head == null && this.tail == null) {
            return true;
        }
    }

    // size() - returns the size of the stack
    // bonus to think about: we can make this way faster - how?
    size() {
        if (this.head == null && this.tail == null) {
            return undefined;
        }
        counter = 0
        var runner = this.head
        
        while (runner != null) {
            counter ++;
            runner = runner.next
        }
        return counter
    }
}

var x = new SLLStack();

console.log(x.pop());
console.log(x.top());
console.log(x.contains(1));
console.log(x.isEmpty());
console.log(x.size());

x.push(7);
x.push(3);
x.push(8);

console.log(x.top());
console.log(x.pop());
console.log(x.contains(8));
console.log(x.contains(7));
console.log(x.isEmpty());
console.log(x.size());