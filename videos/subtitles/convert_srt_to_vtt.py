import os


def main():
    num = 0

    for fname in os.listdir('.'):
        if os.path.isfile(fname) and fname.endswith('.srt'):
            new_fname = fname[:-3] + 'vtt'
            if not os.path.exists(new_fname):
                with open(fname) as f:
                    content = f.read()
                new_content = 'WEBVTT\n\n' + content.replace(',', '.')
                os.renames(fname, new_fname)
                with open(new_fname, 'w') as f:
                    f.write(new_content)
                print(f'File converted: {fname}')
                num += 1

    if num == 0:
        print('There is no SRT file to convert.')


if __name__ == '__main__':
    main()
