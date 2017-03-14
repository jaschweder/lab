"use strict";
describe('TestController', function(){
	beforeEach(module('testApp'));

	describe('list', function(){
		it('should have a list initialized with 3 elements', inject(function($controller){
			var testController = $controller('TestController');
            		assert.equal(3, testController.list.length);
		}));
	});
});
