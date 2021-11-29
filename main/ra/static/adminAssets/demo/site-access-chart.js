// Data define for bar chart
var myData = {
    labels: ["Springer Open", "Science Direct", "Scirp", "t&f online", "Herdin++", "Zlibrary", "Cambridge Core","Wiley Online Library - CELph","Wiley Online Library - ALBASA","Pro Quest Elibrary","Philippines Ebook Hub"],
    datasets: [{
        label: "Number of Students!",
        fill: false,
        backgroundColor: ['#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000'],
        borderColor: 'black',
        data: [85, 60,70, 50, 18, 20, 45, 30, 20, 40, 100],
    }]
};
// Code to drow Chart
// Default chart defined with type: 'bar'
var ctx = document.getElementById('my_Chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',    	// Define chart type
    data: myData    	// Chart data
});
// Function runs on chart type select update
function updateChartType() {
    // Destroy the previous chart
    myChart.destroy();
    // Draw a new chart on the basic of dropdown
    myChart = new Chart(ctx, {
        type: document.getElementById("chartType").value,  // Select chart type from dropdown
        data: myData
    });
};
