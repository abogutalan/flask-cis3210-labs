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

  // document.getElementById("get-button").addEventListener("click", get_method);
  // document.getElementById("put-button").addEventListener("click", put_method);
  // document.getElementById("delete-button").addEventListener("click", delete_method);
  document.getElementById("show-button").addEventListener("click", show_method);
  document.getElementById("exclude-button").addEventListener("click", exclude_method);

  function show_method() {
    // https://codeburst.io/multiple-ways-of-implementing-flickr-public-api-in-jquery-and-javascript-dbaf0f35bbef
    console.log("get bttn clicked!");
    var flickerAPI = "https://api.flickr.com/services/feeds/photos_public.gne?format=json&tags=" + $("#search").val();
    $.ajax({
      url: flickerAPI,
      dataType: "jsonp", // jsonp
      jsonpCallback: 'jsonFlickrFeed', // add this property
      success: function (result, status, xhr) {
        document.getElementById("outputDiv").innerHTML = "";
        let quantity = $('#quantity').val();
        let outputDiv = document.getElementById('outputDiv');
        
        $.each(result.items, function (i, item) {
          console.log('item')
          console.log(item)
          // $("<img>").attr("src", item.media.m).appendTo("#outputDiv");
          let a = document.createElement('a');
          let img = document.createElement('img');
          img.src = item.media.m;
          img.title = "Author: " + item.author + 
            "\nAuthor id: " + item.author_id + 
            "\nPublished: " + item.published + 
            "\nTaken Date: " + item.date_taken +
            "\nLink: " + item.link;

          a.appendChild(img);                    
          a.href = item.media.m;
          a.download = item.media.m;

          img.height = 100;
          img.width = 100;

          outputDiv.appendChild(a);

          if (i == quantity-1) {
            return false;
          }
        });
        $('#outputDiv').each(function() {
          if (!$(this).find('img').length) {
              // there is an image in this div, do something...
              console.log("img does not exist!")
              document.getElementById("outputDiv").innerHTML = "img does not exist!";
          }
      });
      },
      error: function (xhr, status, error) {
        console.log(xhr)
        $("#outputDiv").html("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
      }
    });
    // $.ajax({
    //   url: "/images", 
    //   data: 'https://live.staticflickr.com/689/22847153945_b769a2b78f_o.jpg', 
    //   type: 'get', success: function (result) {
    //     $("#result-text").html(result);
    //   }
    // });
  }

  $('#outputDiv').on('click', 'img', function (e) {
    e.stopPropagation();
    $(this).remove();
});

function exclude_method() {
  // https://codeburst.io/multiple-ways-of-implementing-flickr-public-api-in-jquery-and-javascript-dbaf0f35bbef
  console.log("get bttn clicked!");
  var flickerAPI = "https://api.flickr.com/services/feeds/photos_public.gne?format=json&tags!=" + $("#search").val();
  $.ajax({
    url: flickerAPI,
    dataType: "jsonp", // jsonp
    jsonpCallback: 'jsonFlickrFeed', // add this property
    success: function (result, status, xhr) {
      document.getElementById("outputDiv").innerHTML = "";
      let quantity = $('#quantity').val();
      let outputDiv = document.getElementById('outputDiv');
      
      $.each(result.items, function (i, item) {
        console.log('item')
        console.log(item)
        // $("<img>").attr("src", item.media.m).appendTo("#outputDiv");
        let a = document.createElement('a');
        let img = document.createElement('img');
        img.src = item.media.m;
        
        a.appendChild(img);                    
        a.href = item.media.m;
        a.download = item.media.m;

        img.height = 100;
        img.width = 100;
        outputDiv.appendChild(a);

        if (i == quantity-1) {
          return false;
        }
      });
      $('#outputDiv').each(function() {
        if (!$(this).find('img').length) {
            // there is an image in this div, do something...
            console.log("img does not exist!")
            document.getElementById("outputDiv").innerHTML = "img does not exist!";
        }
    });
    },
    error: function (xhr, status, error) {
      console.log(xhr)
      $("#outputDiv").html("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
    }
  });
  // $.ajax({
  //   url: "/images", 
  //   data: 'https://live.staticflickr.com/689/22847153945_b769a2b78f_o.jpg', 
  //   type: 'get', success: function (result) {
  //     $("#result-text").html(result);
  //   }
  // });
}

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

