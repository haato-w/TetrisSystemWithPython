# TetrisSystemWithPython

テトリスプログラムです。
Pythonで実装しており、ゲーム処理部分はサーバー、GUI部分をクライアントとして通信する形になっています。
ゲームオーバー時に消した行数ををポイントとして表示します。




# 【実行方法】
1. Pythonが実行できる環境にプログラムを設置する
2. player.pyを実行する
3. client_gui.pyを実行する
4. ゲーム開始
5. ゲーム終了後 ポイントがコマンドラインに表示される

# 【詳細】
ミノに色はついていません。

言語：Python
GUI：Tkinter

client_gui.py：GUIを実装　通信ではクライアント部分
mino_shapes.py：ミノの形を表すデータを保持
player.py：ゲーム処理を実装　通信ではサーバー部分
