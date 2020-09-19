$(document).ready(function () {

  console.log('cis3210');

  // Load Links
  clippy.load('Links', getArtsy);

  //Replace with a Links animation
  $('#alert-button').click(function () {
    alert("Alert!");
  });

  
  function getArtsy (agent) {
    // Do anything with the loaded agent
    $('#artsy-button').click(function () {
  
      agent.play('GetArtsy');
      agent.moveTo(300, 300);
      agent.show();
    });
  }

});

