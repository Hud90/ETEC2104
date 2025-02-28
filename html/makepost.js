"use strict";

function submit(){
    let post_name = document.getElementById("name").value;
    let picfiles = document.getElementById("pic").files;
    if (picfiles.length === 0)
    {
        console.log("Error");
        return;
    }
    let fdata = new FormData();
    fdata.append("name", post_name)
    fdata.append("pic", picfiles[0])
    
    fetch( "/make_post", {
        method: "POST",
        body: fdata
    }).then( (resp) => {
        resp.json().then( (J) => {
            console.log("Server said:",J);

            // Check if the server responded with success
            if (J.ok) {
                // Redirect to another page after successful post
                document.location.href = '/';   // Home page
            } else {
                alert("Error: " + J.reason); // Show error if post failed
            }
        }).catch( (err) => {
            console.log("JSON error:",err);
        })
    }).catch( (err) => {
        console.log("Error:",err);
    });
}

function updatethumb(){
    let picfiles = document.getElementById("pic").files;
    if(picfiles.length > 0){
        let u = URL.createObjectURL(picfiles[0]);
        let th = document.getElementById("thumbnail");
        th.onload = () => {
            URL.revokeObjectURL(u);
        };
        th.src = u;
    }
}

