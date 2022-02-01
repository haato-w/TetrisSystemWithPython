# TetrisSystemWithPython

テトリスプログラムです。<br>
Pythonで実装しており、ゲーム処理部分はサーバー、GUI部分をクライアントとして通信する形になっています。<br>
ゲームオーバー時に消した行数ををポイントとして表示します。<br>

![tetris_python_single](https://user-images.githubusercontent.com/64346215/151933951-9f4c6b53-276d-46e2-9377-7e5a3ebe15f3.gif)


## 【実行方法】
1. Pythonが実行できる環境にプログラムを設置する
2. player.pyを実行する
3. client_gui.pyを実行する
4. ゲーム開始
5. ゲーム終了後 ポイントがコマンドラインに表示される

## 【操作方法】
キーボード操作になります<br>
w: ミノの向きを変更<br>
d: ミノを右に移動<br>
s: ミノを下に移動<br>
a: ミノを左に移動<br>

## 【詳細】
ミノに色はついていません。<br>

言語：Python<br>
GUI：Tkinter<br>

client_gui.py：GUIを実装　通信ではクライアント部分<br>
mino_shapes.py：ミノの形を表すデータを保持<br>
player.py：ゲーム処理を実装　通信ではサーバー部分<br>
