<template>
  <div class="bg-info bg-gradient bg-opacity-10">
    <header class="bg-danger bg-gradient bg-opacity-10">
      <nav class="navbar navbar-expand-lg navbar-light bg-primary bg-gradient bg-opacity-10">
        <div class="container-fluid bg-danger bg-gradient bg-opacity-10">
          <!--<i class="fa fa-bell"></i>-->
          <i class="fa fa-user-graduate"></i>
          <i class="fa fa-school"></i>
          <i class="fa fa-chalkboard"></i>
          <!--<i class="fa fa-atom"></i>-->
          <i><strong>Play2Learn</strong></i>
          <!--<i class="fa fa-music"></i>-->
          <!--<i class="fa fa-graduation-cap"></i>-->
          <i class="fa fa-laptop-code"></i>
          <i class="fa fa-book-open"></i>      
          <i class="fa fa-graduation-cap"></i>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
              <li class="nav-item"><router-link to="/" class="nav-link mx-3 fw-bold">Home</router-link></li>
              <li class="nav-item"><router-link to="/login" class="nav-link mx-3 fw-bold">Login</router-link></li>
              <li class="nav-item"><router-link to="/about" class="nav-link mx-3 fw-bold">About</router-link></li>
              <li class="nav-item dropdown">
                <a class="nav-link mx-3 dropdown-toggle fw-bold" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Games
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li class="nav-item"><router-link to="/games/math-facts" class="nav-link mx-1 fw-bold">Math Facts</router-link></li>
                  <li class="nav-item"><router-link to="/games/anagram-hunt" class="nav-link mx-1 fw-bold">Anagram Hunt</router-link></li>
                </ul>
              </li>
              <li class="nav-item"><router-link to="/contact" class="nav-link mx-3 fw-bold">Contact</router-link></li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script>
  export default {
    name: 'Header'
  }
</script>
