/**
 * @author marcd 2019-96-02
 */

var mu = require('../src/multistat');
var wu = require('../src/weight_utils');
var su = require('../src/state_utils');
var u = require('../src/utils');
// console.log(p)
printDeGaussedSaturatedprintCycle();

function printDeGaussedSaturatedprintCycle() {	// 5, 3, 1
	let size = 75;	
	let support = [0, 1];
	let thresholds = u.initThresholds(support, size);		// console.log("thresholds = ", thresholds);
	
	let weights = wu.uniformWeights(thresholds);
	let xHistory = su.degaussHistory(thresholds);
	
	// console.log("weights = ", weights);
	// console.log("xHistory = ", xHistory);

	let m = new mu.multistat(support, size, xHistory, weights);

	let ins = [];
	let outs;

	ins[0] = thresholds[Math.ceil(size/2)];
	outs = m.output; 
	// let tmp = d.currentThreshold;
	[ins, outs] = printCycle(1.1, m, ins, outs);
	[ins, outs] = printCycle(-0.1, m, ins, outs);
	[ins, outs] = printCycle(1.1, m, ins, outs);
	// there are, of course, 'size' statios when traversing from supportMin -> supportMax

}


function printCycle(val, d, ins, out) {
	let ioLists = d.update(val);
	for (let i = 0; i < ioLists[0].length ; i++) {
		ins[1] = ioLists[0][i];
		// outs[1] = ioLists[1][i];

		// should I maybe send to a csv of json file??
		// should I at least JSON.stringify()
		console.log(ins[0], ins[1], out);

		ins[0] = ioLists[0][i];
		out = ioLists[1][i];
	}
	// ins[1] = ioLists[0][ioLists.length-1];
	// console.log(ins[0], ins[1], out);

	// THERE IS THE EXTRA BIT THAT IS MISSING...EXPECIALLY FOR THE SATURATION TAILS
	// THERE IS ALSO THE ARTIFACT THAT IT DOESN'T START AT 0.5: x OR y
	// COULD BE THE Y IS 1 LOW

	return [ins, out];
}
/**
 * Mixed feelings about using JSON when a csv is perfectly fine
 * The thing is that when using numerical arrays they aren't key val pairs
 * So you have to make valid JSON, 
 8 it should be easiest to collect all arrays and work from there
 */
function printJSON(val, d, ins, out) {
	let ioLists = d.update(val);
	// console.log("ioLists = ", ioLists);
	// console.log(ioLists[0]);
	// console.log(ioLists[0].length);

	console.log('{"vals":');

	for (let i = 0; i < ioLists[0].length - 1; i++) {
		ins[1] = ioLists[0][i];
		// outs[1] = ioLists[1][i];

		// should I maybe send to a csv of json file??
		// should I at least JSON.stringify()
		// console.log(ins[0], ins[1], out);
		console.log(JSON.stringify('{"ins":[' + ins + '], "out":' + out + '},\n'));
		// array2dToJson: is basically a nice util but it is easier to create a specialised valid JSON object 
		// let res = u.array2dToJson([ins, [out]], 'statio'+i, '\n');
		// console.log(res);		

		ins[0] = ioLists[0][i];
		out = ioLists[1][i];
	}
	console.log(JSON.stringify('{"ins":[' + ins + '], "out":' + out + '}'));



	console.log('}');

	return [ins, out];
}

