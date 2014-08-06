
import argparse
import os


DIRECTORY_PATH = "/.python_notes"
CONFIG_FILE = os.path.join(DIRECTORY_PATH, ".python_notes_config")


def main():
    args = parse_args()

    check_setup()

    if args.open is not None:
        open_note(args.open)
    elif args.new is not None:
        create_note(args.new)
    elif args.delete is not None:
        delete_note(args.delete)
    elif args.true_delete is not None:
        true_delete_note(args.true_delete)
    else:
        list_notes()


def parse_args():
    parser = argparse.ArgumentParser(description='Create, edit and manage notes.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-o', '--open', help="Opens the note.", type=int)
    group.add_argument('-n', '--new', help="Name of the note to be created.")
    group.add_argument('-d', '--delete', help="Deletes the note, but not the file.", type=int)
    group.add_argument('-dd', '--true_delete', help="Deletes the note and the file.", type=int)
    return parser.parse_args()


def check_setup():
    if not os.path.exists(DIRECTORY_PATH):
        os.makedirs(DIRECTORY_PATH)


def get_note_filepath(note_name):
    return os.path.join(DIRECTORY_PATH, note_name + ".txt")


def list_notes():
    notes_file = open(CONFIG_FILE, 'r')
    i = 0
    for note in notes_file:
        if note:
            note = note.replace('\n', '')
            print "#{0}:\t{1}".format(i, note)
            i += 1
    notes_file.close()


def create_note(note_name):
    note_filepath = get_note_filepath(note_name)
    if not os.path.exists(note_filepath):
        with open(CONFIG_FILE, "a+") as config_file:
            config_file.write(note_name + "\n")

        note_file = open(note_filepath, "w")
        note_file.close()

        os.system(os.path.abspath(note_filepath))


def open_note(id):
    with open(CONFIG_FILE, 'r') as notes_file:
        i = 0
        for note in notes_file:
            if i == id:
                note = note.replace('\n', '')
                note_filepath = get_note_filepath(note)
                if os.path.exists(note_filepath):
                    os.system(os.path.abspath(note_filepath))
            i += 1




def delete_note(id):
    notes_copy = None
    with open(CONFIG_FILE, 'r') as notes_file:
        notes_copy = notes_file.read()

    with open(CONFIG_FILE, 'w') as notes_file:
        i = 0
        for note in notes_copy:
            if i != id:
                note_file.write(note)
            i += 1


def true_delete_note(id):
    notes_copy = None
    with open(CONFIG_FILE, 'r') as notes_file:
        notes_copy = notes_file.read()

    note_name = None
    with open(CONFIG_FILE, 'w') as notes_file:
        i = 0
        for note in notes_copy:
            if i != id:
                note_file.write(note)
            else:
                note_name = note.replace('\n', '')
            i += 1

    if note_name:
        note_filepath = get_note_filepath(note_name)
        if os.path.exists(note_filepath):
            os.remove(note_filepath)



if __name__ == '__main__':
    main()
