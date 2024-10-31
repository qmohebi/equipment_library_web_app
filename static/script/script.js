$(document).ready(function () {
  // location dropdown list (Jquery)
  $("#id_location").select2({
    theme: "bootstrap-5",
  });

  const currentYear = new Date().getFullYear();
  $("#current-year").text(currentYear);

  const submitBtn = $("#submit-btn");
  const spinner = $("#spinner");
  const modal = new bootstrap.Modal("#staticBackdrop");
  let form = document.querySelector(".needs-validation");

  spinner.hide();

  submitBtn.click(function (event) {
    event.preventDefault(); // Prevent the default form submission

    if (form.checkValidity()) {
      spinner.show();

      // Send AJAX request
      $.ajax({
        type: "POST",
        url: form.action,
        data: $(form).serialize(), // Serialize form data
        success: function (response) {
          // Hide the spinner
          spinner.hide();

          if (response.status === "success") {
            // Clear the loan items in the modal
            $(".loan-success-items").empty();

            // Loop through the loan_data from the response and add items to the modal
            response.loan_data.forEach(function (item) {
              $(".loan-success-items").append(
                `<li>Request Number: ${item.request_number} - ${item.model_name}</li>`
              );
            });

            // fixed modal delay and spinner
            spinner.show();
            setTimeout(function () {
              spinner.hide();
              modal.show();
            }, 1200);
          } else {
            // Handle any errors (if needed)
            alert("Something went wrong, please try again.");
          }
        },
        error: function (error) {
          spinner.hide();
          alert("An error occurred.");
        },
      });
    } else {
      event.preventDefault();
      form.classList.add("was-validated");
    }
  });
});
