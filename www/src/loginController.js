myApp.controller('loginController', function ($scope, $http, $location) {
	$scope.message="Invoice Pal";
	$scope.Login = function () {
		console.log("trying to login")
	}
	$scope.signup = function () {
		console.log("trying to signup")
	}
});  
