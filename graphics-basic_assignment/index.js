
var canvas = document.createElement('canvas')
canvas.width = 400
canvas.height = 400
canvas.style.align='center'
// Get our WebGL Context that we'll use to pass data to the GPU
var gl = canvas.getContext('webgl')
gl.enable(gl.DEPTH_TEST)

// We create an input slider that will control our animations playback speed
// You can drag this slider to view the animation in either slow or fast motion
var playbackSlider = document.createElement('input')
playbackSlider.type = 'range'
playbackSlider.min = 0
playbackSlider.max = 2
playbackSlider.step = 0.01
playbackSlider.value = 1
playbackSlider.style.display = 'block'

// We create a display that shows us how fast our animation is playing
var speedDisplay = document.createElement('span')
speedDisplay.innerHTML = 'Playback Speed: 100%'

// Whenever we drag our input slider we update our playback speed
var playbackSpeed = 1
playbackSlider.oninput = function () {
  playbackSpeed = playbackSlider.value
  speedDisplay.innerHTML = 'Playback Speed: ' + (playbackSpeed * 100).toFixed(0) + '%'
}

// We insert our canvas and controls into the page
var demoLocation = document.querySelector('#animation assignment') || document.body
demoLocation.appendChild(canvas)
demoLocation.appendChild(playbackSlider)
demoLocation.appendChild(speedDisplay)

// Grab our model's JSON data that we'll use to know how to render it
var cowboyJSON = require('./cowboy.json')
// We convert our joint matrices into dual quaternions.
// Dual quaternions are easier to blend
// see: https://www.cs.utah.edu/~ladislav/kavan07skinning/kavan07skinning.pdf
var keyframesToDualQuats = require('keyframes-to-dual-quats')
cowboyJSON.keyframes = keyframesToDualQuats(cowboyJSON.keyframes)

var cowboyModel
var texture = new window.Image()
texture.onload = function () {
  // We buffer our 3d model data on the GPU so that we can later draw it
  var loadCollada = require('load-collada-dae')
  cowboyModel = loadCollada(gl, cowboyJSON, {texture: texture})
  gl.useProgram(cowboyModel.shaderProgram)
}
texture.src = '/cowboy-texture.png'

// We use the number of seconds that have elapsed to know
// how much to interpolate our model's joints
var secondsElapsed = 0

// We create a request animation frame loop in which we'll re-draw our
// animation every time the browser is ready for a new frame
var renderLoop = require('raf-loop')
var animationSystem = require('skeletal-animation-system')

renderLoop(function (millisecondsSinceLastRender) {
  // We don't try to draw our model until it's been loaded
  if (cowboyModel) {
    var uniforms = {
   
      uUseLighting: true,
      uAmbientColor: [0.75, 0.75, 0.75],
      // NOTE: This lighting direction needs to be a normalized vector
      uLightingDirection: [1, 0, 0],
      uDirectionalColor: [1, 0, 0],
      // Move the model back 27 units so we can see it
      uMVMatrix: [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0.0, 0.0, -30.0, 1],
      uPMatrix: require('gl-mat4/perspective')([], Math.PI / 4, 400 / 400, 0.1, 100)
    }

    // We calculate the dual quaternions for all of our joints at this
    // point in time. By passing these into our shader as uniforms our
    // model will be rendered at the correct pose for our time
    secondsElapsed += millisecondsSinceLastRender * playbackSpeed / 500
    var interpolatedJoints = animationSystem.interpolateJoints({
      currentTime: secondsElapsed,
      keyframes: cowboyJSON.keyframes,
      jointNums: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
      currentAnimation: {
        range: [6, 17],
        startTime: 0
      }
    }).joints

    // Add our joint's quaternions into our uniform data to pass to our vertex shader
    for (var i = 0; i < 18; i++) {
      uniforms['boneRotQuaternions' + i] = interpolatedJoints[i].slice(0, 4)
      uniforms['boneTransQuaternions' + i] = interpolatedJoints[i].slice(4, 8)
    }

    // We run a function that sets up and calls `gl.drawElements` in order to
    // draw our model onto the page
    cowboyModel.draw({
      attributes: cowboyModel.attributes,
      uniforms: uniforms
    })
  }
}).start()
