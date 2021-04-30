angular.module('minesweeperApp.dashboardCtrl', [
    'ui.router',
    'ngRoute',
    'ngMaterial',
    'ngMessages',
    'minesweeperApp.dashboardCtrl',
    'minesweeperApp.easyGameCtrl',
    'minesweeperApp.mediumGameCtrl',
    'minesweeperApp.hardGameCtrl'
])

.controller('dashboardCtrl', ['$scope', '$rootScope', '$http', '$state',
    function($scope, $rootScope, $http, $state) {

    $rootScope.$state = $state;

    $scope.goToEasyGame = () => {
        $state.go('dashboard.easy')
    }

    $scope.goToMediumGame = () => {
        $state.go('dashboard.medium')
    }

    $scope.goToHardGame = () => {
        $state.go('dashboard.hard')
    }


}])