/**
 * @author marcd 2019-96-02
 */

var mu = require('../src/multistat');
var wu = require('../src/weight_utils');
var su = require('../src/state_utils');
var u = require('../src/utils');
var s = require('../src/statio');
// console.log(p)
printAllStatios();

function printAllStatios() {	// 5, 3, 1
	let size = 7;	
	let support = [0, 1];
	let thresholds = u.initThresholds(support, size);		// console.log("thresholds = ", thresholds);
	
	let weights = wu.uniformWeights(thresholds);
	// console.log("weights = ", weights);
	let xHistory = [0];
	
	let m = new mu.multistat(support, size, xHistory, weights);

	let ins = [];
	let outs;

	ins[0] = thresholds[Math.ceil(size/2)];
	outs = m.output; 

	statios = s.buildStatios(weights);
	// console.log("num statios = ", statios.length);
	for (let s of statios) { 
		// console.log(s.thresholds, s.output);
		console.log(s.thresholds[0], s.thresholds[1], s.output);
		// console.log(s.arr);
	}

}

function printCycle(val, d, ins, out) {
	let ioLists = d.update(val);
	// console.log("ioLists = ", ioLists);
	// console.log(ioLists[0]);
	// console.log(ioLists[0].length);
	for (let i = 0; i < ioLists[0].length; i++) {
		ins[1] = ioLists[0][i];
		// outs[1] = ioLists[1][i];

		// should I maybe send to a csv of json file??
		// should I at least JSON.stringify()
		// console.log("cycle ", ins[0], ins[1], outs[0], outs[1]);
		// let res = [ins, out];
		console.log(ins[0], ins[1], out);
		// console.log(JSON.stringify(res));

		ins[0] = ioLists[0][i];
		out = ioLists[1][i];
	}		
	return [ins, out];
}

