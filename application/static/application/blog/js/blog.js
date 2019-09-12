

	var cat_id = 0;
//recuperation 

  $(".delete-btn").click(function(event) {
  	// alert('The modal is about to be shown.');
  	var button = $(this)
  	cat_id = parseInt(button.data('artid')) 
  	console.log(cat_id)
	console.log($('#art_id').val(cat_id));

	if (cat_id != 0) {
		// $('#confirm-delete-btn').attr("href", "http://localhost:8000/blog/delete/"+ cat_id+"/");
		// $('#delete-form').attr("action", "{% url 'blog:delete_article' "+ cat_id + "%}");
		$('#delete-form').attr("action", "/blog/delete/"+ cat_id+"/");
	
	}

  });


	// $('a .confirm-delete-btn').attr("href", "https://www.w3schools.com/jquery/");
