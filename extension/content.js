console.log("CHATGPT LOGGER LOADED");

async function captureConversation() {

    try {

        console.log("CAPTURE STARTED");

        const messages = document.querySelectorAll(
            '[data-message-author-role]'
        );

        let conversation = [];

        messages.forEach(msg => {

            conversation.push({

                role:
                    msg.getAttribute(
                        'data-message-author-role'
                    ),

                text:
                    msg.innerText
            });

        });

        if (conversation.length === 0) {

            console.log(
                "NO CHAT MESSAGES FOUND"
            );

            return;
        }

        const conversationText =
            conversation
                .map(
                    m =>
                        `${m.role.toUpperCase()}:\n${m.text}`
                )
                .join(
                    "\n\n====================\n\n"
                );

        const payload = {

            timestamp:
                new Date().toISOString(),

            title:
                document.title,

            content:
                conversationText
        };

        console.log(
            "SENDING MESSAGE TO BACKGROUND"
        );

        chrome.runtime.sendMessage(
            {
                type: "SAVE_CHAT",
                payload: payload
            },
            (response) => {

                if (
                    chrome.runtime.lastError
                ) {

                    console.error(
                        "RUNTIME ERROR:",
                        chrome.runtime.lastError.message
                    );

                    return;
                }

                console.log(
                    "SAVE RESPONSE:",
                    response
                );
            }
        );

        console.log(
            "MESSAGE SENT"
        );

    }
    catch (err) {

        console.error(
            "CAPTURE ERROR:",
            err
        );
    }
}

// Run once after page loads
setTimeout(
    captureConversation,
    5000
);

// Run every minute
setInterval(
    captureConversation,
    60000
);