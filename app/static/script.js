// Botones flotantes
document.querySelectorAll(".btn").forEach(btn => {
    btn.addEventListener("mouseover", () => {
        btn.style.boxShadow = "0 0 40px white";
    });

    btn.addEventListener("mouseout", () => {
        btn.style.boxShadow = "";
    });
});

// Animación suave cards
document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("mousemove", e => {
        card.style.transform = "scale(1.05)";
    });

    card.addEventListener("mouseleave", e => {
        card.style.transform = "scale(1)";
    });
});
