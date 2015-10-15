(function () {
  'use strict';

  angular
    .module('bagpiper.referral.services')
    .factory('Referral', Referral);

  Referral.$inject = ['$http'];

  function Referral($http) {
    var Referral = {
      verify: verify
    };

    return Referral;

    ////////////////////
  
    function verify(refcode) {
      return $http.get('/api/referral/' + refcode + '/verify/');
    }

  }
})();