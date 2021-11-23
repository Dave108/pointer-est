    var player;
    var video_list;

    document.onreadystatechange = function(){
        if(document.readyState == 'interactive'){
            player = document.getElementById('player')
            video_list = document.getElementById('video_list')
            playerHeight()
        }
    }

    function playerHeight(){
        var w = player.clientWidth
        var h = (w*9)/16
        console.log({w,h});
        player.height = h
        video_list.style.maxHeight = h + "px"
    }

    window.onresize = playerHeight


    function sign_up_func(){
        console.log("sign up function");
            var sign_up = document.getElementById('sign_up');
            if (sign_up.className === "d-none"){
                sign_up.className = "";
                var z = document.getElementById('sign_in');
                z.className = "d-none";
            } else {
                sign_up.className = "d-none"
            }
    }
    function login_func(){
        console.log("login----function");
            var sign_in = document.getElementById('sign_in');
            if (sign_in.className === "d-none"){
                sign_in.className = "";
                var z = document.getElementById('sign_up');
                z.className = "d-none";
            } else{
                sign_in.className = "d-none"
            }

    }