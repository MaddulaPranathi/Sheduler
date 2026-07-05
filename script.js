function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const userText = input.value;

    if (userText.trim() === "") return;

    const userMsg = document.createElement("div");
    userMsg.textContent = "You: " + userText;
    chatBox.appendChild(userMsg);

    // Call your Render backend
    fetch("https://sheduler-1.onrender.com/add_reminder", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: userText })
    })
    .then(res => res.json().then(data => ({ ok: res.ok, data })))
    .then(({ ok, data }) => {
        const botMsg = document.createElement("div");
        if (ok) {
            botMsg.textContent = `Bot: Reminder Saved for '${data.task}' at ${data.time}`;

            // 🔔 Show browser notification
            if (Notification.permission === "granted") {
                new Notification("Reminder", { body: `${data.task} at ${data.time}` });
            } else {
                Notification.requestPermission().then(permission => {
                    if (permission === "granted") {
                        new Notification("Reminder", { body: `${data.task} at ${data.time}` });
                    }
                });
            }
        } else {
            botMsg.textContent = `Bot: ${data.error || 'Invalid input'}`;
        }
        chatBox.appendChild(botMsg);
        input.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(err => {
        const botMsg = document.createElement("div");
        botMsg.textContent = "Bot: Failed to connect to backend.";
        chatBox.appendChild(botMsg);
        input.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
        console.error(err);
    });
}
