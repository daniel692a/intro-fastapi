from typing import List
from fastapi import FastAPI, status
from typing import List
from note import Note

app = FastAPI(version='0.0.1', title='Notas', description='API para acesso al sistema de notas')

notes : List[Note] = []

@app.get('/', response_model=List[Note])
def get_notes():
    return notes

@app.post('/create/', response_model=Note)
def create_note(note: Note):
    new_note = {
        'id': len(notes),
        'title': note.title,
        'content': note.content
    }
    notes.append(new_note)
    return new_note

@app.get('/note/{id}', response_model=Note)
def show_note(id: int):
    for note in notes:
        if note['id'] == id:
            return note
    return {'error': 'Note not found'}

@app.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id: int):
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            return {'message': 'Note deleted'}
    return {'error': 'Note not found'}

@app.put('/update/{id}', response_model=Note)
def update_note(id: int, note_udt: Note):
    update_nt = notes[id]
    update_nt['title'] = note_udt.title
    update_nt['content'] = note_udt.content
    return update_nt