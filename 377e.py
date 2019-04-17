# reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/

import itertools

def fit1(X, Y, x, y):
  return (X//x) * (Y//y)

def fit2(X,Y,x,y):
  return max([fit1(X,Y,x,y),
              fit1(X,Y,y,x)])

def fit3(X,Y,Z,x,y,z):
  def fit_help(x,y,z):
    return (X//x)*(Y//y)*(Z//z)
    
  most = 0
  for orientation in itertools.permutations([x,y,z]):
    boxes = fit_help(*orientation)
    if boxes > most:
      most = boxes
  return most

def fitn(crate,box):
  def fit_help(box):
    boxes = 1
    for c, dim in enumerate(crate):
      boxes *= dim//box[c]
    return boxes

  most = 0
  for orientation in itertools.permutations(box):
    boxes = fit_help(orientation)
    if boxes > most:
      most = boxes
  return most
  
