
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
    console.log("adding some spice");
    idSelectedUser = {};
	$scope.setSelected = function (id) {
		if (id in idSelectedUser){
			delete idSelectedUser[id];
		}else{
			idSelectedUser[id]=id;
		}
		// console.log("clicked a user");
   		// $scope.idSelectedVote = id;
};
	$scope.checkSelected = function (id) {
		if (id in idSelectedUser){
			console.log( id + " is selected");
			return true;

		}else {
			console.log("not selected");
			return false;
		}
	}
	$scope.addUser = function (){

		$scope.message="this has been run"
		postuser= $http({
			method: 'POST',
			url: 'http://localhost:5000/api/v1/users',
			data:$scope.user
			});

		postuser.then(function (response) {
			console.log(response);
			changeView('/adduser');
		});

	};
		$scope.deleteSelected= function (){
		console.log(JSON.stringify(idSelectedUser));
		deluser= $http({
			method: 'POST',
			url: 'http://localhost:5000/api/v1/users/delete',
			data:{'data': JSON.stringify(idSelectedUser) } 
			});

		deluser.then(function (response) {
			console.log("deleted");
			idSelectedUser={}	;
			changeView('/adduser');
		});

	};
});
  
