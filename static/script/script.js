$(document).ready(function () {
  // location dropdown list (Jquery)
  $("#id_location").select2({
    theme: "bootstrap-5",
  });

  /* ---- Bootstrap form validation ---- */
  // Loop over them and prevent submission
  const forms = document.querySelectorAll(".needs-validation");

  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });

  /* ---- Spinner and Modal ---- */
  let submitBtn = $("#submit-btn");
  let spinner = $("#spinner");
  let modal = new bootstrap.Modal("#staticBackdrop");

  spinner.hide();
  modal.hide();

  submitBtn.click(function () {
    spinner.show();
    setTimeout(function () {
      spinner.hide();
      modal.show();
    }, 1200);
  });
});
