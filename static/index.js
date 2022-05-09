function sendJSON() {
    const result = document.querySelector(".result");
    const map_size_x = document.querySelector("#map_size_x");
    const map_size_y = document.querySelector("#map_size_y");
    const start_x = document.querySelector("#start_x");
    const start_y = document.querySelector("#start_y");
    const end_x = document.querySelector("#end_x");
    const end_y = document.querySelector("#end_y");
    const weight = document.querySelector("#weight");
    const number_of_obstacles = document.querySelector("#number_of_obstacles");


    const data = JSON.stringify({
        map_size_x: map_size_x.value,
        map_size_y: map_size_y.value,
        start_x: start_x.value,
        start_y: start_y.value,
        end_x: end_x.value,
        end_y: end_y.value,
        weight: weight.value,
        number_of_obstacles: number_of_obstacles.value,
    });

    fetch("http://127.0.0.1:8000/astar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: data,
    })
        .then(response => response.json())
        .then(data => createTable(data));

}

function createTable(input) {
    var data = input.table;
    var path = input.path;
    var table = '<table >';

    for (i = 0; i <= data.length - 1; i++) {
        table += "<tr>";
        for (j = 0; j <= data[0].length - 1; j++) {
            if (checkIfPath(i, j, path))
                table += "<td class=" + "greenElement" + ">" + data[i][j].F + "</td>";
            else if (data[i][j].V == 0)
                table += "<td class=" + "redElement" + ">" + data[i][j].F + "</td>";
            else
                table += "<td class=" + "Element" + ">" + data[i][j].F + "</td>";
        }
        table += "</tr>";
    }
    table += "</table>";

    document.getElementById("result").innerHTML = table;
}

function checkIfPath(x, y, path) {

    for (var element of path) {
        if (x === element[0] && y === element[1]) return true;

    }
    return false
}
