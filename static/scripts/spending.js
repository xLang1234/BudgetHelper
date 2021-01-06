var app = angular.module("myApp", [], function ($interpolateProvider) {
    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");
});

app.controller("mainPageCtrl", function ($scope, $http) {
    $scope.data = [];
    
    var cb = function(result){
        console.log(result);
        $scope.data = result;
        $scope.$apply();
    }

    $scope.init = function() {
        doAJAXCall('spendingdata', { 'user_id' : localStorage.getItem("user_id") }, cb , cb)
    }

});