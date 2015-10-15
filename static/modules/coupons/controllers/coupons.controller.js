(function () {
  'use strict';

  angular
    .module('bagpiper.coupons.controllers')
    .controller('CouponsController', CouponsController);

  CouponsController.$inject = ['$scope'];

  function CouponsController($scope) {
    var vm = this;    
  }
})();