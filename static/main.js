//API recognises in 2D array elements as 1 is normal place; element 0 is an obstacle; element -1 is meta; element 2 is start
const url = "http://127.0.0.1:8000/";
let buttonList = [];
let action = 0;

const FieldValues = {
    Normal: 1,
    Obstacle: 0,
    Meta: -1,
    Start: 2
}

function validateInput(xSize, ySize) {

    if (xSize <= 43 && xSize > 2 && ySize <= 60 && ySize > 2) return true;
    else return false;
}

//Create Table based on html input
function generateTable() {

    //reset table
    if (document.getElementById("map").hasChildNodes()) {
        const prevTables = document.getElementById("map").childNodes;
        document.getElementById("map").removeChild(prevTables[0]);
        buttonList = []
        action = 0;
    }

    //get data from the form
    const xSize = document.getElementById("X").value;
    const ySize = document.getElementById("Y").value;

    if (!validateInput(xSize, ySize)) {
        userInfo("Map size must be grater than 2 and smaler than 40")
        return;
    }

    // creates a <table> element and a <tbody> element
    const tbl = document.createElement("table");
    const tblBody = document.createElement("tbody");

    // creating all cells
    for (let i = 0; i < xSize; i++) {
        // creates a table row
        const row = document.createElement("tr");
        let buttonListRow = [];
        for (let j = 0; j < ySize; j++) {
            // Create a <td> element and a text node, make the text
            // node the contents of the <td>, and put the <td> at
            // the end of the table row
            const cell = document.createElement("td");
            const button = document.createElement("button");
            button.classList.add("table-button");
            button.style.background = "purple";
            button.onclick = function () { OnClickAction(button) };
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
    userInfo("Select Start Field")

}

// define behaovr of a button in table
function OnClickAction(button) {

    const thisButton = button;

    //value-color map
    if (action == 0) {
        thisButton.val = FieldValues.Start;
        action++;
        userInfo("Select Finish Field");
    }
    else if (action == 1 && thisButton.val != FieldValues.Start) {
        thisButton.val = FieldValues.Meta;
        action++;
        userInfo("Place the obstacles");
    }
    else if (action == 2 && thisButton.val == FieldValues.Obstacle) {
        thisButton.val = FieldValues.Normal;
    }
    else if (action == 2 && thisButton.val != FieldValues.Meta && thisButton.val != FieldValues.Start) {
        thisButton.val = FieldValues.Obstacle;
        userInfo("Place the obstacles and Click Start");
    }

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
        let element = row.map((element) => element.val);
        uploadData.push(element);
    });
    return uploadData;
}

// send json data from table
function send() {

    let uploadDataJSON = JSON.stringify({
        input_map: GenerateUploadData(buttonList)
    })

    fetch(url + "astar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: uploadDataJSON,
    })
        .then(response => response.json())
        .then(data => ColorPath(data))
        .then(data => Values(data))
        .catch((err) => {
            userInfo(err)
        });

    userInfo("Calculations Completed");

}

//Color optimal path on path
function ColorPath(data) {

    let path = data['Path'];

    //color Buttons on path from start to meta
    path.forEach(element => buttonList[element.Y][element.X].style.backgroundColor = 'orange');

    return data;
}

function Values(data) {

    let valuesOFFields = data['Values'];

    //color Buttons on path from start to meta

    for (let i = 0; i < valuesOFFields.length; i++) {
        // Loop through columns
        for (let j = 0; j < valuesOFFields[i].length; j++) {
            buttonList[i][j].textContent = valuesOFFields[i][j];
        }
    }

    return data;
}

function userInfo(text) {
    document.getElementById("info").innerHTML = "A star: " + text;
}