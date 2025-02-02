document.getElementById("rock").addEventListener("click", () => playGame("rock"));
document.getElementById("paper").addEventListener("click", () => playGame("paper"));
document.getElementById("scissors").addEventListener("click", () => playGame("scissors"));

function playGame(playerChoice) {
    fetch("/play", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ choice: playerChoice }),
    })
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("computer-choice").textContent = `Computer's Choice: ${data.computer_choice}`;
        document.getElementById("result").textContent = `Result: ${data.result}`;
    });
}