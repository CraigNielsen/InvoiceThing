var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
    when('/users', {
      templateUrl: 'users.html',
      controller: 'appController'
    }).
    when('/adduser', {
      templateUrl: 'adduser.html',
      controller: 'appController'
    }).
    when('/success', {
      templateUrl: 'success.html',
      controller: 'SuccessController'
    }).
    otherwise({
      redirectTo: '/adduser'
    });
}]);