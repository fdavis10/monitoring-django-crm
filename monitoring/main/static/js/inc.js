async function get_inc() {
    const response = await get('main/incedents-api/');
    const data = await response.json();
    const tableBody = document.getElementById('incidenttypetable');
    tableBody.innerHTML = '';
    data.incedents.forEach(incedent => {
        const row = `<tr>
            <td>${machine_status}</td>
            <td>${incedent_type}</td>
            <td>${new Date(incedent.timestamp).toLocaleDateString()}</td>
        </tr>`;
        tableBody.innerHTML += row;
    });
    
}

setInterval(get_inc, 5000);
document.addEventListener('DOMContentLoaded', get_inc);