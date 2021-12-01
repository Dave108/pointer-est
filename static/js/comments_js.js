function open_comments(){
console.log("open_pin----function");
    var pindiv = document.getElementById('comments_section');
    if (pindiv.className === "comment-form d-none"){
        pindiv.className = "comment-form";
    } else{
        pindiv.className ="comment-form d-none";
    }
    }