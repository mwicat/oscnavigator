$.widget("custom.musictable", {

    options: {
        cellwidth: 100,
        cellheight: 100
    },


    _create: function () {
        var doc = document;
        var fragment = doc.createDocumentFragment();
        var self = this;

        for (var row = 0; row < this.options.rows; row++) {
            var tr = doc.createElement("tr");

            for (var col = 0; col < this.options.columns; col++) {
                var td = doc.createElement("td");
                td.setAttribute("width", this.options.cellwidth);
                td.setAttribute("height", this.options.cellheight);
                td.style.textAlign = 'center';
                td.style.borderWidth = "1px";
                td.style.borderColor = "#000";
                td.style.borderStyle = "solid";


                td.onclick = function () {

                    var td_row = parseInt($(this).parent().index());
                    var td_col = parseInt($(this).index());

                    self._trigger("cellclick", null, {
                        row: td_row,
                        column: td_col
                    });
                };

                tr.appendChild(td);
            }
            fragment.appendChild(tr);
        }

        this.table = doc.createElement("table");
        this.table.setAttribute("border", "1px");

        this.table.style.borderCollapse = "collapse";
        this.table.style.borderWidth = "1px";
        this.table.style.borderColor = "#000";
        this.table.style.borderStyle = "solid";

        this.table.appendChild(fragment);

        this.element[0].appendChild(this.table);

        this.element.addClass("musictable");
        this.refresh();

    },

    _setOption: function (key, value) {
        this._super(key, value);
    },

    _setOptions: function (options) {
        this._super(options);
        this.refresh();
    },

    refresh: function () {
    },

    setCell: function (row, col, color, text) {
        var td = this.table.rows[row].cells[col];
        td.setAttribute("bgcolor", color);
        if (text !== undefined) {
            td.innerHTML = '<font color="white">' + text + '</font>';
        }
    },

    unsetCell: function (row, col) {
        var td = this.table.rows[row].cells[col];
        td.removeAttribute("bgcolor");
    },

    setColumn: function (col, color) {
        for (var row = 0; row < this.table.rows.length; row++) {
            this.setCell(row, col, color);
        }
    },

    unsetColumn: function (col) {
        for (var row = 0; row < this.table.rows.length; row++) {
            this.unsetCell(row, col);
        }
    }

});
