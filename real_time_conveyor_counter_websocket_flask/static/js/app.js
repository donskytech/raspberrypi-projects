$(document).ready(function () {
  //connect to the socket server.
  var socket = io.connect("http://" + document.domain + ":" + location.port);
  // var socket = io.connect();

  //receive details from server
  socket.on("updateSensorData", function (msg) {
    console.log("Received sensorData :: " + msg.date + " :: " + msg.value);
    $("#current-count").text(msg.value);

  });
});
