var value=[53000, 23000, 7000, 6000, 4000, 7000]


var data = [{
  values: value,
  labels: ['Cash', 'Wheat', 'Soybeans', 'Corn', 'Cotton', 'Sugar'],
  type: 'pie'
}];

var layout = {
  title: '',
  font: {
    family: 'Impact monospace',
    size: 18,
    color: 'black'},

  height: 700,
  width: 900

};

Plotly.newPlot('pie-chart', data, layout);
