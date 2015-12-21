var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
    when('/users', {
      templateUrl: 'views/users.html',
      controller: 'appController'
    }).
    when('/adduser', {
      templateUrl: 'views/adduser.html',
      controller: 'appController'
    }).
    when('/success', {
      templateUrl: 'views/success.html',
      controller: 'SuccessController'
    }).
    otherwise({
      redirectTo: '/adduser'
    });
}]);