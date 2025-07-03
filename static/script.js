async function loadNotes() {
    const res = await fetch('/api/notes');
    const notes = await res.json();
    const list = document.getElementById('noteList');
    list.innerHTML = '';
    notes.forEach(note => {
        const li = document.createElement('li');
        li.textContent = note.text + ' ';
        const delBtn = document.createElement('button');
        delBtn.textContent = '삭제';
        delBtn.onclick = async () => {
            await fetch(`/api/notes/${note.id}`, { method: 'DELETE' });
            loadNotes();
        };
        li.appendChild(delBtn);
        list.appendChild(li);
    });
}

async function addNote() {
    const input = document.getElementById('noteInput');
    const text = input.value.trim();
    if (!text) return alert('메모를 입력하세요!');
    await fetch('/api/notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
    });
    input.value = '';
    loadNotes();
}

window.onload = loadNotes;
