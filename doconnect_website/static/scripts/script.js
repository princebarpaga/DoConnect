$(document).ready(function() {

	$(".button4").on('click', function() {
		var username = $('#id_username').val();
		var password = $('#id_password').val();

		$.ajax({
			url: 'validate_username',
			type: 'get',
			data: {
				'username' : username;
				'password' : password;

			}
			dataType: "json",
			success: function (data) {
          if (data.is_taken) {
            alert("A user with this username already exists.");
		}
	});
});
});
});