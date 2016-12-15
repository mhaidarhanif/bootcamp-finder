import os
import shutil

import yaml

BOOTCAMPS_FOLDER_LOCAL = 'bootcamps'


def convert_bootcamp_data(slug):
    """Convert a bootcamp's folder from the old format to the new."""
    # Rename existing folder as `slug`-legacy
    shutil.move(
        '{}/{}/'.format(BOOTCAMPS_FOLDER_LOCAL, slug),
        '{}/{}-legacy'.format(BOOTCAMPS_FOLDER_LOCAL, slug))

    # Create new empty `slug` folder
    os.mkdir('{}/{}'.format(BOOTCAMPS_FOLDER_LOCAL, slug))

    # Copy logo over to new folder
    shutil.copy(
        '{}/{}-legacy/logo.png'.format(BOOTCAMPS_FOLDER_LOCAL, slug),
        '{}/{}/logo.png'.format(BOOTCAMPS_FOLDER_LOCAL, slug))

    # Compile bootcamp's and its programs' data.yml and description.md files
    # into one and write back to single data.yml file in new folder
    with open(
            '{}/{}-legacy/data.yml'.format(
                BOOTCAMPS_FOLDER_LOCAL, slug), 'r') as f:
        data = yaml.load(f.read())

    with open(
            '{}/{}-legacy/description.md'.format(
                BOOTCAMPS_FOLDER_LOCAL, slug), 'r') as f:
        description = f.read()

    data.update({'description': description})
    data.update({'programs': {}})

    with open('{}/{}/data.yml'.format(BOOTCAMPS_FOLDER_LOCAL, slug), 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


def main():
    # all_bootcamps = os.listdir('./bootcamps/')
    convert_bootcamp_data('bloc')


if __name__ == '__main__':
    main()
