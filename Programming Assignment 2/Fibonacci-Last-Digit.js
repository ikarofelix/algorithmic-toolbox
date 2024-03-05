// by Alexander Nikolskiy

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    console.log(fib(parseInt(line, 10)));
    process.exit();
}

function fib(n) {
    // write your code here
    let remainder = n % 60;

    let fibonacci = [0, 1]
    for (let i = 2; i <= 60; i++) {
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    }

    const number = fibonacci[remainder]

    const numberSplitted = number.toString().split("")

    return Number(numberSplitted[numberSplitted.length - 1])
}

module.exports = fib;
