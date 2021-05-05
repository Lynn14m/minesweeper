angular.module('minesweeperApp.homeCtrl', [
    'ui.router',
    'ngRoute',
    'ngMaterial',
    'minesweeperApp.homeCtrl',
    'minesweeperApp.dashboardCtrl',
    'minesweeperApp.easyGameCtrl'
])

.config(function config($stateProvider, $httpProvider){

    const homeState = {
        name: 'home',
        url: '/home',
        templateUrl: 'static/app/components/home/home.html',
        controller: 'homeCtrl'
    };

    const dashboardState = {
        name: 'dashboard',
        url: '/dashboard',
        templateUrl: 'static/app/components/dashboard/dashboard.html',
        controller: 'dashboardCtrl'
    };

    const easyGameState = {
        name: 'dashboard.easy',
        url: '/dashboard/easy',
        templateUrl: 'static/app/components/game/easyGame.html',
        controller: 'easyGameCtrl'
    };

    const mediumGameState = {
        name: 'dashboard.medium',
        url: '/dashboard/medium',
        templateUrl: 'static/app/components/game/mediumGame.html',
        controller: 'mediumGameCtrl'
    };

    const hardGameState = {
        name: 'dashboard.hard',
        url: '/dashboard/hard',
        templateUrl: 'static/app/components/game/hardGame.html',
        controller: 'hardGameCtrl'
    };

    $stateProvider.state(homeState);
    $stateProvider.state(dashboardState);
    $stateProvider.state(easyGameState);
    $stateProvider.state(mediumGameState);
    $stateProvider.state(hardGameState);

})

.controller('homeCtrl', ['$scope', '$rootScope', '$http', '$state', function($scope, $rootScope, $http, $state) {

    $rootScope.$state = $state;

    $scope.enterGame = function () {
        $state.go('dashboard.easy');
    }

}])
