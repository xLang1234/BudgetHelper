var app = angular.module("myApp", [], function ($interpolateProvider) {
    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");
});

app.controller("mainPageCtrl", function ($scope, $http) {
    $scope.data = [];
    $scope.sendData = {
        'name' : '',
        'amount' : 0,
        'user_id' : 1
    };
    var cb = function(result){
        console.log(result);
        $scope.data = result;
        $scope.$apply();
    }

    var cbAdd = function(result){
        console.log(result)
        alert("Added into budgets")
    }

    $scope.init = function() {
        doAJAXCall('data', {}, cb , cb)
    }

    $scope.addBudget = function(){
        doAJAXCall('insertdata', $scope.sendData, cbAdd , cbAdd);
    }

    $scope.addSpending = function(){
        doAJAXCall('insertdata', $scope.sendData, cbAdd , cbAdd);
    }
});