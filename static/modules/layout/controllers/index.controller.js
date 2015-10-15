(function () {
  'use strict';

  angular
    .module('bagpiper.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Authentication', 'Coupons', 'Referral', 'Snackbar', '$modal'];

  function IndexController($scope, Authentication, Coupons, Referral, Snackbar, $modal) {
    var vm = this;

    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.coupons = [];
    vm.refcode = ''

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

    vm.verifyReferral = function() {
      Referral.verify(vm.refcode)
      .then(function(response){
        Snackbar.show(response.data.message);
      }, function(){
        Snackbar.error(response.data);
      });
    };

  }
})();
