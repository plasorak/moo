#!/usr/bin/env python3
'''
Generate artifacts from models.
'''
import os
import sys
import jsonnet
from jinja2 import Environment, FileSystemLoader

def render_default(template, params):
    env =  Environment(loader = FileSystemLoader(os.path.dirname(template)),
                       extensions=['jinja2.ext.do'])
                       
    tmpl = env.get_template(os.path.basename(template))
    return tmpl.render(**params)



for one in sys.argv[1:]:
    dat = jsonnet.load(one)

    render = eval("render_" + dat.get("renderer", "default"))
    text = render(dat["template"], dat["params"])
    output = dat["artifact"]
    open(dat["artifact"], 'wb').write(text.encode('utf-8'))
    print (output)

