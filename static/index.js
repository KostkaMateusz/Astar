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
        random: true,
        weight: weight.value,
        number_of_obstacles: number_of_obstacles.value,
    });

    fetch("https://fastapi-a-star.herokuapp.com/engine", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: data,
    })
        .then((response) => response.arrayBuffer())
        .then((data) => {

            const arrayBufferView = new Uint8Array(data);
            const blob = new Blob([arrayBufferView], { type: "image/png" });
            const urlCreator = window.URL || window.webkitURL;
            const imageUrl = urlCreator.createObjectURL(blob);
            const img = document.querySelector("#photo");
            img.src = imageUrl;
        })
        .catch((err) => {
            console.log(err)
        })
}