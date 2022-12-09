<template>
<main class="col-sm col-md border rounded-3 border-dark bg-primary bg-gradient bg-opacity-10 m-5 pb-5">
  <h1 class="text-center m-3">Registration and Login</h1>
    <div class="row mt-3">
      <div class="col">
        <button class="btn btn-primary" data-bs-toggle="collapse" href="#collapseRegistration" aria-expanded="false" aria-controls="collapseRegistration">Need an account? Register here.</button>
      </div>
      <div class="col">
        <button class="btn btn-primary" data-bs-toggle="collapse" href="#collapseLogin" aria-expanded="false" aria-controls="collapseLogin">Have an account? Log in here.</button>
      </div>
    </div>
  <div class="row">
    <div class="col mx-5">
      <div class="collapse multi-collapse" id="collapseRegistration">
        <form id="registration-form" method="post" action="javascript:alert('Form Submitted')" class="form-control mt-2" novalidate>
          <h2>Register</h2>
          <div class="mb-3">
            <label for="register-username" class="form-label">Username:</label>
            <input class="form-control" type="text" id="register-username" name="register-username" 
              required minlength="8" maxlength="25">
          </div>
          <div class="mb-3">
            <label for="register-email" class="form-label">Email:</label>
            <input class="form-control" type="email" id="register-email" name="register-email" required>
          </div>
          <div class="mb-3">
            <label for="pw" class="form-label">Password:</label>
            <input class="form-control" type="password" name="pw" id="pw" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number, one uppercase and lowercase letter, and at least 8 or more characters." required>
          </div>
          <div class="mb-3">
            <label for="pw2" class="form-label">Repeat Password:</label>
            <input class="form-control" type="password" name="pw2" id="pw2" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Please enter a matching password." required>
          </div>
          <div class="mb-3">
            <button class="btn btn-warning" name="submit" id="registration-button">Register</button>
          </div>
          <div class="mb-3" id="registerterms">
              <input type="checkbox" name="terms" id="terms" required>
              <label for="terms">I am over 13 and like playing computer games.</label>
          </div>
        </form>
      </div>
    </div>
    <div class="col">
      <div class="collapse multi-collapse" id="collapseLogin">
        <form id="login-form" action="javascript:alert('Form Submitted')" method="post" class="form-control mt-2" novalidate>
          <h2>Login</h2>
            <div class="mb-3">
              <label for="login-username" class="form-label">Username:</label>
              <input class="form-control" type="text" id="login-username" name="login-username" 
                required minlength="8" maxlength="25">
            </div>
            <div class="mb-3">
              <label for="login-password" class="form-label">Password:</label>
              <input class="form-control" type="password" name="login-password" id="login-password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters." required>
            </div>
            <button class="btn btn-success" name="submit" id="login-button">Log In</button>
        </form>
      </div>
    </div>
  </div>
</main>
</template>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script>
  export default {
    name: 'Login'
  }
</script>