# 変数定義
x = 1
y = 2

# wrong
xxxx = 1
zz   = 2

# 関数の引数の「=」にはスペース不要
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# operatorの周りにスペース１つ, 優先度がある場合はスペースをなくす
x = x + 1
x += 1
x = x*2 + 1
a = x*y + y*zz

# カンマの後にはスペース
range(1, 11)
a = [1, 2, 3, 4]

# 閉じ括弧を改行しておく、最後の要素にもカンマをつけておく
FILES = [
    'xxxx',
    'yyyy',
]

# 行の折り返し
# 引数の頭を揃える
foo = long_function_name(yyyyyyyy,ssssssss, wwwww,
                         dddddd,ffffff)

foo = long_function_name(
    yyyyyyyy,ssssssss, wwwww,
    dddddd,ffffff,
)

def long_function_name(
        one, two, three,):
    print(one)

# '\'で区切って改行する
print("xxxxxxxxxxxxxxx\
xxxxxxxxxxx")

a = 10000000000 \
    + 10000000000 \
    + 10000000000 \
    + 10000000000 \
    + 10000000000 \
    + 10000000

# 関数間は二行開ける
def func():
    pass


def func():
    pass


# importの書き方
# 一番上に書く
import os
import sys
from subprocess import Popen

# コメントの書き方
# なるべく英語で書く
# 書くときは文章で書くと望ましい
#  # の後に半角スペース
# ドッグストリングは基本的に全てのモジュール、関数の、メソッドにつける
# そのコードが何をしているかよりもなぜそう書いたかが有益

# 命名規則
# 変数や関数　スネークケース
# クラス名　キャメルケース
# 定数　大文字

# アンスコ
# _xxx ノンパブリックの意味
# xxx_ Pythonですでに使われている単語を使いたいとき　type_
# __xxx  クラスの属性として使うと名前修飾される
# __xxx___ マジックメソッドと呼ばれる　開発者が定義することはない
# _ 最近実行した戻り値やイテレーション時に使わない変数
for _ in range(10):
    print("hello")

# return
# 一方を書くなら両方書く
def foo(x):
    if x <= 0:
        return math.sprt(x)
    else:
        return None

# オブジェクトタイプの確認はisinstance()を使う
# correct
if isinstance(obj, int):

if type(obj) is type(1):

# Booleanに比較演算子を使わない
bool_ver = True
# correct
if bool_ver:
# wrong
if bool_ver == True:

# type hint
def greeting(name:str) -> str:
    return "hello" + name
# 一つでもhintをつけたら全てにつける
# Pythonがtypeのチェックをするわけではない
# Pythonは動的型付け言語
