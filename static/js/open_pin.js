
function open_pin(){
console.log("open_pin----function");
    var pindiv = document.getElementById('add-pin');
    if (pindiv.className === "d-none"){
        pindiv.className = "";
    } else{
        pindiv.className ="d-none";
    }
    }


function show_board(){
console.log("open_pin----function");
    var tag = document.getElementById('select-board');
    var newboard = document.getElementById('new-board');
    if (tag.className === "d-none"){
        tag.className = "";
        newboard.className = "d-none";
    } else{
        tag.className ="d-none";
    }
    }


function show_new_tag(){
console.log("open_pin----function");
    var tag = document.getElementById('new-board');
    var selectboard = document.getElementById('select-board');
    if (tag.className === "d-none"){
        tag.className = "";
        selectboard.className ="d-none";
    } else{
        tag.className ="d-none";
    }
    }



function show_tag_div(){
console.log("open_pin----function");
var tag = document.getElementById('tags');
    var newboard = document.getElementById('new-tag');
    if (tag.className === "d-none"){
        tag.className = "";
        newboard.className = "d-none";
    } else{
        tag.className ="d-none";
    }
}

function show_new_tag_div(){
console.log("open_pin----function");
    var tag = document.getElementById('new-tag');
    var selectboard = document.getElementById('tags');
    if (tag.className === "d-none"){
        tag.className = "";
        selectboard.className ="d-none";
    } else{
        tag.className ="d-none";
    }

}