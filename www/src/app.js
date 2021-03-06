var myApp = angular.module('myApp', ['ui.router']);

myApp.config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise("/state1");

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
        .state('state1.signin', {
            url: "/signin",
            templateUrl: "login.html",
            controller: "loginController"
        })

});
