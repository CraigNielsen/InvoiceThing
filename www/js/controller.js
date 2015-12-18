
myApp.controller('appController', function ($scope, $http,$location) {
	$scope.message="Invoice Pal";


	getUsers = $http({
		method: 'GET',
		url: 'http://localhost:5000/api/v1/users'
	});

	getUsers.then(function (response) {
		$scope.users = response.data;
	});

	changeView = function(view){
            $location.path(view); // path not hash
        }

	$scope.addUser = function (){

		$scope.message="this has been run"
		postuser= $http({
			method: 'POST',
			url: 'http://localhost:5000/api/v1/users',
			data:$scope.user
			});

		postuser.then(function (response) {
			changeView('/users');
		});

	};
});
  
