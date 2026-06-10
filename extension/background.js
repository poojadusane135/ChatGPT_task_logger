console.log("BACKGROUND STARTED");

chrome.runtime.onMessage.addListener(
    (message, sender, sendResponse) => {

        console.log(
            "MESSAGE RECEIVED",
            message
        );

        if (
            message.type === "SAVE_CHAT"
        ) {

            console.log(
                "POSTING TO FLASK"
            );

            fetch(
                "http://localhost:5000/save_chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify(
                        message.payload
                    )
                }
            )
            .then(
                response => response.json()
            )
            .then(data => {

                console.log(
                    "FLASK RESPONSE",
                    data
                );

                sendResponse(data);
            })
            .catch(err => {

                console.error(
                    "FETCH FAILED",
                    err
                );

                sendResponse({
                    error:
                        err.message
                });
            });

            return true;
        }
    }
);