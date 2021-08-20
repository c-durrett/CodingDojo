class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// a queue! first in, first out
// where should we add items? where are they removed from>

class SLLQueue {
    constructor() {
        this.head = null;
        this.tail = null;
    }
    // enqueue(value) - adds the given value to the queue (at the tail)
    enqueue(value) {
        var newQ = new ListNode(value);
        if (this.head == null && this.tail == null) {
            this.head = newQ;
            this.tail = newQ;
        }
        else {
            newQ.next = null;
            this.tail = newQ;
        }
    }
    
    // dequeue() - removes the front (i.e. the head) value from queue and returns it
    dequeue() {
        if (this.head == null && this.tail == null) {
            return undefined;
        }
        if (this.head == this.tail){
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }

        var temp = this.head;
        this.head = this.head.next;
        temp.next = null;
        return temp.value;
    }

    // front() - returns the front value without removing it
    front() {
        if (this.head == null) {
            return undefined;
        }
        return this.head.value;
    }

    // contains(target) - returns true if the target value is in the queue,
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

    // isEmpty() - returns true if the queue is empty, false otherwise
    isEmpty() {
        if (this.head == null && this.tail == null) {
            return true;
        }
    }

    // size() - returns the size of the queue
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

    // method: compareQueues (odd-numbered group)
    // return true if the queues have the same values in the same order
    // false otherwise
    // important: this is a non-destructive operation!
    // do not modify either queue
    compareQueues(queue2) {
        
    }
}

// compareQueues (even-numbered group)
// return true if the queues have the same values in the same order
// false otherwise
// important: this is a non-destructive operation!
// do not modify either queue
function compareQueues(queue1, queue2) {
    if (size(queue1) != size(queue2)) {
        return false
    }
    else {
        counter = 0;
        var runner = queue1.head
        var runner2 = queue2.head
        while (runner != null) {
            if (runner.value != runner2.value) {
                return false
            }
            else {
                runner = runner.next
                runner2 = runner2.next
            }
        }
        return true
    }
}


// test your queue implementation here!

var queue_A = new SLLQueue();

var queue_B = new SLLQueue();

var queue_C = new SLLQueue();

var queue_D = new SLLQueue();