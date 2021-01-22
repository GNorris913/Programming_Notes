
var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
var canvasWidth = canvas.width
var canvasHeight = canvas.height

context.clearRect(0,0, canvasWidth, canvasHeight)
context.fillStyle = "Blue";
context.fillRect(0, 0, 480, 480);




const colorRect = (x,y)=> {
    
    context.fillStyle = "White";
    context.fillRect(x, y, 48, 48);}

var z=0
const MAX_ITERATION = 100
function mandelbrot(x,y){
    var i = 0;
    var cx = 2+x/50;
    var cy = -2+y/50;
    var zx = 0;
    var zy = 0;
    while(i<MAX_ITERATION&&(zx*zx+zy*zy)<4)
    {
        var xt=zx*zy;
        zx=zx*zx-zy*zy+cx;
        zy=2*xt+cy;
        i++;
    }

    var i=color.toString(16);
    context.beginPath();
    context.rect(x*4, y*4, 4, 4);
    context.fillStyle ='#'+color+color+color;
    context.fill();
}
for (var y=0; y<100; y++){
    for(var x=0; x<100; x++){
        mandelbrot(x,y)

    }
}

