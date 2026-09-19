import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.12.2/dist/mermaid.esm.min.mjs";

mermaid.initialize({
  startOnLoad: false,
  securityLevel: "strict",
  theme: "base",
  fontFamily: 'Inter, "Segoe UI", system-ui, sans-serif',
  themeVariables: {
    primaryColor: "#F2F6FB",
    primaryTextColor: "#16243A",
    primaryBorderColor: "#254DB8",
    lineColor: "#254DB8",
    secondaryColor: "#DDF3F6",
    tertiaryColor: "#FFF7E3",
  },
});

window.mermaid = mermaid;

async function renderMermaid(root = document) {
  const nodes = root.querySelectorAll("pre.mermaid:not([data-processed])");
  if (!nodes.length) return;
  await mermaid.run({ nodes });
}

function renderCurrentDocument(root) {
  renderMermaid(root).catch((error) => {
    console.error("Falha ao renderizar diagrama Mermaid", error);
  });
}

if (window.document$ && typeof window.document$.subscribe === "function") {
  document$.subscribe(({ body } = {}) => renderCurrentDocument(body || document));
} else {
  window.addEventListener(
    "DOMContentLoaded",
    () => renderCurrentDocument(document),
    { once: true },
  );
}
