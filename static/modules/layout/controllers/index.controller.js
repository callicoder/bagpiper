(function () {
  'use strict';

  angular
    .module('bagpiper.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Authentication', 'Coupons', 'Snackbar', '$modal'];

  function IndexController($scope, Authentication, Coupons, Snackbar, $modal) {
    var vm = this;

    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.coupons = [];

    activate();
    function activate() {

      Coupons.all().then(couponsSuccessFn, couponsErrorFn);


      function couponsSuccessFn(data, status, headers, config) {
        vm.coupons = data.data;
      }

      function couponsErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }
  }
})();
