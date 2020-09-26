$(document).ready(function () {

  console.log('name: Abdullah Ogutalan');
  console.log('student number: 1109732');


  document.getElementById("get-button").addEventListener("click", get_method);
  document.getElementById("put-button").addEventListener("click", put_method);
  document.getElementById("post-button").addEventListener("click", post_method);
  document.getElementById("delete-button").addEventListener("click", delete_method);


  function get_method() {

    console.log("get bttn clicked!");
    $.ajax({
      url: "/user", type: 'get', success: function (result) {
        $("#result-text").html(result);
      }
    });
  }

  function put_method() {

    console.log("put bttn clicked!");
    $.ajax({
      url: "/user", 
      type: 'put', 
      data: $('form').serialize(),
      success: function (result) {
        console.log('Updated user credentials!')
        $("#result-text").html(result);
      }
    });
  }

  function post_method() {

    console.log("post bttn clicked!");
    $.ajax({
      url: "/user", 
      type: 'post', 
      success: function (result) {
        $("#result-text").html(result);
      }
    });
  }

  function delete_method() {

    console.log("delete bttn clicked!");
    $.ajax({
      url: "/user", type: 'delete', success: function (result) {
        console.log('Deleted user credetials!')
        $("#result-text").html(result);
      }
    });
  }

  $('#signup-form').submit(function (e) {
    e.preventDefault();
    var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
    $.ajax({
      url: '/signUpUser',
			data: $('form').serialize(),
      type: 'POST',
      success: function (response) {
        console.log(response);
        $("#result-text").html(response);
      },
      error: function (error) {
        console.log(error);
      }
    });
  });



});

