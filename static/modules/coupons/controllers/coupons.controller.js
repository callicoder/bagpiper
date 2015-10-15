(function () {
  'use strict';

  angular
    .module('bagpiper.coupons.controllers')
    .controller('CouponsController', CouponsController);

  CouponsController.$inject = ['$scope'];

  function CouponsController($scope) {
    var vm = this;

    vm.columns = [];

    activate();


    function activate() {
      $scope.$watchCollection(function () { return $scope.posts; }, render);
    //  $scope.$watch(function () { return $(window).width(); }, render);
    }
    
  }
})();