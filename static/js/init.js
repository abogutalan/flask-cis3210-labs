$(document).ready(function () {

  console.log('name: Abdullah Ogutalan');
  console.log('student number: 1109732');

  //how to protect your application against query injection and sanitize user input.
  // console.log('How to protect your application against query injection and sanitize user input:')
  // console.log("Using the Python DB API, don't do this:\n\
  // # Do NOT do it this way.\n\
  // cmd = '\"update people set name=\'%s\' where id=\'%s\'\" % (name, id)\n\
  // curs.execute(cmd)\n\
  // This builds a SQL string using Python's string formatting, but it creates an unsafe string that is then passed through to the database and executed.\n\
  // Instead, do this:\n\
  // cmd = \"update people set name=%s where id=%s\"\n\
  // curs.execute(cmd, (name, id))\n\
  // This sets up placeholders so that the database can fill in the data values properly and safely.\n\
  // For cases involving a single variable do this:\n\
  // cmd = \"SELECT * FROM PEOPLE WHERE name = %s\"\n\
  // curs.execute(cmd, (name,))\n\
  // Note that the placeholder syntax depends on the database you are using.")
  // console.log('citation: https://bobby-tables.com/python.html')

  document.getElementById("get-button").addEventListener("click", get_method);
  document.getElementById("put-button").addEventListener("click", put_method);
  document.getElementById("delete-button").addEventListener("click", delete_method);


  function get_method() {

    console.log("get bttn clicked!");
    $.ajax({
      url: "/user", 
      data: $('form').serialize(), 
      type: 'get', success: function (result) {
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

  function delete_method() {

    console.log("delete bttn clicked!");
    $.ajax({
      url: "/user", data: $('form').serialize(), type: 'delete', success: function (result) {
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
      url: '/user',
			data: $('form').serialize(),
      type: 'POST',
      success: function (response) {
        console.log(response);
        location.reload();
        $("#result-text").html(response);
        
      },
      error: function (error) {
        console.log(error);
      }
    });
  });



});

