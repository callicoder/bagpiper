(function() {
	'use strict';

  	angular
    .module('bagpiper.authentication', [
    	'bagpiper.authentication.controllers',
      	'bagpiper.authentication.services'
    ]);

  	angular
    .module('bagpiper.authentication.controllers', []);

  	angular
    .module('bagpiper.authentication.services', ['ngCookies']);
})();
