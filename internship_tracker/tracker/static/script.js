
    function validateForm() {
      const name = document.forms["internshipForm"]["student_name"].value;
      if (name == "") {
        alert("Name must be filled out");
        return false;
      }
    }