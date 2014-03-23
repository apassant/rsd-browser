## Controller
RSDController = ($scope, $http, $sce) ->

    $scope.trustAsHTML = (html) ->
        $sce.trustAsHtml(html)
    
    $http.get('./assets/rsd.json').success (data) ->
        $scope.releases = data

## Filter
filterSelected = () ->
    (releases, selected=false) ->
        return releases if not selected
        return (release for release in releases when release.selected)
  
## App
rsd = angular.module 'RSD', ['ui.bootstrap', 'ui.bootstrap.popover']
rsd.controller 'RSDController', RSDController
rsd.filter 'filterSelected', filterSelected