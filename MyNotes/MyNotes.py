import sqlite3
from PyQt5 import QtWidgets

conn = sqlite3.connect('MyNotesDatabase.db')

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget()
window.setWindowTitle('MyNotes')
window.resize(600,600)

layout = QtWidgets.QVBoxLayout()
hlayout = QtWidgets.QHBoxLayout()

def save_function():
    title = title_text.text()
    text = note_text.toPlainText()

    conn.execute(
        'INSERT INTO notes (title, text) VALUES (?, ?)', (title, text)
    )
    conn.commit()

    # cursor = conn.execute(
    #     'SELECT title FROM notes'
    # )
    #
    # if title not in cursor:
    #     conn.execute(
    #         'INSERT INTO notes (title, text) VALUES (?, ?)', (title, text)
    #     )
    #     conn.commit()
    # else:
    #     conn.execute(
    #         "UPDATE notes SET text=? WHERE title=?", (text, title)
    #     )

    title_text.setText('')
    note_text.setPlainText('')
    print('saved note')

def load_function():
    title = title_text.text()

    cursor = conn.execute(
        'SELECT text FROM notes WHERE title=?', (title,)
    )

    myNote = cursor.fetchone()
    # myNote = cursor.fetchall()

    if myNote:
        note_text.setPlainText(myNote[0])
        #counter += 1
    else:
        note_text.setPlainText('')
    print('loaded note')


def delete_function():
    title = title_text.text()

    conn.execute(
        'DELETE FROM notes WHERE title=?', (title,)
    )
    conn.commit()

    title_text.setText('')
    note_text.setPlainText('')
    print('deleted note')

#butoane
save_button = QtWidgets.QPushButton('Save Note')

hlayout.addWidget(save_button)
save_button.clicked.connect(save_function)

load_button = QtWidgets.QPushButton('Load Note')
hlayout.addWidget(load_button)
load_button.clicked.connect(load_function)

delete_button = QtWidgets.QPushButton('Delete Note')
hlayout.addWidget(delete_button)
delete_button.clicked.connect(delete_function)

layout.addLayout(hlayout)

#titlu
title_label = QtWidgets.QLabel('Note title:')
layout.addWidget(title_label)

title_text = QtWidgets.QLineEdit()
layout.addWidget(title_text)

#continut
note_label = QtWidgets.QLabel('MyNote:')
layout.addWidget(note_label)

note_text = QtWidgets.QPlainTextEdit()
layout.addWidget(note_text)

window.setLayout(layout)

if __name__ == "__main__":
    import sys
    window.show()
    sys.exit(app.exec())