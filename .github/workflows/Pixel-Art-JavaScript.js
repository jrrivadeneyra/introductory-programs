//Pixel-Art-JavaScript

// Select color input
// Select size input
let height, width, color, cell, grid, canvas;

// When size is submitted by the user, call makeGrid()
document.getElementById('sizePicker').addEventListener("submit", function(event) {
    event.preventDefault();
    height = document.getElementById('inputHeight').value;
    width = document.getElementById('inputWidth').value;
    makeGrid(height, width);
})

function makeGrid(x, y) {
    canvas = document.getElementById('pixelCanvas');
    canvas.innerHTML = null;
    

    for (let i = 1; i <=x ; i++) {
        grid = document.createElement('tr');
        grid.setAttribute("id","table" + i);
        document.getElementById('pixelCanvas').append(grid);
        for (let j = 1; j <= y; j++) {
            cell = document.createElement('td');
            document.getElementById('table' + i).append(cell);
        }
    }
    // add cell color
    document.getElementById('pixelCanvas').addEventListener("click", function addColor(event) {
        color = document.getElementById('colorPicker').value;
        let clickedCell = event.target;
        if (clickedCell.cellIndex >= 0) {
            clickedCell.style.backgroundColor = colorPicker.value;
        }
    })
}
