async function fetchAlerts() {
    const response = await fetch("http://localhost:5000/alerts");
    const data = await response.json();

    const alertContainer = document.getElementById("alerts");
    alertContainer.innerHTML = "";

    data.forEach(alert => {
        const div = document.createElement("div");
        div.className = "alert " + alert.severity;
        div.innerHTML = `
            <strong>${alert.severity} Alert</strong><br>
            ${alert.description}<br>
            <small>${alert.timestamp}</small>
        `;

        if (alert.severity === "High") {
            playSound("alert_high.wav");
        }

        alertContainer.appendChild(div);
    });
}

async function fetchLogs() {
    const response = await fetch("http://localhost:5000/logs");
    const data = await response.json();

    const logContainer = document.getElementById("logs");
    logContainer.innerHTML = "";

    data.forEach(log => {
        const div = document.createElement("div");
        div.className = "log";
        div.innerHTML = `
            <strong>${log.timestamp}</strong> — ${log.message}
        `;
        logContainer.appendChild(div);
    });
}

function playSound(file) {
    const audio = document.getElementById("alert-sound");
    audio.src = "sounds/" + file;
    audio.play();
}

// Auto refresh every 5 seconds
setInterval(() => {
    fetchAlerts();
    fetchLogs();
}, 5000);

// Load immediately on page open
fetchAlerts();
fetchLogs();
