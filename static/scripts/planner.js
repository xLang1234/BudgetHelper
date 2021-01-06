var app = angular.module("myApp", [], function ($interpolateProvider) {
    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");
});

app.controller("mainPageCtrl", function ($scope, $http) {
    $scope.data = {};

    $scope.init = function() {
        if(budgetData == null){
            localStorage.setItem("budgetData" , $scope.data);
        }
    }

    $scope.addBudget = function(){

    }
});