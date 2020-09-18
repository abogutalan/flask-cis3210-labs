$(document).ready(function () {

  console.log('cis3210');
  // Load Links

  //Replace with a Links animation
  $('#alert-button').click(function () {
    alert("Alert!");
  });

  $('#artsy-button').click(function () {
    clippy.load('Links', function (agent) {
    //   // Do anything with the loaded agent
      agent.play('GetArtsy');
      agent.moveTo(300, 300);
      agent.show();
    });
  });

});