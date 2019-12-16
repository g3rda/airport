
function myFunction(){
	var name = document.getElementById("name").value;
	var email = document.getElementById("email").value;
	var message = document.getElementById("message").value;
	var subj=name+';'+email
	Email.send({
    Host : "smtp.gmail.com",
    Username : "fri3d.gr33n.t0m4t0es@gmail.com",
    Password : "Fried Green Tomatoes",
    To : 'fri3d.gr33n.t0m4t0es@gmail.com',
    From : "fri3d.gr33n.t0m4t0es@gmail.com",
    Subject : subj,
    Body : message
}).then(
  message => alert(message)
);

}
