async function loadAlerts() {
  try {
    const response = await fetch('/alerts');
    if (!response.ok) {
      throw new Error('Unable to load alerts');
    }

    const data = await response.json();
    const alerts = data.alerts || [];

    document.getElementById('alert-count').textContent = data.total_alerts || 0;
    document.getElementById('overall-risk').textContent = Math.min(99, Math.max(40, data.total_alerts * 18 + 32));
    document.getElementById('risk-ips').textContent = alerts.filter((alert) => alert.type === 'SUSPICIOUS_IP').length;

    const totalFailed = alerts.reduce((sum, alert) => sum + (alert.failed_attempts || 0), 0);
    document.getElementById('failed-logins').textContent = totalFailed;

    const tableBody = document.getElementById('alerts-table');
    tableBody.innerHTML = alerts.map((alert) => {
      const severity = (alert.severity || 'MEDIUM').toLowerCase();
      const risk = alert.risk_level || 'MEDIUM';
      return `
        <tr>
          <td>${alert.type || 'ALERT'}</td>
          <td>${alert.ip || 'N/A'}</td>
          <td><span class="badge ${severity}">${severity}</span></td>
          <td><span class="badge ${risk.toLowerCase()}">${risk}</span></td>
        </tr>
      `;
    }).join('');
  } catch (error) {
    document.getElementById('alerts-table').innerHTML = `
      <tr>
        <td colspan="4">Unable to load alert data.</td>
      </tr>
    `;
  }
}

loadAlerts();
