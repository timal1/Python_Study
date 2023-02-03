import view


def write_to_files(data):
    with open("guide1.txt", 'a', encoding='utf-8') as file1:
        file1.write(f'{view.line_entry(data)}\n')
    with open("guide2.txt", 'a', encoding='utf-8') as file2:
        file2.write(f'{view.column_entry(data)}\n-----------------------\n')
