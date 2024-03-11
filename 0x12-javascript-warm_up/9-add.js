#!/usr/bin/node

function add(a, b) {
    return a + b;
}

const args = process.argv.slice(2);
if (args.length < 2) {
    console.log("NaN");
} else {
    const num1 = parseInt(args[0], 10);
    const num2 = parseInt(args[1], 10);
    if (isNaN(num1) || isNaN(num2)) {
        console.log("NaN");
    } else {
        console.log(add(num1, num2));
    }
}
