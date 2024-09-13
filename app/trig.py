from random import *

help_text = """
<b>Основные тригонометрические тождества</b>:

<code>sin²(x) = 1-cos²(x)

cos²(x) = 1-sin²(x)

sin²(x) + cos²(x) = 1

tg(x) = sin(x)/cos(x)

ctg(x) = cos(x)/sin(x)</code>

<b>Свойства функций чётности</b>:

<code>cos(-x) = cos(x)

sin(-x) = -sin(x)

tg(-x) = -tg(x)

ctg(-x) = -ctg(x)</code>

<b>Дополнительные тождества</b>:

<code>tg(x)*ctg(x) = 1

1 + tg²(x) = 1/cos²(x)

1 + ctg²(x) = 1/sin²(x)</code>

<b>Формулы сложения</b>:

<code>sin(x+y) = sin(x)*cos(y) + cos(x)*sin(y)

sin(x-y) = sin(x)*cos(y) - cos(x)*sin(y)

cos(x+y) = cos(x)*cos(y) - sin(x)*sin(y)

cos(x-y) = cos(x)*cos(y) + sin(x)*sin(y)</code>

<b>Формулы двойного угла</b>:

<code>sin(2x) = 2sin(x)cos(x)

cos(2x) = cos²(x) - sin²(x)

cos(2x) = 2cos²(x) - 1

cos(2x) = 1 - 2sin²(x)</code>

<b>Сумма и разность тригонометрических функций</b>

<code>sin(x) + sin(y) = 2sin(x+y/2)*cos(x-y/2)

sin(x) - sin(y) = 2sin(x-y/2)*cos(x+y/2)

cos(x) + cos(y) = 2cos(x+y/2)*cos(x-y/2)

cos(x) - cos(y) = -2sin(x+y/2)*sin(x-y/2)</code>

<b>Табличные значения</b>

<code>sin(0°) = 0
sin(30°) = 1/2
sin(45°) = √2/2
sin(60°) = √3/2
sin(90°) = 1
sin(180°) = 0

cos(0°) = 1
cos(30°) = √3/2
cos(45°) = √2/2
cos(60°) = 1/2
cos(90°) = 0
cos(180°) = -1

tg(0°) = 0
tg(30°) = √3/3
tg(45°) = 1
tg(60°) = √3
tg(90°) = не сущ
tg(180°) = 0

ctg(0°) = не сущ
ctg(30°) = √3
ctg(45°) = 1
ctg(60°) = √3/3
ctg(90°) = 0
ctg(180°) = не сущ</code>
"""

formulas = [
  {"question": "sin²(x)", "answer": "1-cos²(x)"},
  {"question": "cos²(x)", "answer": "1-sin²(x)"},
  {"question": "sin²(x) + cos²(x)", "answer": "1"},
  {"question": "tg(x)", "answer": "sin(x)/cos(x)"},
  {"question": "ctg(x)", "answer": "cos(x)/sin(x)"},
  {"question": "cos(-x)", "answer": "cos(x)"},
  {"question": "sin(-x)", "answer": "-sin(x)"},
  {"question": "tg(-x)", "answer": "-tg(x)"},
  {"question": "ctg(-x)", "answer": "-ctg(x)"},
  {"question": "tg(x)*ctg(x)", "answer": "1"},
  {"question": "1 + tg²(x)", "answer": "1/cos²(x)"},
  {"question": "1 + ctg²(x)", "answer": "1/sin²(x)"},
  {"question": "sin(x+y)", "answer": "sin(x)*cos(x) + cos(x)*sin(y)"},
  {"question": "sin(x-y)", "answer": "sin(x)*cos(y) - cos(x)*sin(y)"},
  {"question": "cos(x+y)", "answer": "cos(x)*cos(y) - sin(x)*sin(y)"},
  {"question": "cos(x-y)", "answer": "cos(x)*cos(y) + sin(x)*sin(y)"},
  {"question": "sin(2x)", "answer": "2sin(x)cos(x)"},
  {"question": "cos(2x)", "answer": "cos²(x) - sin²(x)"},
  {"question": "cos(2x)", "answer": "2cos²(x) - 1"},
  {"question": "cos(2x)", "answer": "1 - 2sin²(x)"},
  {"question": "sin(x) + sin(y)", "answer": "2sin(x+y/2)*cos(x-y/2)"},
  {"question": "sin(x) - sin(y)", "answer": "2sin(x-y/2)*cos(x+y/2)"},
  {"question": "cos(x) + cos(y)", "answer": "2cos(x+y/2)*cos(x-y/2)"},
  {"question": "cos(x) - cos(y)", "answer": "-2sin(x+y/2)*sin(x-y/2)"},

]

# {"question": "sin(0°)", "answer": "0"},
# {"question": "sin(30°)", "answer": "1/2"},
# {"question": "sin(45°)", "answer": "√2/2"},
# {"question": "sin(60°)", "answer": "√3/2"},
# {"question": "sin(90°)", "answer": "1"},
# {"question": "sin(180°)", "answer": "0"},
# {"question": "cos(0°)", "answer": "1"},
# {"question": "cos(30°)", "answer": "√3/2"},
# {"question": "cos(45°)", "answer": "√2/2"},
# {"question": "cos(60°)", "answer": "1/2"},
# {"question": "cos(90°)", "answer": "0"},
# {"question": "cos(180°)", "answer": "-1"},
# {"question": "tg(0°)", "answer": "0"},
# {"question": "tg(30°)", "answer": "√3/3"},
# {"question": "tg(45°)", "answer": "1"},
# {"question": "tg(60°)", "answer": "√3"},
# {"question": "tg(90°)", "answer": "не сущ"},
# {"question": "tg(180°)", "answer": "0"},
# {"question": "ctg(0°)", "answer": "не сущ"},
# {"question": "ctg(30°)", "answer": "√3"},
# {"question": "ctg(45°)", "answer": "1"},
# {"question": "ctg(60°)", "answer": "√3/3"},
# {"question": "ctg(90°)", "answer": "0"},
# {"question": "ctg(180°)", "answer": "не сущ"},