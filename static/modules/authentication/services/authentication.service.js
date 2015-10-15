(function() {
	'use strict'
	angular
	.module('bagpiper.authentication.services')	
	.factory('Authentication', Authentication);

	Authentication.$inject = ['$cookies', '$http'];
	
	function Authentication($cookies, $http) {
		var Authentication = {
			login: login,
			register: register,
			logout: logout,
			getAuthenticatedAccount: getAuthenticatedAccount,
			isAuthenticated: isAuthenticated,
			setAuthenticatedAccount: setAuthenticatedAccount,
			unauthenticate: unauthenticate
		};

		return Authentication;

		function login(email, password) {
			return $http.post('/api/auth/login/', {
				email: email,
				password: password
			}).then(loginSuccessFn, loginErrorFn);
		}

		function loginSuccessFn(response, status, headers, config) {
			Authentication.setAuthenticatedAccount(response.data);	
			window.location = '/';
		}

		function loginErrorFn(response, status, headers, config) {
			console.error(response.data);
		}

		function register(email, password, username) {
			return $http.post('/api/users/', {
				username: username,
				password: password,	
				email: email
			}).then(registerSuccessFn, registerErrorFn);
		}

		function registerSuccessFn(response, status, headers, config) {
			Authentication.login(response.data.email, response.data.password);
		}

		function registerErrorFn(response, status, headers, config) {
			console.error(response.data);
		}

		function logout() {
			return $http.post('/api/auth/logout/')
				.then(logoutSuccessFn, logoutErrorFn);
		}

		function logoutSuccessFn(response, status, headers, config) {
			Authentication.unauthenticate();
			window.location = '/';
		}

		function logoutErrorFn(response, status, headers, config) {
			console.error(response.data);
		}
	
		function getAuthenticatedAccount() {
			if(!$cookies.authenticatedAccount) {
				return;
			}
			return JSON.parse($cookies.authenticatedAccount);
		}

		function isAuthenticated() {
			return !!$cookies.authenticatedAccount;
		}

		function setAuthenticatedAccount(account) {
			$cookies.authenticatedAccount = JSON.stringify(account);	
		}

		function unauthenticate() {
			delete $cookies.authenticatedAccount;
		}
	}

})();
