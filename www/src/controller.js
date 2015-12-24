myApp.controller('appController', function ($scope, $http, $location) {
	updateUsers = function () {
		getUsers = $http({
			method: 'GET',
			url: 'http://localhost:5000/api/v1/users'
		});
		getUsers.then(function (response) {
			$scope.users = response.data;
		});
	};
    
	$scope.setSelected = function (id) {
		if (id in idSelectedUser){
			delete idSelectedUser[id];
		} else {
			idSelectedUser[id] = id;
		}
	};

	$scope.checkSelected = function (id) {
		if (id in idSelectedUser){
			return true;
		} else {
			return false;
		}
	}

	$scope.addUser = function (){
		createUser = $http({
			method: 'POST',
			url: 'http://localhost:5000/api/v1/users',
			data:$scope.user
		});
		createUser.then(function (response) {
			updateUsers();
		});
	};
	
	$scope.deleteSelected= function (){
		deleteUser = $http({
			method: 'POST',
			url: 'http://localhost:5000/api/v1/users/delete',
			data:{'data': JSON.stringify(idSelectedUser) } 
		});
		deleteUser.then(function (response) {
			idSelectedUser = {};
			updateUsers();
		});
	};

	$scope.message="Invoice Pal";
	updateUsers();
	console.log("adding some spice");
    idSelectedUser = {};
});
