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
    if (form.checkValidity()) {
      event.preventDefault();

      spinner.show();
      setTimeout(function () {
        spinner.hide();
        modal.show();
      }, 1200);
    } else {
      event.preventDefault();
      form.classList.add("was-validated");
    }
  });
});
