document.getElementsByClassName('email-form')[0].addEventListener('submit', function(e) {
  e.preventDefault();   
  var email = this.querySelector('input[type="email"]').value;
  var name = this.querySelector('input[type="text"]').value;
  var message = this.querySelector('textarea').value;
  var link = `mailto:coderz@gces.edu.in?subject=Message from ${name} - [${email}]&body=${message}`;
  window.location.href = link;
});