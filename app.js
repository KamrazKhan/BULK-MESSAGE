async function sendMessages() {
    const numbersText = document.getElementById('numbers').value;
    const message = document.getElementById('message').value;
    const statusDiv = document.getElementById('status');

    // Split numbers by line
    const numbers = numbersText
        .split('\n')
        .map(n => n.trim())
        .filter(n => n.length > 0);

    if (numbers.length === 0 || message.trim() === '') {
        showStatus('Please enter phone numbers and a message.', 'error');
        return;
    }

    showStatus(`Sending to ${numbers.length} numbers...`, 'success');

    try {
        const response = await fetch('/send', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ numbers, message })
        });

        const result = await response.json();

        if (result.success) {
            showStatus(`✅ Messages sent! Success: ${result.sent}, Failed: ${result.failed}`, 'success');
        } else {
            showStatus('❌ Error: ' + result.error, 'error');
        }
    } catch (err) {
        showStatus('❌ Could not connect to server.', 'error');
    }
}

function showStatus(msg, type) {
    const statusDiv = document.getElementById('status');
    statusDiv.textContent = msg;
    statusDiv.className = type;
    statusDiv.style.display = 'block';
}