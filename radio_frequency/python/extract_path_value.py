import sys
import argparse

def read_config(file_path):
    config = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                    else:
                        parts = line.split(None, 1)
                        if len(parts) < 2:
                            continue
                        key, value = parts
                    config[key.strip()] = value.strip()
        return config
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
        sys.exit(1)

def get_value(config, key):
    if key in config:
        return config[key]
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="путь к файлу", required=True)
    parser.add_argument("--key", help="ключ", required=True)
    args = parser.parse_args()
    
    file_path = args.path
    key = args.key
    
    config = read_config(file_path)
    value = get_value(config, key)
    
    if value is not None:
        print(value)
    else:
        print(f"ключ '{key}' не найден в '{file_path}'", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()