// $(document).ready(function (message) {
//     $('.waves-effect').ripple(options);
//
// })

document.querySelectorAll('.waves-effect').forEach((cardRipple) => {
  new mdb.Ripple(cardRipple, { color: 'light' })
});