#!/usr/bin/python

import os
import re
import sys


def clean_html(raw_html):
	cleanr = re.compile('<(.|\n)*?>')
	clean_text = re.sub(cleanr, '', raw_html)
	return clean_text


def convert_bytes_to_string(bytes_text):
	pattern = re.compile(r'''(?<![^\t\n])\W*b(["'])(.*?)\1\W*?(?![^\t\n])''')
	string_text = pattern.sub(r'\2', bytes_text)
	return string_text


def remove_html_tags_from_file(src_file_path, dest_file_path):
	if not os.path.exists(src_file_path):
		print(src_file_path + ' does not exist!')
		sys.exit(1)

	src_file = open(src_file_path, 'rb')
	contents = str(src_file.read(), encoding='latin1')
	contents = contents.strip()

	src_file.close()

	clean_contents = clean_html(contents)

	dest_file = open(dest_file_path, 'w')
	dest_file.write(clean_contents)
	dest_file.close()


def main():
	total_files = 2500
	base_src_path = 'dataset/extracted/TR/TRAIN_'
	base_dest_path = 'dataset/text/TR/TRAIN_'
	for i in range(1, total_files + 1):
		remove_html_tags_from_file('{}{}.eml'.format(base_src_path, str(i)), '{}{}.txt'.format(base_dest_path, str(i)))

	total_files = 1827
	base_src_path = 'dataset/extracted/TT/TEST_'
	base_dest_path = 'dataset/text/TT/TEST_'
	for i in range(1, total_files + 1):
		remove_html_tags_from_file('{}{}.eml'.format(base_src_path, str(i)), '{}{}.txt'.format(base_dest_path, str(i)))


if __name__ == '__main__':
	main()