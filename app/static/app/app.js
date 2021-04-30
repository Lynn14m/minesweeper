angular.module('minesweeperApp', [
    'ui.router',
    'ngRoute',
    'ngMaterial',
    'minesweeperApp.homeCtrl',
    'minesweeperApp.dashboardCtrl',
    'minesweeperApp.easyGameCtrl',
    'minesweeperApp.mediumGameCtrl',
    'minesweeperApp.hardGameCtrl'
])

.config(['$stateProvider', '$urlRouterProvider', '$httpProvider', function($stateProvider, $urlRouterProvider, $httpProvider) {
	$urlRouterProvider.otherwise("/home");

	$httpProvider.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest";
}])


