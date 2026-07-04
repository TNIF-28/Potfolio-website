const chatbox = document.getElementById('chatbox');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

// fuction to add a message to the chatbox
function addmessage(message) {
    const newMessage = document.createElement('div');
    newMessage.textContent = message;
    chatbox.appendChild(newMessage);
}

//Click Event on the send button
sendButton.addEventListener('click', function() {
    const message = messageInput.value;
    if (message !== '') {
        addmessage(message);
        messageInput.value = '';
    }
});

// click event of the enter key in the typing area
messageInput.addEventListener('keypress', function(event){
    if (event.key === 'Enter') {
        const message = messageInput.value;
        if (message != '') {
            addmessage(message);
            messageInput.value= '';
            
        }
    }
});