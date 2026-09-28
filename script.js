"use strict";

// Reemplazá este valor por el email comercial real antes de publicar.
const CONTACT_EMAIL = "juanlucky518@gmail.com";

document.documentElement.classList.add("js");
const menuButton = document.querySelector(".menu-toggle");
const menu = document.querySelector(".main-nav");
if (menuButton && menu) {
  const closeMenu = () => {
    menuButton.setAttribute("aria-expanded", "false");
    menuButton.setAttribute("aria-label", "Abrir menú");
    menu.classList.remove("is-open");
  };
  menuButton.addEventListener("click", () => {
    const expanded = menuButton.getAttribute("aria-expanded") !== "true";
    menuButton.setAttribute("aria-expanded", String(expanded));
    menuButton.setAttribute("aria-label", expanded ? "Cerrar menú" : "Abrir menú");
    menu.classList.toggle("is-open", expanded);
  });
  menu.querySelectorAll("a").forEach(link => link.addEventListener("click", closeMenu));
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
      closeMenu();
      menuButton.focus();
    }
  });
  document.addEventListener("click", event => {
    if (!event.target.closest(".site-header")) closeMenu();
  });
  const desktop = window.matchMedia("(min-width: 761px)");
  desktop.addEventListener("change", closeMenu);
}
document.querySelectorAll("[data-contact-email]").forEach(link => { link.textContent = CONTACT_EMAIL; link.href = `mailto:${CONTACT_EMAIL}`; });
const year = document.querySelector("#copyright-year"); if (year) year.textContent = new Date().getFullYear();
const form = document.querySelector("#contact-form");
if (form) form.addEventListener("submit", event => { event.preventDefault(); const data = new FormData(form); const subject = `Consulta desde Atlas — ${data.get("name")}`; const body = [`Nombre: ${data.get("name")}`, `Email: ${data.get("email")}`, `Empresa: ${data.get("company") || "No indicada"}`, "", data.get("message")].join("\n"); window.location.href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`; });
