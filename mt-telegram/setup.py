import subprocess

def install_libraries(libs):
    for lib in libs:
        subprocess.check_call(['pip', 'install', lib])

libraries_to_install = ['flask', 'request', 'requests', 'rich', 'Console', 'time', 'sleep', 'datetime', 'webbrowser']


install_libraries(libraries_to_install)