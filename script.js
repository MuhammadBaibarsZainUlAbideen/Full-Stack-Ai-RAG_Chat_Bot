const messageInput = document.getElementById("Message");
const idInput = document.getElementById("ID");
const userMessageDiv = document.getElementById("chatBox");
const botMessageDiv = document.getElementById("chatBox");
const button = document.getElementById("submit_button");
const uplaod_file = document.getElementById("file_upload")
const paying = document.getElementById("pay")
const payingb = document.getElementById("Paying")
function scrollToBottom() {
    const chatBox = document.getElementById("chatBox");
    chatBox.scrollTop = chatBox.scrollHeight;
}
let counting = 0;

async function gp(event) {

    event.preventDefault(); 
    // counting +=1;
    // console.log("Count is :",counting)
    // if(counting == 2){
    //     document.getElementById("container").classList.add("hidden");
    //     paying.className = "h-screen w-screen flex flex-col items-center justify-center"
    //     payingb.textContent = "Pay to continues"
        


    // }
    uid1 = user.uid;
    console.log(uid1)
    const ff = new FormData()
    ff.append("id",uid1)
    try{
        const response = await fetch("http://127.0.0.1:8000/paywall",{
            method:"POST",
            body:ff,

        })
        const r = await response.json()
        what = r.paywall
        if(what == 1){
            document.getElementById("container").classList.add("hidden");
            paying.className = "h-screen w-screen flex flex-col items-center justify-center"
            payingb.textContent = "Pay to continues"
        }z

    }catch(error){
        console.log(error)
    }
    

    const message = messageInput.value.trim();


    const userMsg = document.createElement("div");
    userMsg.textContent = message;
    userMsg.className = "text-green-500 font-minecraft rounded-none max-w-10xs self-end p-2 mt-2";
    
    userMessageDiv.appendChild(userMsg);


    const formData = new FormData();
    formData.append("message", message);
    scrollToBottom()

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            body: formData,
            credentials: "include"
        });
        console.log("baba")

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        console.log("baba1")

        const data = await response.json();
        const botMsg = document.createElement("div");
        botMsg.textContent = data.reply;
        botMsg.className = "text-red-500 p-2 font-minecraft rounded-none max-w-10xs self-start p-2 mt-2";
        botMessageDiv.appendChild(botMsg);
        scrollToBottom()

    } catch (error) {
        const errorMsg = document.createElement("p");
        errorMsg.textContent = "Bot: Error sending message.";
        botMessageDiv.appendChild(errorMsg);
    }

    messageInput.value = "";
}


button.addEventListener("click", gp);


messageInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        gp(event);
    }
});




























// async function testing(event){
//     event.preventDefault()
//     if(uplaod_file.files.length>0){
//         const file = uplaod_file.files[0]
//         const name = file.name
//         if (name.toLowerCase().endsWith(".jpg") || name.toLowerCase().endsWith(".png") || name.toLowerCase().endsWith(".gif")){
//             const formData = new FormData();
//             formData.append("uploaded_image",file)
//             const image_resposne = await fetch("http://127.0.0.1:8000/uploadimage",{
//                 method : "POST",
//                 body : formData,
//                 credentials:"include"
            
//             })
//             const rdata = await image_resposne.json();
//             console.log("pup")
//             const botMsg1 = document.createElement("div");
//             botMsg1.textContent = rdata.reply;
//             botMsg1.className = "text-red-500 p-2 font-minecraft rounded-none max-w-10xs self-start p-2 mt-2";
//             botMessageDiv.appendChild(botMsg1);
//             scrollToBottom()



//         }
//         if (name.toLowerCase().endsWith(".pdf") || name.toLowerCase().endsWith(".txt")){
//             const formData = new FormData();
//             formData.append("uploaded_file",file)
//             const file_resposne = await fetch("http://127.0.0.1:8000/uploadfile",{
//                 method : "POST",
//                 body : formData,
//                 credentials:"include"
            
//             })
//             const rdata = await file_resposne.json();
//             console.log("pup")
//             const botMsg12 = document.createElement("div");
//             botMsg12.textContent = rdata.reply;
//             botMsg12.className = "text-red-500 p-2 font-minecraft rounded-none max-w-10xs self-start p-2 mt-2";
//             botMessageDiv.appendChild(botMsg12);
//             scrollToBottom()

//         }

//     }

// }

// uplaod_file.addEventListener('change',testing)




