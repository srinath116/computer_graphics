main();

function main() {
    const canvas = document.getElementById('glCanvas');
    const gl = canvas.getContext('2d');

    // Draws a wink smiley
    gl.beginPath();
    gl.arc(75, 75, 50, 0, Math.PI * 2, true); // Outer circle
    gl.moveTo(110, 75);
    gl.arc(75, 75, 35, 0, Math.PI, false); // Mouth (clockwise)
    gl.moveTo(65, 65);
    gl.arc(60, 65, 5, 0, Math.PI * 2, true); // Left eye
    gl.moveTo(95, 65);
    gl.arc(90, 65, 5, 0, Math.PI, true); // Right eye
    gl.stroke();
}
