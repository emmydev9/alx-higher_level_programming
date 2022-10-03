#!/usr/bin/node

const process = require("process")
let len = 0
process.argv.forEach(() => {
	len += 1
})

if (len < 3) {
	console.log('No argument')
} else {
	console.log(process.argv[2])
}
