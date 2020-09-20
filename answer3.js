/*
When the function create, the value of i will always equal to y because i and y are in the same environment.
Change the type of "var" to "let" to let i only be access by the for loop.
The corrected function as below:
*/
function createArrayOfFunctions(y) {
    var arr = [];
    for(let i = 0; i<y; i++) {
    arr[i] = function(x) { return x + i; }
    }
    return arr;
    }