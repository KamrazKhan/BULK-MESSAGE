async function sendMessages() {
    const numbersText = document.getElementById('numbers').value;
    const message = document.getElementById('message').value;

    // Split numbers by line
    const numbers = numbersText
        .split('\n')
        .map(n => n.trim())
        .filter(n => n.length > 0);

    if (numbers.length === 0 || message.trim() === '') {
        showStatus('❌ Please enter phone numbers and a message.', 'error');
        return;
    }

    // Disable button while sending
    const btn = document.getElementById('sendBtn');
    btn.disabled = true;
    btn.textContent = 'Sending...';

    showStatus(`⏳ Sending to ${numbers.length} numbers...`, 'info');

    try {
        const response = await fetch('/send', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ numbers, message })
        });

        // Check if response is OK
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const result = await response.json();

        if (result.success) {
            showStatus(
                `✅ Done! Success: ${result.sent}, Failed: ${result.failed}`,
                'success'
            );

            // Show detail results
            showDetails(result.details);

        } else {
            showStatus('❌ Error: ' + result.error, 'error');
        }

    } catch (err) {
        showStatus('❌ Could not connect to server. Is server.py running?', 'error');
        console.error(err);

    } finally {
        // Re-enable button always
        btn.disabled = false;
        btn.textContent = 'Send to All';
    }
}

// ── Show status message ──────────────────────────────
function showStatus(msg, type) {
    const statusDiv = document.getElementById('status');
    statusDiv.textContent = msg;
    statusDiv.className = type;
    statusDiv.style.display = 'block';
}

// ── Show per-number result details ───────────────────
function showDetails(details) {
    // Remove old result box if exists
    const old = document.getElementById('resultBox');
    if (old) old.remove();

    if (!details || details.length === 0) return;

    const box = document.createElement('div');
    box.id = 'resultBox';
    box.className = 'result-box';

    box.innerHTML = '<h3>📋 Delivery Report</h3>';

    details.forEach(d => {
        const item = document.createElement('div');
        item.className = `result-item ${d.status === 'sent' ? 'ok' : 'fail'}`;

        if (d.status === 'sent') {
            item.textContent = `✅ ${d.number} — Sent (SID: ${d.sid})`;
        } else {
            item.textContent = `❌ ${d.number} — Failed: ${d.error}`;
        }

        box.appendChild(item);
    });

    // Append after status div
    const statusDiv = document.getElementById('status');
    statusDiv.insertAdjacentElement('afterend', box);
}