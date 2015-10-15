(function () {
  'use strict';

  angular
    .module('bagpiper.profiles.services')
    .factory('Profile', Profile);

  Profile.$inject = ['$http'];

  function Profile($http) {

    var Profile = {
      destroy: destroy,
      get: get,
      update: update
    };

    return Profile;

    /////////////////////

    function destroy(profile) {
      return $http.delete('/api/users/' + profile.id + '/');
    }

    function get(username) {
      return $http.get('/api/users/' + username + '/');
    }

    function update(profile) {
      return $http.put('/api/users/' + profile.username + '/', profile);
    }
  }
})();