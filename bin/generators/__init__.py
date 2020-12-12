from bin.constants import *
import os
import shutil
import traceback

def generate(params):
  opt = {
    'blueprint': blueprint,
    'controller': controller
  }
  handler = opt[params[0]]
  handler(params[1:])

#g blueprint [name]
def blueprint(params):
  bp_name = params[0]
  bp_name_camel = [w.capitalize() for w in bp_name.split('_')]
  bp_name_camel = ''.join(bp_name_camel)
  nbp = f'{BPP}/{bp_name}'
  os.mkdir(nbp)
  routes = f'{nbp}/routes.yaml'
  os.mkdir(f'{nbp}/models')
  os.mkdir(f'{nbp}/templates')
  os.mkdir(f'{nbp}/templates/{bp_name}')
  os.mkdir(f'{nbp}/views')
  src = BP_INIT
  dest = f'{nbp}/__init__.py'
  shutil.copyfile(src, dest)
  with open(dest, 'rt') as bps:
    cont = []
    bp_name = params[0]
    for li in bps.readlines():
      cont.append(li.format(bp_name=bp_name, bp_name_camel=bp_name_camel))
          
  with open(dest, 'wt') as bps:
    bps.writelines(cont)
    
  src = BP_TP
  dest = f'{nbp}/templates/{bp_name}/index.html'
  shutil.copyfile(src, dest)
  with open(dest, 'rt') as tps:
    cont = []
    for li in tps.readlines():
      try:
        cont.append(
        li.format(
          bp_name_camel=bp_name_camel))
          
      except KeyError:
        pass
      
  with open(dest, 'wt') as tps:
    tps.writelines(cont)
    
  with open(routes, 'wt') as rtf:
    rt_cont = [
      '# register your routes here\n',
      '# they will be loaded in app startup\n',
      '# no need to use conventional Flask routing\n',
      f'root: {bp_name}_views.index'
    ]
    rtf.writelines(rt_cont)
    
  print(f'Blueprint {bp_name} created')

#g controller [name] in [bp_name]
def controller(params):
  pass
  