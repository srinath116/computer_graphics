main();
function main() {
    const canvas = document.getElementById('glCanvas');
    const gl = canvas.getContext('2d');

    gl.beginPath();
    gl.fillRect(100, 100, 100, 100);
    gl.stroke();
    gl.closePath();

    gl.beginPath();
    gl.fillStyle = 'blue';
    gl.fillRect(180, 110, 100, 100);
    gl.closePath();
}