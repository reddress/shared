var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

var geometry = new THREE.CubeGeometry(1, 1, 1);
var material = new THREE.MeshLambertMaterial({ color: 0x00ffff });
var cube = new THREE.Mesh(geometry, material);
scene.add(cube);

var directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
directionalLight.position.set(2, 1, 0);
scene.add(directionalLight);

var light = new THREE.AmbientLight(0xffcc00);
scene.add(light);

camera.position.z = 5;

function render() {
  requestAnimationFrame(render);
  cube.rotation.x += 0.1;
  cube.rotation.y += 0.1;
  renderer.render(scene, camera);
}

render();
