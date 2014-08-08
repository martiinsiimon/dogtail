#!/usr/bin/env python3
__author__ = "Zack Cerza <zcerza@redhat.com>"

from distutils.core import setup
from distutils.command.bdist_rpm import bdist_rpm

def examples():
    import os
    exList = os.listdir(os.curdir + '/examples/')
    result = []
    for ex in exList:
        if ex.split('.')[-1] == 'py':
            result = result + ['examples/' + ex]
    return result

def examples_data():
    import os
    dataList = os.listdir(os.curdir + '/examples/data/')
    result = []
    for data in dataList:
        result = result + ['examples/data/' + data]
    return result

def tests():
    import os
    exList = os.listdir(os.curdir + '/tests/')
    result = []
    for ex in exList:
        if ex.split('.')[-1] == 'py':
            result = result + ['tests/' + ex]
    return result

def sniff_icons():
    import os
    list = os.listdir(os.curdir + '/sniff3/icons/')
    result = []
    for file in list:
        if file.split('.')[-1] in ('xpm'):
            result = result + ['sniff3/icons/' + file]
    return result

def icons(ext_tuple):
    import os
    list = os.listdir(os.curdir + '/icons/')
    result = []
    for file in list:
        if file.split('.')[-1] in ext_tuple:
            result = result + ['icons/' + file]
    return result

def scripts():
    import os
    list = os.listdir(os.curdir + '/scripts/')
    result = ['sniff3/sniff3']
    for file in list:
        result = result + ['scripts/' + file]
    return result

def session_file():
    result = ['scripts/gnome-dogtail-headless.session']
    return result

setup (
        name = 'dogtail3',
        version = '0.9.0-4.beta1',
        description = """GUI test tool and automation framework that uses Accessibility (a11y) technologies to communicate with desktop applications. Python3 compatible version.""",
        author = """Zack Cerza <zcerza@redhat.com>,
Ed Rousseau <rousseau@redhat.com>,
David Malcolm <dmalcolm@redhat.com>,
Vitezslav Humpa <vhumpa@redhat.com>""",
        author_email = 'dogtail-list@gnome.org',
        url = 'http://dogtail.fedorahosted.org/',
        packages = ['dogtail'],
        scripts = scripts(),
        data_files = [
                                ('share/doc/dogtail3/examples',
                                        examples() ),
                                ('share/doc/dogtail3/examples/data',
                                        examples_data() ),
                                ('share/doc/dogtail3/tests',
                                        tests() ),
                                ('share/dogtail3/glade', ['sniff3/sniff3.ui']),
                                ('share/dogtail3/icons', sniff_icons() ),
                                ('share/applications', ['sniff3/sniff3.desktop']),
                                ('share/icons/hicolor/48x48/apps', icons('png')),
                                ('share/icons/hicolor/scalable/apps', icons('svg'))
                                ],
        cmdclass = {
                'bdist_rpm': bdist_rpm
                }
)

# vim: sw=4 ts=4 sts=4 noet ai
