document.addEventListener("DOMContentLoaded", () => {

  // Animación entrada tarjetas
  document.querySelectorAll(".card").forEach((card, i) => {
    card.style.opacity = 0;
    card.style.transform = "translateY(50px)";

    setTimeout(() => {
      card.style.transition = "all 0.8s ease";
      card.style.opacity = 1;
      card.style.transform = "translateY(0)";
    }, i * 300);
  });

});
