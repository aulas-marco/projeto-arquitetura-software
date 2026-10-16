function abrirDetalhesDoAlvo() {
  var alvo = location.hash ? document.getElementById(decodeURIComponent(location.hash.slice(1))) : null;
  for (var el = alvo; el; el = el.parentElement) {
    if (el.tagName === "DETAILS") el.open = true;
  }
  if (alvo) alvo.scrollIntoView();
}
window.addEventListener("hashchange", abrirDetalhesDoAlvo);
document.addEventListener("DOMContentLoaded", abrirDetalhesDoAlvo);
