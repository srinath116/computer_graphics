main();

function main() {
    const canvas = document.getElementById('glCanvas');
    const gl = canvas.getContext('2d');

    if (gl === null) {
        alert('Unable to initialise context');
    }

    // Drawing lot of circles with different shades
    for (let i = 0; i < 9; i++) {
        gl.beginPath();
        gl.arc(200, 200, i*1.5 + 150, 0, 2 * Math.PI);
        gl.lineWidth = 5;
        console.log(i);
        if(i === 0) {
            gl.strokeStyle = 'gainsboro';
        }
        else if(i === 1) {
            gl.strokeStyle = 'lightgray';
        }
        else if(i === 2) {
            gl.strokeStyle = 'silver';
        }
        else if(i === 3) {
            gl.strokeStyle = 'darkgray';
        }
        else if(i === 4) {
            gl.strokeStyle = 'gray';
        }
        else if(i === 5) {
            gl.strokeStyle = 'dimgray';
        }
        else if(i === 6) {
            gl.strokeStyle = 'lightslategray';
        }
        else if(i === 7) {
            gl.strokeStyle = 'slategray';
        }
        else if(i === 8) {
            gl.strokeStyle = 'darkslategray';
        }
        gl.stroke();
        gl.closePath();
    }
}