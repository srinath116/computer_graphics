// Add scene, camera, renderer of Three.js
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create a cube to be supplied to the scene
var geometry1 = new THREE.SphereGeometry(10, 12, 12);
var material1 = new THREE.MeshBasicMaterial({ color: '#4285F4', side: THREE.DoubleSide });
var cube1 = new THREE.Mesh(geometry1, material1);
var geometry2 = new THREE.SphereGeometry(10, 12, 12);
var material2 = new THREE.MeshBasicMaterial({ color: '#DB4437', side: THREE.DoubleSide });
var cube2 = new THREE.Mesh(geometry2, material2);

var xDistance = 60;
var xOffset = -30;
cube1.position.x = xDistance + xOffset;
scene.add(cube1);
scene.add(cube2);

// Set camera position
camera.position.z = 300;

// Rendering the scene
var dxPerFrame = 2;
function animate() {
    console.log(cube1.position.z);
    console.log(cube2.position.z);
    requestAnimationFrame(animate);
    cube1.position.y += dxPerFrame;
    cube2.position.y += dxPerFrame;
    cube1.position.z += dxPerFrame;
    cube2.position.z += dxPerFrame;
    if(cube1.position.y > 100) {
        dxPerFrame = -1;
    }
    if(cube1.position.y < -100) {
        dxPerFrame = 1;
    }
    if(cube2.position.y > 100) {
        dxPerFrame = -1;
    }
    if(cube2.position.y < -100) {
        dxPerFrame = 1;
    }
    renderer.render(scene, camera);
}

animate();

