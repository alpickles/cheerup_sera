// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
    const generateBtn = document.getElementById("generate-btn");
    const promptTextElement = document.getElementById("prompt-text");
    const copyBtn = document.getElementById("copy-btn");

    // Function to fetch and update the prompt message
    async function fetchNewMessage() {
        try {
            // Show loading message or spinner
            promptTextElement.textContent = "Loading...";

            // Fetch a new prompt from the backend
            const response = await fetch('/generate');
            const data = await response.json();
            promptTextElement.textContent = data.prompt_text; // Update the prompt text on the page

            // Update the URL with the new message (this keeps the message persistent on refresh)
            history.pushState({}, '', '/prompt?message=' + encodeURIComponent(data.prompt_text));
        } catch (error) {
            console.error("Error fetching the new prompt:", error);
            promptTextElement.textContent = "Oops! Something went wrong. Please try again later.";
        }
    }

    // Event listener for generating a new message
    generateBtn.addEventListener("click", fetchNewMessage);

    // Event listener for copying the message to clipboard (for mobile users, especially on iPhones)
    copyBtn.addEventListener("click", () => {
        const text = promptTextElement.textContent;

        if (text && text !== "Click the button to get a new message!") {
            // Use the modern Clipboard API
            navigator.clipboard.writeText(text)
                .then(() => {
                    alert("Message copied to clipboard!");
                })
                .catch(err => {
                    console.error("Failed to copy text: ", err);
                    alert("There was an error copying the message.");
                });
        } else {
            alert("There's no message to copy yet. Please generate one first.");
        }
    });

    // Check if there's a message in the URL (to persist the message on page reload)
    const urlParams = new URLSearchParams(window.location.search);
    const messageFromUrl = urlParams.get('message');
    if (messageFromUrl) {
        promptTextElement.textContent = decodeURIComponent(messageFromUrl);
    } else {
        promptTextElement.textContent = "Click the button to get a new message!";
    }
});
