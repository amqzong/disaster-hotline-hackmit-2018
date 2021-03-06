#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from flask import Flask, render_template, request
from operator import itemgetter, attrgetter
from revsample import main_rev
app = Flask(__name__)
app.config['DEBUG']=True
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/process')
def transcribe():
	main_rev()

if __name__ == '__main__':
    app.run()