const button = document.getElementById("sendBtn");

button.addEventListener("click", async () => {

    const message = document.getElementById("message").value;

    const reply = document.getElementById("reply");

    reply.textContent = "Loading...";

    try {

        const response = await fetch("/chat",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                message
            })
        });

        const data = await response.json();

        if(data.success){
            reply.textContent = data.data.reply;
        }else{
            reply.textContent = data.message;
        }

    } catch(error){

        reply.textContent = error.message;

    }

});