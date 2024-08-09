import os
import sys
import argparse
import pandas as pd

pd.set_option('display.max_rows', 500)

KIBIBYTE = 1024
KILOBYTE = 1000


def get_content_size(start_path='.'):
    # Source: https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if os.path.islink(fp):
                continue
            # is file or hidden file
            total_size += os.path.getsize(fp)

    return total_size


if __name__ == "__main__":

    # Parse user-input arguments
    description = "This program displays the size of top-level files in the specified directory."
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('root_path',
                        type=str,
                        metavar='DIR_PATH',
                        help="Full path to the target directory")
    parser.add_argument('-u',
                        dest='unit',
                        type=str,
                        choices=('gib', 'mib', 'kib', 'gb', 'mb', 'kb'),
                        metavar='UNIT',
                        help="preferred unit for displaying file size")
    args = parser.parse_args()

    # Check path validity
    if not os.path.exists(args.root_path):
        print("Invalid path provided!")
        print(f"Could not find \"{args.root_path}\"")
        print("Exiting program...")
        sys.exit(1)

    # Get content size of all top-level items
    top_level_items = []

    for item in os.listdir(args.root_path):
        item_path = os.path.join(args.root_path, item)

        if os.path.isfile(item_path):
            item_type = 'file'
            item_size = os.path.getsize(item_path)
        else:
            item_type = 'folder'
            item_size = get_content_size(item_path)

        top_level_items.append((item, item_type, item_size))

    # Source: https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value#:~:text=Adding%20to%20Cheeken%27s%20answer%2C%20This%20is%20how%20you%20sort%20a%20list%20of%20tuples%20by%20the%202nd%20item%20in%20descending%20order.
    top_level_items = sorted(top_level_items, key=lambda x: x[2], reverse=True)

    # Create displayed table in console
    df = pd.DataFrame(data=top_level_items, columns=('File', 'Type', 'Size'))
    df.index += 1

    # Display and exit if user didn't specify unit
    if args.unit is None:
        print(df)
        sys.exit(0)

    # Display in user-specified unit
    unit = args.unit
    if unit == 'gib':
        divisor = KIBIBYTE * KIBIBYTE * KIBIBYTE
    elif unit == 'mib':
        divisor = KIBIBYTE * KIBIBYTE
    elif unit == 'kib':
        divisor = KIBIBYTE
    elif unit == 'gb':
        divisor = KILOBYTE * KILOBYTE * KILOBYTE
    elif unit == 'mb':
        divisor = KILOBYTE * KILOBYTE
    else:  # kb
        divisor = KILOBYTE

    df['Size'] = df['Size'].div(divisor).round(1)
    print(f"Size unit: {unit}")
    print(df)
