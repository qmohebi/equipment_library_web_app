$(document).ready(function () {
  $("#id_location").select2({
    theme: "bootstrap-5",
  });

  // Footer date
  const currentYear = new Date().getFullYear();
  $("#current-year").text(currentYear);

  const submitBtn = $("#submit-btn");
  const spinner = $("#spinner");
  const feedbackMessage = $('.equ-invalid-feedback');
  const modal = new bootstrap.Modal("#staticBackdrop");
  let form = document.querySelector(".needs-validation");

  feedbackMessage.hide();
  spinner.hide();

  submitBtn.click(function (event) {
    event.preventDefault(); // Prevent the default form submission

    if (form.checkValidity()) {
      feedbackMessage.hide();
      spinner.show();

      // Send AJAX request
      $.ajax({
        type: "POST",
        url: form.action,
        data: $(form).serialize(), // Serialize form data
        success: function (response) {
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
            }, 1000);
          } else {
            // Handle any errors (if needed)
            // alert("Something went wrong, please try again.");
            spinner.hide();
          }
        },
        error: function (error) {
          alert("An error occurred.");
        },
      });
    } else {
      event.preventDefault();
      form.classList.add("was-validated");
      feedbackMessage.show();
    }
  });

  // reload main page when user closes modal
  const closeModalBtn = $("#close_modal_btn");
  closeModalBtn.on("click", function() {
    window.location.reload();
  });
});
