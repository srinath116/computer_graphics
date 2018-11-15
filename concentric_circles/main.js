main();

function main() {
    const canvas = document.getElementById('glCanvas');
    const gl = canvas.getContext('2d');

    if(gl === null) {
        alert('Unable to initialise context');
    }

    // Drawing concentric circles
    for(let i = 25; i <= 75; i+= 25) {
        console.log(i);
        gl.beginPath();
        gl.arc(100, 100, i, 0, 2 * Math.PI);
        gl.lineWidth = 3;
        if(i === 25) {
            gl.strokeStyle = '#CB2B09';
        }
        else if(i === 50) {
            gl.strokeStyle = '#05A640';
        }
        else if(i === 75) {
            gl.strokeStyle = '#0516A6';
        }
        gl.stroke();
    }
}