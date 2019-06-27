// by Chtiwi Malek on CODICODE.COM

var mousePressed = false;
var lastX, lastY;
var ctx;
var points = {'hand':'r'};
var pointsCount = 0;
var points_obj = {};
var rescaling_07 = 0.6;
//var points_pack = '';
var image_number = 0;
var img_obj;
var current_image_object;
var current_image_name;


function InitThis() {

    get_img_from_server('', '')
    

    $('#myCanvas').mousedown(function (e) {
//        mousePressed = true;
        if (pointsCount == 11){
            return false;
        } else{
            pointName = String('point_' + pointsCount);
            Draw(ctx,
                e.pageX - $(this).offset().left,
                e.pageY - $(this).offset().top,
                true,
                pointName);

            var offset = $(this).offset();
            var X = Math.round((e.pageX - offset.left)/rescaling_07);
            var Y = Math.round((e.pageY - offset.top)/rescaling_07);
            points[pointName] = [X, Y];
            pointsCount += 1;
        }


        console.log('pointsCount_' + pointsCount)

        console.log('pointName_' + pointName);

//        $('#coord').append('<div>' + 'X: ' + X + ' Y: ' + Y + '</div>');
//        $('#points').append('<div>' + 'points' + points + '</div>');
    });

    // $('#myCanvas').mousemove(function (e) {
    //     if (mousePressed) {
    //         Draw(ctx, e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
    //     }
    // });

    $('#myCanvas').mouseup(function (e) {
        mousePressed = false;
    });

    $('#myCanvas').mouseleave(function (e) {
        mousePressed = false;
    });
}

function get_img_from_server(action_number, current_image_name_path){

    console.log('action_number==', action_number)
    console.log('current_image_name_path==', current_image_name_path)

    var params = JSON.stringify({'select_action': action_number, 'current_path': current_image_name_path});

//    var get_image = axios.post('http://127.0.0.1:5000/hands_markup/get_image', params);
    var get_image = axios.post('http://192.168.26.21:5000/hands_markup/get_image', params);
    get_image.then(r => {
        img_obj = r.data;
        show_image(img_obj);
    })

}


function show_image(img_obj){
    c = document.getElementById('myCanvas');
    ctx = c.getContext("2d");

    var img = new Image();

    console.log('img_obj.img_name++++' + img_obj.img_name);

    img_name = img_obj.img_name;
    img_str = img_obj.img_obj;
    img.src = img_str;

    current_image_object = img_obj;
    current_image_name = img_name;
    console.log('current_image_name==' + current_image_name)

    img.addEventListener('load', function() {
        img_width = this.naturalWidth * rescaling_07;
        img_height = this.naturalHeight * rescaling_07;

        c.height = img_height;
        c.width = img_width;

        ctx.drawImage(this, 0, 0, img_width, img_height)
    });
}


$(document).ready(function(){
    $('#send_points_to_server').click(function(){
        points_obj['file_name'] = current_image_name;
        points_obj['points'] = points;

//        axios.post('http://127.0.0.1:5000/hands_markup/save_points', JSON.stringify(points_obj));
        axios.post('http://192.168.26.21:5000/hands_markup/save_points', JSON.stringify(points_obj));

        get_img_from_server(2, current_image_name);
        clean();
    });
});

$(document).ready(function(){
    $('#previous_img').click(function(){

//        if (image_number > 0){
//            --image_number;
//        } else {
//            image_number = 0;
//        }
//        console.log('previous_img--' + image_number)
        get_img_from_server(1, current_image_name)
        clean();
    })
})


$(document).ready(function(){
    $('#next_img').click(function(){

//        ++image_number;
//
//        console.log('next_img' + image_number)
        get_img_from_server(2, current_image_name)
        clean()
    })
})

//$(document).ready(function(){
//    $('#clean_all').click(function(){
//        c = document.getElementById('myCanvas');
//        ctx = c.getContext("2d");
////        ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
//        clean()
//        get_img_from_server(image_number)
//    })
//})

$(document).ready(function(){
    $('#clean_all').click(function(){
        show_image(current_image_object);
        clean()
    })
})


function clean(){

    points = {'hand':'r'};
    pointsCount = 0;
    points_obj = {};
}


function Draw(ctx, x, y, isDown, pointName) {
    if (isDown) {
        ctx.fillStyle = "#0000FF";
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI*2, true);
        ctx.font = '10pt Calibri';
        ctx.fillText(pointName, x-20, y-10);
        ctx.closePath();
        ctx.fill();
    }
}

function clearArea(ctx) {
//    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}
window.onload=InitThis;
