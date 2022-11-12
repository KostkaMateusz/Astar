
//API recognises in 2D array elements as 1 is normal place; element 0 is an obstacle; element -1 is meta; element 2 is start
let buttonList = [];

let FieldValues = {
    Normal: 1,
    Obstacle: 0,
    Meta: -1,
    Start: 2
}


//Create Table
function generateTable() {
    //get data from the form
    var xSize = document.getElementById("X").value;
    var ySize = document.getElementById("Y").value;

    // creates a <table> element and a <tbody> element
    const tbl = document.createElement("table");
    const tblBody = document.createElement("tbody");

    // creating all cells
    for (let i = 0; i < xSize; i++) {
        // creates a table row
        const row = document.createElement("tr");
        var buttonListRow = [];
        for (let j = 0; j < ySize; j++) {
            // Create a <td> element and a text node, make the text
            // node the contents of the <td>, and put the <td> at
            // the end of the table row
            const cell = document.createElement("td");
            const button = document.createElement("button");
            button.classList.add("table-button");
            button.style.background = "purple";
            button.onclick = function (button) { OnClickAction(button) };
            button.val = FieldValues.Normal;
            buttonListRow.push(button);
            cell.appendChild(button);
            row.appendChild(cell);
        }

        buttonList.push(buttonListRow);
        // add the row to the end of the table body
        tblBody.appendChild(row);
    }

    // put the <tbody> in the <table>
    tbl.appendChild(tblBody);
    tbl.setAttribute('id', "table-map");
    // appends <table> into <body>
    document.getElementById("map").appendChild(tbl);
    // document.body.appendChild(tbl);

}


function OnClickAction(button) {

    const thisButton = button.path[0];

    //value-color map
    if (thisButton.val == 2) thisButton.val = FieldValues.Meta;
    else if (thisButton.val == -1) thisButton.val = FieldValues.Obstacle;
    else if (thisButton.val == 0) thisButton.val = FieldValues.Normal;
    else if (thisButton.val == 1) thisButton.val = FieldValues.Start;

    // change color based on value
    switch (thisButton.val) {
        case FieldValues.Meta:
            thisButton.style.backgroundColor = "yellow";
            break;
        case FieldValues.Obstacle:
            thisButton.style.backgroundColor = "red";
            break;
        case FieldValues.Normal:
            thisButton.style.backgroundColor = "purple";
            break;
        case FieldValues.Start:
            thisButton.style.backgroundColor = "green";
            break;
    }

}

// take value from button list
function GenerateUploadData(tableOfButtons) {

    let uploadData = [];

    tableOfButtons.forEach(row => {
        var element = row.map((element) => element.val);
        uploadData.push(element);
    });
    return uploadData;
}

function send() {

    let uploadDataJSON = JSON.stringify({
        input_map: GenerateUploadData(buttonList)
    })

    fetch("http://127.0.0.1:8000/astar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: uploadDataJSON,
    }).then(response => response.json())
        .then(data => ColorPath(data));
}

function ColorPath(data) {

    var path = data['Path'];
    //color Buttons on path from start to meta
    path.forEach(element => buttonList[element.Y][element.X].style.backgroundColor = 'orange');
}


