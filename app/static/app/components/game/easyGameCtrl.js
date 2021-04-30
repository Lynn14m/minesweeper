angular.module('minesweeperApp.easyGameCtrl', [
    'ui.router',
    'ngRoute',
    'ngMaterial',
    'minesweeperApp.dashboardCtrl',
    'minesweeperApp.easyGameCtrl',
])

.controller('easyGameCtrl', ['$scope', '$rootScope', '$http', '$state','$mdDialog', function($scope, $rootScope, $http, $state, $mdDialog) {

    $rootScope.$state = $state;

    const defaultGrid = {
        rowsCount: 4,
        columnsCount: 4,
        mineCount: 3
    }

    $scope.showGameWon = function(ev) {
        let gameWon = $mdDialog.confirm()
          .title('YOU WON!')
          .textContent("Well Done! You've won!")
          .ariaLabel('Game won')
          .targetEvent(ev)
          .ok('Start new game')

        $mdDialog.show(gameWon).then(function () {
          $state.reload()
        });
    };

     $scope.showGameOver = function(ev) {
        let gameOver = $mdDialog.confirm()
          .title('GAME OVER!')
          .textContent('Click below to start a new game')
          .ariaLabel('Game over')
          .targetEvent(ev)
          .ok('Start new game')

        $mdDialog.show(gameOver).then(function () {
          $state.reload()
        });
    };

    $http.post('http://localhost:8000/api/initialise', JSON.stringify(defaultGrid)).then(function (response) {
        $rootScope.currentGrid = response.data.id
    }, function (response) {
        console.log(response.data)
    });

    $scope.safeSquares = (defaultGrid.rowsCount * defaultGrid.columnsCount) - defaultGrid.mineCount

    const board = jsboard.board({attach: "game", size:"4x4"});
    board.cell("each").style({background:"-80px -16px no-repeat", width:"64px", height:"64px", margin:"0", padding:"0", border:"1px solid black"});

    board.cell("each").on("click", function() {
        $scope.safeSquares -= 1
        const coordinates = board.cell(this).where()
        $http.get('http://localhost:8000/api/square/detailed', {headers:{row: coordinates[0], column: coordinates[1], grid: $rootScope.currentGrid}}).then(function(response) {
            let cellColour = 'lightGreen'
            if(response.data.value === -1) {
                cellColour = 'red'
            }
            const currentCell = jsboard.piece({ text: response.data.value.toString(), fontSize: "30px", textAlign: "center", backgroundColor: cellColour});
            board.cell([coordinates[0],coordinates[1]]).place(currentCell.clone())
            if(response.data.value === -1) {
                $scope.showGameOver();
                $http.delete('http://localhost:8000/api/grid/' + $rootScope.currentGrid).then(function(response) {
                    console.log("Board Deleted")
                }, function() {
                    console.log("Error deleting")
                })
            }
        }, function (response) {
            $scope.msg = "Error returning grid data.";
        });
        if($scope.safeSquares === 0) {
            $scope.showGameWon();
            $http.delete('http://localhost:8000/api/grid/' + $rootScope.currentGrid).then(function(response) {
                console.log("Board Deleted")
            }, function() {
                console.log("Error deleting")
            })
        }
    });
}])
