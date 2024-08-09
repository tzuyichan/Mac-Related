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
