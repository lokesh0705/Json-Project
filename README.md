# Json-Project

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>form</title>
</head>
<body>
  <html>
    <head>
        <title>Contact Form </title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <link href='https://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>
        <link href='custom.css' rel='stylesheet' type='text/css'>
    </head>
    <body>

        <div class="container">

            <div class="row">

                <div class="col-xl-8 offset-xl-2 py-5">

                  <h1>Contact Form <a href="">Stay in Touch</a></h1>

                    <p class="lead">Your suggestions are precious to us.</p>

                    <!-- We're going to place the form here in the next step -->
                    <form></form> 

                </div>

            </div>

        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>        
        <script src="https://cdnjs.cloudflare.com/ajax/libs/1000hz-bootstrap-validator/0.11.9/validator.min.js" integrity="sha256-dHf/YjH1A4tewEsKUSmNnV05DDbfGN3g7NMq86xgGh8=" crossorigin="anonymous"></script>
        <script src="contact.js"></script>

        <form id="contact-form" method="post" action="/form" role="form">
          {%csrf_token%}
          <div class="messages"></div>
      
          <div class="controls">
      
              <div class="row">

                  <div class="col-md-6">
                      <div class="form-group">
                          <label for="form_name">Firstname *</label>
                          <form action="/form" method="post">
                          <input id="form_name" type="text" name="name" class="form-control" placeholder="Please enter your firstname *" required="required" data-error="Firstname is required.">
                         
                      </div>
                  </div>
                  <div class="col-md-6">
                      <div class="form-group">
                          <label for="form_lastname">Lastname *</label>
                          <input id="form_lastname" type="text" name="surname" class="form-control" placeholder="Please enter your lastname *" required="required" data-error="Lastname is required.">
                         
                      </div>
                  </div>
              </div>
              <div class="row">
                  <div class="col-md-6">
                      <div class="form-group">
                          <label for="form_email">Email *</label>
                          <input id="form_email" type="email"   name="email" class="form-control" placeholder="Please enter your email *" required="required" data-error="Valid email is required.">
                          
                      </div>
                  </div>
                  <div class="col-md-6">
                      <div class="form-group">
                          <label for="form_need">mobile *</label>
                       
                            <input id="phone" type="phone" name="mobile" class="form-control" placeholder="Please enter your contact number* "required="required" data-error="Valid email is required.">
                            
                          
                         
                      </div>
                  </div>
              </div>
              <div class="row">
                  <div class="col-md-12">
                      <div class="form-group">
                          <label for="form_message">Message *</label>
                          <textarea id="form_message"  class="form-control" name="desc" placeholder="Message for me *" rows="4" required="required" data-error="Please, leave us a message."></textarea>
                          
                      </div>
                  </div>
                  <div class="col-md-12">
                      <input type="submit" class="btn btn-success btn-send" value="Send message">
                  </div>
              </div>
              <div class="row">
                  <div class="col-md-12">
                      <p class="text-muted">
                          <strong>*</strong> These fields are required. 
                          <a href=" " target="_blank">Thank YOU!</a>.</p>
                  </div>
              </div>
          </div>
      
      </form>
    </body>
</html>

    
<script> 
  function validateAndGetFormData() {
var empIdVar = $("#empId").val();
if (empIdVar === "") {
alert("Employee ID Required Value");
$("#empId").focus();
return "";
}
var empNameVar = $("#empName").val();
if (empNameVar === "") {
alert("Employee Name is Required Value");
$("#empName").focus();
return "";
}
var empEmailVar = $("#empEmail").val();
if (empEmailVar === "") {
alert("Employee Email is Required Value");
$("#empEmail").focus();
return "";
}
var jsonStrObj = {
empId: empIdVar,
empName: empNameVar,
empEmail: empEmailVar,
};
return JSON.stringify(jsonStrObj);
}  
    
 
    
function SaveEmployee{}{
var putReqStr = createPUTRequest("90935586|-31948841969445468|90933720",
jsonStr, "SAMPLE", "EMP-REL");
alert(putReqStr);
jQuery.ajaxSetup({async: false});
var resultObj = executeCommand(putReqStr,
"http://api.login2explore.com:5577", "/api/iml");
alert(JSON.stringify(resultObj));
jQuery.ajaxSetup({async: true});
resetForm();
}
</script>

</body>    
</html>

