$(document).ready(function () {
  $("#id_location").select2({
    theme: "bootstrap-5",
  });

  const submitBtn = $("#submit-btn");
  const spinner = $("#spinner");
  const modal = new bootstrap.Modal("#staticBackdrop");
  const form = document.querySelector(".needs-validation");

  spinner.hide();

  submitBtn.click(function (event) {
    event.preventDefault();

    if (form.checkValidity()) {
      // Only proceed with AJAX if the form is valid
      spinner.show();

      $.ajax({
        type: "POST",
        url: form.action,
        data: $(form).serialize(),  // Serialize form data
        success: function (response) {
          spinner.hide();

          if (response.status === "success") {
            // Populate and show the modal with loan data
            $(".loan-success-items").empty();
            response.loan_data.forEach(function (item) {
              $(".loan-success-items").append(
                `<li>Request Number: ${item.request_number} - ${item.model_name}</li>`
              );
            });
            modal.show();
          } else {
            alert("Form submission failed. Please check for errors.");
          }
        },
        error: function () {
          spinner.hide();
          alert("An error occurred.");
        },
      });
    } else {
      // Show validation feedback if the form is not valid
      form.classList.add("was-validated");
    }
  });
});