document.addEventListener("DOMContentLoaded", () => {
  const blocks = document.querySelectorAll(
    ".td-content pre.chroma, .td-content .highlight > pre"
  );
  blocks.forEach((pre) => {
    const code = pre.querySelector("code") || pre;
    const classes = (code.getAttribute("class") || pre.getAttribute("class") || "");
    const lang = (classes.match(/language-([\w+-]+)/)?.[1] ||
                 classes.match(/(\w+)$/)?.[1] || "text").toUpperCase();

    const wrap = document.createElement("div");
    wrap.className = "km-code";
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);

    const hdr = document.createElement("div");
    hdr.className = "km-code__hdr";
    hdr.innerHTML = `<span class="km-code__lang">${lang}</span>
                     <button class="km-code__copy" type="button">Copy</button>`;
    wrap.insertBefore(hdr, pre);

    hdr.querySelector(".km-code__copy").addEventListener("click", async (e) => {
      try {
        await navigator.clipboard.writeText(code.innerText);
        e.target.textContent = "Copied!";
        setTimeout(() => (e.target.textContent = "Copy"), 1200);
      } catch {
        e.target.textContent = "Error";
      }
    });
  });
});
