/*global app,$SCRIPT_ROOT,alertify*/

app.factory('tasksService', ['$http', function ($http) {
    'use strict';
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    var getTasks = function () {
        return $http.get('/api/tasks/')
            .then(function (response) {
                    if ('error' in response.data) {
                        throw response.data.error;
                    } else {
                        return response.data
                    }
                },
                function (error) {
                    throw error.statusText;
                });
    };

    var getTask = function (id) {
        return $http.get('/api/tasks/' + id + '/')
            .then(function (response) {
                    if ('error' in response.data) {
                        throw response.data.error;
                    } else {
                        return response.data
                    }
                },
                function (error) {
                    throw error.statusText;
                });
    };

    var updateStatus = function (id, value) {
        return $http({
            url: '/api/tasks/status/' + id + '/',
            method: "PUT",
            headers: { 'Content-Type': 'application/json', 'X-CSRFTOKEN': csrftoken },
            data: {status: value}
        })
    };

    var updateTask = function (id, task) {
        var url;
        var method;
        if(!angular.isUndefined(id)){
            url = '/api/tasks/' + id + '/';
            method = "PUT";
        }else{
            url = '/api/tasks/';
            method = "POST";
        }
        return $http({
            url: url,
            method: method,
            headers: { 'Content-Type': 'application/json', 'X-CSRFTOKEN': csrftoken },
            data: task
        }).then(function (response) {
                if ('error' in response.data) {
                    throw response.data.error;
                } else {
                    return response.data
                }
            },
            function (error) {
                if(error.status == 403){
                    alertify.error('You can edit only your tasks');
                }else{
                    throw response.data.error;
                }
            });
    };

    return {
        getTasks: getTasks,
        getTask: getTask,
        updateStatus: updateStatus,
        updateTask: updateTask
    };

}]);
