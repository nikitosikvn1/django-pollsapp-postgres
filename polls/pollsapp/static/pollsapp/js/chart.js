document.addEventListener('DOMContentLoaded', () => {
    const field = document.querySelector('#result-chart').getContext('2d');
    const jsonText = JSON.parse(document.querySelector('#data').textContent);

    const labels = jsonText['labels'];
    const values = jsonText['values'];

    const chart = new Chart(field, {
        // 'pie', 'doughnut', 'bar', 'bubble', 'line', 'polarArea', 'radar', 'scatter'
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Voting result',
                data: values,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
