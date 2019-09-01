var assert = require('assert');
/*
*Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
*/

const filter_list = l => l.filter((value) => typeof value == "number");

filter_list([1,'a','b',0,15])
//[1, 0, 15]