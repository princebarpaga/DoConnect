// $(document).ready(function() {

// 	$("#plogin").on('click', function() {
// 		var username = $('#id_username').val();
// 		var password = $('#id_password').val();

// 		$.ajax({
// 			// url: 'validate_username',
// 			url: 'views.py',
// 			type: 'get',
// 			data: {
// 				'username' : username,
// 				'password' : password

// 			},
// 			dataType: "json"
// 		})
// 	})
// });


function gologin() {
	var username = document.getElementById("id_username").value;
	var pass = document.getElementById("id_password").value;

	console.log(username);
	console.log(pass);

}