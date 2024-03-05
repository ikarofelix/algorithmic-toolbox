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
    let result = [0, 1];
    for (let i = 2; i <= n; i++) {
        result[i] = result[i-1] + result[i-2]
    }
    return result[n];
}

module.exports = fib;
