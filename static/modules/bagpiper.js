(function () {
	'use strict';

	angular
	.module('bagpiper', [
		'bagpiper.routes',
		'bagpiper.config',
		'bagpiper.authentication',
		'bagpiper.layout',
		'bagpiper.utils',
		'bagpiper.profiles',
		'bagpiper.coupons',
		'bagpiper.referral',
		'ui.bootstrap'
	])
	.run(run);

	run.$inject = ['$http'];

	function run($http) {
		$http.defaults.xsrfHeaderName = 'X-CSRFToken';
		$http.defaults.xsrfCookieName = 'csrftoken';	
	}
	
	angular
    .module('bagpiper.routes', ['ngRoute']);

	angular
	.module('bagpiper.config', []);
})();


