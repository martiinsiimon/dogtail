#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, unicode_literals
import dogtail.predicate
import dogtail.tree
from gtkdemotest import GtkDemoTest
import unittest

"""
Unit tests for the dogtail.procedural API
"""
__author__ = "Zack Cerza <zcerza@redhat.com>"

dogtail.config.config.logDebugToFile = False
dogtail.config.config.logDebugToStdOut = True


class TestScreenshot(GtkDemoTest):

    def make_expected_and_compare(self, actual_path, jpg_tolerance=None):
        extension = actual_path.split('.')[-1]
        expected_path = actual_path.replace(extension, "expected." + extension)

        import os
        os.system("gnome-screenshot -f %s" % expected_path)

        command = ["compare", "-metric", "MAE",
                   actual_path, expected_path, "output"]
        import subprocess
        p = subprocess.Popen(command, stderr=subprocess.PIPE)
        output, error = p.communicate()

        import re
        m = re.search(r"\((.*)\)", str(error))
        self.assertTrue(0.1 >= float(m.group(1)))

    def test_screenshot_incorrect_timestamp(self):
        self.assertRaises(
            TypeError, dogtail.utils.screenshot, "timeStamp", None)

    def test_screenshot_default(self):
        actual_path = dogtail.utils.screenshot()
        self.make_expected_and_compare(actual_path)

    def test_screenshot_basename(self):
        actual_path = dogtail.utils.screenshot("basename")
        self.make_expected_and_compare(actual_path)

    def test_screenshot_no_time_stamp(self):
        actual_path = dogtail.utils.screenshot(timeStamp=False)
        self.make_expected_and_compare(actual_path)

    def test_screenshot_jpeg(self):
        actual_path = dogtail.utils.screenshot("basename.jpg")
        self.make_expected_and_compare(actual_path, jpg_tolerance=True)

    def test_screenshot_unknown_format(self):
        self.assertRaises(ValueError, dogtail.utils.screenshot, "basename.dat")


class TestA11Y(unittest.TestCase):

    def test_bail_when_a11y_disabled(self):
        self.assertRaises(SystemExit, dogtail.utils.bailBecauseA11yIsDisabled)

    def test_enable_a11y(self):
        dogtail.utils.enableA11y()
