var myApp = angular.module('myApp', ['ui.router']);

myApp.config(function($stateProvider, $urlRouterProvider) {
  //
  // For any unmatched url, redirect to /state1
  $urlRouterProvider.otherwise("/state1");
  //
  // Now set up the states
  $stateProvider
    .state('state1', {
      url: "/state1",
      templateUrl: "navbar.html"
    })
    .state('state1.users', {
      url: "/users",
      templateUrl: "users.html",
      controller: function($scope) {
        $scope.items = ["A", "List", "Of", "Items"];
      }
    })
    .state('state1.addusers', {
      url: "/addusers",
      templateUrl: "adduser.html",
      controller: "appController"
    })
    .state('state1.login', {
      url: "/login",
      templateUrl: "login.html",
      controller: "loginController"
    })
    .state('state1.signup', {
      url: "/login",
      templateUrl: "signup.html",
      controller: "loginController"
    })
    .state('state1.login.signup', {
      url: "/signup",
      templateUrl: "signup.html",
      controller: "loginController"
    })
});
