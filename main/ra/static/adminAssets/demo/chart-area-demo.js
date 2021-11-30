// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

document.getElementById("myAreaChart")
// Area Chart Example
var ctx = document.getElementById("myAreaChart");


const dates = ['2021-03-01', '2021-03-02', '2021-03-03', '2021-03-04', '2021-03-05', '2021-03-06', '2021-03-07'];
const datapoints= [10000, 30162, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451];
  

const data = {
    type: 'line',
    labels: dates,
    datasets: [{
      label: "Active Users",
      lineTension: 0.3,
      backgroundColor: "rgba(191, 63, 63)",
      borderColor: "rgba(243, 246, 85)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(191, 63, 63)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(243, 246, 85)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: datapoints,
    }],
 
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 40000,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
};


const config = {
      type: 'line',
      data,
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    };

const myAreaChart = new Chart(
  document.getElementById('myAreaChart'),
  config
);
