# Copyright 2017 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Reads a multi-document yaml from standard in and writes to standard out in reverse object order."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import yaml


def main():

    inputs = sys.stdin.read()

    content = yaml.dump_all(
        reversed([x for x in yaml.load_all(inputs, Loader=yaml.SafeLoader)]))

    print(content)


if __name__ == '__main__':
    main()
