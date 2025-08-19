document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".td-content pre.chroma, .td-content pre").forEach(block => {
    const btn = document.createElement("button");
    btn.className = "km-copy";
    btn.type = "button";
    btn.innerText = "Copy";
    btn.addEventListener("click", async () => {
      const code = block.querySelector("code")?.innerText || "";
      try {
        await navigator.clipboard.writeText(code);
        btn.innerText = "Copied!";
        setTimeout(() => (btn.innerText = "Copy"), 1200);
      } catch { btn.innerText = "Error"; }
    });
    block.style.position = "relative";
    block.appendChild(btn);
  });
});
