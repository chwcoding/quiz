document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('cheer-btn');
    const countEl = document.getElementById('cheer-count');
    let cls = document.body.getAttribute('data-class');

    function update() {
        fetch(`/api/cheer-count?cls=${cls}`)
            .then(r => r.json())
            .then(data => {
                countEl.textContent = data.count;
            });
    }

    btn.addEventListener('click', () => {
        fetch('/api/cheer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cls })
        }).then(update);
    });

    update();
});
