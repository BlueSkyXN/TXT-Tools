import configparser
import codecs
import argparse
import os

# 解析命令行参数
parser = argparse.ArgumentParser(description='Merge txt files based on the configuration file.')
parser.add_argument('-c', '--config', default='config.ini', help='path to the configuration file')
args = parser.parse_args()

# 读取配置文件
config = configparser.ConfigParser()
with codecs.open(args.config, 'r', encoding='utf-8') as file:
    config.read_file(file)

# 获取配置信息
input_file_list = config.get('General', 'input_file_list')
output_file = config.get('General', 'output_file')
file_encoding = config.get('General', 'file_encoding', fallback='utf-8')

def merge_txt_files(file_list, output_file, encoding):
    try:
        with open(file_list, 'r') as f:
            file_paths = f.read().splitlines()
    except Exception as e:
        print(f"Error opening file list: {e}")
        return

    try:
        with codecs.open(output_file, 'w', encoding=encoding) as outfile:
            for file_path in file_paths:
                try:
                    with codecs.open(file_path, 'r', encoding=encoding) as infile:
                        for line in infile:
                            outfile.write(line)
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    except Exception as e:
        print(f"Error writing to output file: {e}")

merge_txt_files(input_file_list, output_file, file_encoding)
