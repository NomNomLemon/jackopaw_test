/*global app,alertify*/

app.controller('ListCtrl', ['$scope', '$uibModal', 'tasksService',
    function ($scope, $uibModal, tasksService) {
        'use strict';
        $scope.tasks = [];
        $scope.reloadTasks = function () {
            tasksService.getTasks()
                .then(function (data) {
                    $scope.tasks = data;
                })
        };
        $scope.updateStatus = function (id, value) {
            tasksService.updateStatus(id, value)
                .then(function(){
                    $scope.reloadTasks();
                    alertify.success('Task successfully updated')
                })
        };
        $scope.reloadTasks();

        $scope.editTask = function(task){
            var modalInstance = $uibModal.open({
                    animation: false,
                    templateUrl: 'edit-task-modal.html',
                    controller: 'editTaskCtrl',
                    size: 'lg',
                    resolve: {
                        task: function () {
                            return task
                        }
                    }
                });
            };
        $scope.$on('updateTasks', $scope.reloadTasks);
    }]);

app.controller('editTaskCtrl', ['$scope', '$rootScope', '$uibModalInstance', 'task', 'tasksService',
    function ($scope, $rootScope, $uibModalInstance, task, tasksService) {
        'use strict';
        $scope.task = {};
        $scope.parentTask = task;
        angular.copy(task,  $scope.task);
        $scope.close = function () {
            $uibModalInstance.close();
        };
        $scope.saveTask = function (id) {
            tasksService.updateTask(id, $scope.task)
                .then(function(data){
                    $uibModalInstance.close();
                    $rootScope.$broadcast('updateTasks');
                    alertify.success('Task successfully updated')
                })
        }
    }]);