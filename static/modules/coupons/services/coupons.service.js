(function () {
  'use strict';

  angular
    .module('bagpiper.coupons.services')
    .factory('Coupons', Coupons);

  Coupons.$inject = ['$http'];

  function Coupons($http) {
    var Coupons = {
      all: all
    };

    return Coupons;

    ////////////////////
  
    function all() {
      return $http.get('/api/coupons/');
    }

  }
})();