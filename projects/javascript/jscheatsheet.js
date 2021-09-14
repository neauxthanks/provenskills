// JavaScript CheatSheet

/* Overall Syntax and Behavior
- uses semicolons like java
- variables have an inital value of "undefined",
        will return a value of NaN (not a number)
- use camelCase like everywhere else
*/

// Starting off with commenting -- in line comment

/* Multi-line comment
everthing after that symbol will be commented 
until it reaches */

// Declaring Variables
var newvariable;
var anothervar;


// assigning 
newvariable = 8;
anothervar = newvariable;

// initializing a new variable
var initvar = 9;



//---- primatives and data types ---

// Numerical Values
    // operators same as always
    // Floats for decimals

// Strings
    // escaping literal quotes in js:

var example = "Outside the quotes \"Inside the Quotes\"";

    /* single or double quotes can be used just be consistent 
    and consider what quotes are be used in the string. *

    \'	single quote
    \"	double quote
      --- interchangable ---
    \\	backslash
    \n	newline
    \r	carriage return -- returns the pointer to the start of the curr line
    \t	tab
    \b	word boundary -- a test for
    \f	form feed -- page break

    WORD BOUNDARIES ARE:

        At string start, if the first string character is a word character \w.
        Between two characters in the string, where one is a word character \w and the other is not.
        At string end, if the last string character is a word character \w.
    */
var letterCount = example.length;

   /* strings are immunitable so it must be reassigned

   */

e

// FUNCTIONS
    /* Syntax of a function 
    function nameOfFunction() {
        do something;
        statements;
    }
    */

function exampleFunction () {
    console.log("Hello World");
}
function exampleFunctionWA (a, b) { // with args
    console.log(a+b);
}

function returnExample () {
    var sweet = "ice cream";
    return sweet;
}

    // calling a function
exampleFunction();
exampleFunctionWA(5,7);
var happy = returnExample();

    //scope (visibility)
globalscope = 6; // this is automatically under the "global" scope -- can be used anywhere
    // declared within a function, var a is automatically "local" scope -- can only be used in that function and taked precendence

    // STATEMENTS

    /* 

    IF/ELSE IF/ELSE

    if (condition) {
        do something;
    } else if (condition) {
        do something;
    } else {
        do something;
    }

    SWITCH --- tested with STRICT EQUALITY
    switch(someValue){
        case a:
            return "A"
            break;       -- break prevents the next statement from being executed 
        etc...:
            ...;
            break;
        default:
            ...;
            break;
    }
    
    WHILE LOOP -- just like java

    DO WHILE -- just like java

    FOR LOOP -- just like java except init as var not int

    == is equality operator --- considered equal regardless of type, js does type conversion
    === strict equality operator --- type and value must match

    typeof operator will determine type of the variable
    */

// DATA STRUCTURES
    //Queues
    /* queues are characterized by FCFO protocol */
var arr = [1, 2, 3];
function impQueue(arr, num){
    arr.push(num); //adds num to the
    arr.shift(); //removes first value
}
    //

// Arrays
/* BIG O NOTATION INFORMATION:
In contrast to most languages, which implement arrays with, well, arrays, in Javascript Arrays are objects, and values are stored in a hashtable, just like regular object values. As such:

Access - O(1)
Appending - Amortized O(1) (sometimes resizing the hashtable is required; usually only insertion is required)
Prepending - O(n) via unshift, since it requires reassigning all the indexes
Insertion - Amortized O(1) if the value does not exist. O(n) if you want to shift existing values (Eg, using splice).
Deletion - Amortized O(1) to remove a value, O(n) if you want to reassign indices via splice.
Swapping - O(1)
In general, setting or unsetting any key in a dict is amortized O(1), and the same goes for arrays, regardless of what the index is. Any operation that requires renumbering existing values is O(n) simply because you have to update all the affected values.
*/
    // can contain more than one datatype
var myArray = ["HI", 2];

// nested arrays
var myNestedArray = [["HI", 2], ["Smile", 4]] // each inner array is called a subarray

//mainpulate arrays
myArray[0] = "Pretty"; // assignment with index
myArray.push("there"); // add to the end of the array
myArray.unshift(5); // adds to the beginning of the array
var removedFromArray = myArray.pop(); // pop returns and removes end value
var begFromArray = myArray.shift(); // returns and removes first valu
// OBJECTS
    //syntax
var obj = {
    field_name: "name",
    "field_val": 0,
    "field_arr": [0,1],
    removed: 7
    // can use numbers as properties but will be typecasted to string
}
    // accessing values from an object
var nametag = obj.field_name; 
var val = obj[field_val]; // must have quotes if the field has spaces in them
var arraccess = obj.field_arr[1];
    //adding and removing properties
obj.added = true;
delete obj.removed;
    // check if property exists
obj.hasOwnProperty(field_arr);

