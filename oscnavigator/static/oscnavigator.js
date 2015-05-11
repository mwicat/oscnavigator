function oncellclick(event, data) {
    alert('clicked ' + data.row + ',' + data.column);
}

var nrows = 3;
var ncols = 3;


$(function () {

    var mtable = $("#musictable")
        .musictable({
            rows: nrows,
            columns: ncols,
            cellclick: oncellclick
        });

    var inbox = new WebSocket("ws://" + location.host + "/notes");

    inbox.onmessage = function (message) {
        var msg = JSON.parse(message.data);
        var color = degree_colors[msg['degree']-1];
        var row = nrows - msg['degree'];
        var col = msg['index'];
        if (col > 0) {
            mtable.musictable("unsetColumn", col-1);
        }
        mtable.musictable("setColumn", col, "grey");
        //mtable.musictable("setCell", row, col, color, '');
    };

    function play() {
        $.get("/play", {song: "mojsong"});
    }

    $("#play").on("click", play);

});
