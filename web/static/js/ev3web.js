$(document).ready(function() {

    $('#ArrowUp').mousedown(function() {
        console.log('ArrowUp down')
        var ip = document.domain
        var power = 60
        var ajax_url = "http://" + ip + ":5000/move/forward"

        $.ajax({
            type: "GET",
            crossDomain: true,
            dataType: 'jsonp',
            url: ajax_url,
            success: function() {
            }
        });
        return false;
    });

    $('#ArrowDown').mousedown(function() {
        console.log('ArrowDown down')
        var ip = document.domain
        var power = 60
        var ajax_url = "http://" + ip + ":5000/move/backward"

        $.ajax({
            type: "GET",
            crossDomain: true,
            dataType: 'jsonp',
            url: ajax_url,
            success: function() {
            }
        });
        return false;
    });

    $('#ArrowLeft').mousedown(function() {
        console.log('ArrowLeft down')
        var ip = document.domain
        var power = 60
        var ajax_url = "http://" + ip + ":5000/move/left?forever=1"

        $.ajax({
            type: "GET",
            crossDomain: true,
            dataType: 'jsonp',
            url: ajax_url,
            success: function() {
            }
        });
        return false;
    });

    $('#ArrowRight').mousedown(function() {
        console.log('ArrowRight down')
        var ip = document.domain
        var power = 60
        var ajax_url = "http://" + ip + ":5000/move/right?forever=1"

        $.ajax({
            type: "GET",
            crossDomain: true,
            dataType: 'jsonp',
            url: ajax_url,
            success: function() {
            }
        });
        return false;
    });

    $('#head-spin .CounterClockwise').mousedown(function() {
        console.log('CounterClockwise down')
        var ip = document.domain
        var power = 60
        var ajax_url = "http://" + ip + ":5000/move-start/lookleft/" + power + "/"

        $.ajax({
            type: "GET",
            crossDomain: true,
            dataType: 'jsonp',
            url: ajax_url,
            success: function() {
            }
        });
        return false;
    });

    $('#head-spin .Clockwise').mousedown(function() {
        console.log('Clockwise down')
        var ip = document.domain
        var power = 60
        var ajax_url = "http://" + ip + ":5000/move-start/lookright/" + power + "/"

        $.ajax({
            type: "GET",
            crossDomain: true,
            dataType: 'jsonp',
            url: ajax_url,
            success: function() {
            }
        });
        return false;
    });

    $('.button').mouseup(function() {
        console.log('Button release')
        var ip = document.domain
        var ajax_url = "http://" + ip + ":5000/move/stop"

        $.ajax({
            type: "GET",
            crossDomain: true,
            dataType: 'jsonp',
            url: ajax_url,
            success: function() {
            }
        });
        return false;
    });

});
