let hamburgerMenuBtn = document.getElementById('hamburger-menu-btn');

let hamburgerMenuShowed = false;

hamburgerMenuBtn.addEventListener('click', (event) => {
  event.preventDefault();
  let menu = document.getElementById('hamburger-menu');
  if (hamburgerMenuShowed === true) {
    menu.classList.add('hidden');
  } else {
    menu.classList.remove('hidden');
  }
  hamburgerMenuShowed = !hamburgerMenuShowed;
});

let inputField = document.getElementById('search');

inputField.addEventListener('keypress', (event) => {
  if (event.key === 'Enter') {
    window.location.replace(`?q=${inputField.value}`)
  }
})
