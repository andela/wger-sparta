var chart = c3.generate({
  bindto: '#chart',
  data: {
    columns: [
      ['Me', 30, 200, 100, 400, 150, 250],
      ['Admin', 50, 20, 10, 40, 15, 25]
    ]
  },
  axis: {
    y: {
      label: {
        text: 'Weight',
        position: 'outer-middle'
      }
    },
    x: {
      label: {
        text: 'Period',
        position: 'middle'
      }
    }
  }
});

chart.load({
  columns: [
    ['Me', 300, 100, 250, 150, 300, 150, 500],
    ['Admin', 100, 200, 150, 50, 100, 250]
  ]
});
