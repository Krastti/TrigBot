from random import *

help_text = [
  ("sin^2(x) = 1-cos^2(x)"),
  (""),
  ("cos^2(x) = 1-sin^2(x)"),
  ("sin^2(x)+cos^2(x) = 1"),
  ("tg(x) = sin(x)/cos(x)"),
  ("ctg(x) = cos(x)/sin(x)"),
  (""),
  ("cos(-x) = cos(x)"),
  ("sin(-x) = -sin(x)"),
  ("tg(-x) = -tg(x)"),
  ("ctg(-x) = -ctg(x)"),
  (""),
  ("tg(x)*ctg(x) = 1"),
  ("1+tg^2(x) = 1/cos^2(x)"),
  ("1+ctg^2(x) = 1/sin^2(x)"),
  (""),
  ("sin(x+y) = sin(x)*cos(x)+cos(x)*sin(y)"),
  ("sin(x-y) = sin(x)*cos(y)-cos(x)*sin(y)"),
  ("cos(x+y) = cos(x)*cos(y)-sin(x)*sin(y)"),
  ("cos(x-y) = cos(x)*cos(y)+sin(x)*sin(y)"),
  (""),
  ("sin(2x) = 2sin(x)cos(x)"),
  ("cos(2x) = cos^2(x)-sin^2(x)"),
  ("cos(2x) = 2cos^2(x)-1"),
  ("cos(2x) = 1-2sin^2(x)"),
  (""),
]

formulas = [
  {"question": "sin^2(x)", "answer": "1-cos^2(x)"},
  {"question": "cos^2(x)", "answer": "1-sin^2(x)"},
  {"question": "sin^2(x)+cos^2(x)", "answer": "1"},
  {"question": "tg(x)", "answer": "sin(x)/cos(x)"},
  {"question": "ctg(x)", "answer": "cos(x)/sin(x)"},
  {"question": "cos(-x)", "answer": "cos(x)"},
  {"question": "sin(-x)", "answer": "-sin(x)"},
  {"question": "tg(-x)", "answer": "-tg(x)"},
  {"question": "ctg(-x)", "answer": "-ctg(x)"},
  {"question": "tg(x)*ctg(x)", "answer": "1"},
  {"question": "1+tg^2(x)", "answer": "1/cos^2(x)"},
  {"question": "1+ctg^2(x)", "answer": "1/sin^2(x)"},
  {"question": "sin(x+y)", "answer": "sin(x)*cos(x)+cos(x)*sin(y)"},
  {"question": "sin(x-y)", "answer": "sin(x)*cos(y)-cos(x)*sin(y)"},
  {"question": "cos(x+y)", "answer": "cos(x)*cos(y)-sin(x)*sin(y)"},
  {"question": "cos(x-y)", "answer": "cos(x)*cos(y)+sin(x)*sin(y)"},
  {"question": "sin(2x)", "answer": "2sin(x)cos(x)"},
  {"question": "cos(2x)", "answer": "cos^2(x)-sin^2(x)"},
  {"question": "cos(2x)", "answer": "2cos^2(x)-1"},
  {"question": "cos(2x)", "answer": "1-2sin^2(x)"},
]