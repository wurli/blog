document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre > code').forEach(code => {
    const pre = code.parentElement;
    pre.style.position = 'relative';

    const button = document.createElement('button');
    button.className = 'code-copy-button';
    button.type = 'button';
    button.innerHTML = '<span class="copy-icon"></span>';

    button.addEventListener('click', () => {
      navigator.clipboard.writeText(code.textContent).then(() => {
        button.classList.add('copied');
        setTimeout(() => {
          button.classList.add('fade-out');
          setTimeout(() => {
            button.classList.remove('copied', 'fade-out');
          }, 200);
        }, 2000);
      });
    });

    pre.appendChild(button);
  });
});
