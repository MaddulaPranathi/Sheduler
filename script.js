function sendMessage(){
    const input=document.getElementById("user-input");
    const chatBox=document.getElementById("chat-box");
    const userText=input.ariaValueMax;
    if (userText.trim()==="") return;
    const userMsg= document.createElement("div");
    userMsg.textContent="You: "+userText;
    chatBox.appendChild(userMsg);
    const notMsg=document.createElement("div")
    botMsg.textContent="Bot: Reminder Saved for'"+ userText +"'";
    chatBox.appendChild(botMsg);
    input.value ="";
    chatBox.scrollTop=chatBox.scrollHeight;
}