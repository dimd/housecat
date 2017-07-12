angular.module('s2')
	.controller('MainCtrl', function($scope, $http) {
		// Default values
		$scope.location = "Athens Thessalloniki";
		$scope.minPrice = 50;
		$scope.maxPrice = 1000;
		$scope.minSqMeters = 50;
		$scope.maxSqMeters = 500;
		$scope.availability = "Rent";
		$scope.type = "Studio Maisonette";

		$scope.search = function() {
		  var searchParameters = {
		    "Location": $scope.location.split(' '),
		    "Availability": $scope.availability,
		    "minPrice": $scope.minPrice,
		    "maxPrice": $scope.maxPrice,
		    "minSquareMeters": $scope.minSqMeters,
		    "maxSquareMeters": $scope.maxSqMeters,
                    "Type": $scope.type.split(' ')
		  };
		  $http({
		    method: 'GET',
		    url: '/api/properties',
		    params: searchParameters
		  }).then(function(response) {
		     $scope.results = response.data
		  });
		}
	});
