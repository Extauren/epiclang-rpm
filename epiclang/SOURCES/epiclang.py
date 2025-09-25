import os
import sys
import glob
import subprocess

EPICLANG_PLUGINS_DIRS = [
    '/usr/lib/epiclang/plugins',
    '/usr/local/lib/epiclang/plugins',
]
BASE_COMMAND = 'clang-20'


def main():
    final_command = [BASE_COMMAND]

    for plugins_dir in EPICLANG_PLUGINS_DIRS:
        if os.path.exists(plugins_dir):
            for plugin in glob.glob(os.path.join(plugins_dir, '*.so')):
                if os.path.isfile(plugin):
                    final_command.extend([f'-fplugin={plugin}'])

    final_command.extend(sys.argv[1:])

    try:
        subprocess.run(final_command, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
    except FileNotFoundError:
        print(f"Error: {BASE_COMMAND} not found in PATH", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
