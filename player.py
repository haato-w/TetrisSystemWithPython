# -*- coding: utf-8 -*-

import math
import random
import time
import copy
import socket
import threading
import select
from enum import IntEnum

from mino_shapes import mino_shapes


class MINO_TYPE(IntEnum):
    MINO_TYPE_I = 0
    MINO_TYPE_O = 1
    MINO_TYPE_S = 2
    MINO_TYPE_Z = 3
    MINO_TYPE_J = 4
    MINO_TYPE_L = 5
    MINO_TYPE_T = 6
    MINO_TYPE_MAX = 7

class MINO_ANGLE(IntEnum):
    MINO_ANGLE_0 = 0
    MINO_ANGLE_90 = 1
    MINO_ANGLE_180 = 2
    MINO_ANGLE_270 = 3
    MINO_ANGLE_MAX = 4


class player():
    
    """
    playerクラスのフィールド群
    """
    field = []#壁＋壁と同化したミノを記録
    displayBuffer = []#壁と落ちている最中のミノを記録→fieldCellsに反映
    
    FIELD_HEIGHT = 22
    FIELD_WIDTH = 12
    
    MINO_WIDTH = 4
    MINO_HEIGHT = 4
    
    mino_x = 5
    mino_y = 0
    mino_type = 0
    mino_angle = 0
    
    mino_shape = mino_shapes().mino_shapes
    
    
    
    """
    send
    displayBufferの情報を文字列に変換してサーバーに送信するメソッド
    """
    def send(self):
        
        #フィールド値を更新
        self.displayBuffer = copy.deepcopy(self.field)

        #mino_shape(現在落ちているミノ)をdisplayBufferに書き込む
        for i in range(self.MINO_HEIGHT):
            for j in range(self.MINO_WIDTH):
                remitted_mino_y, remitted_mino_x = self.index_remitter(self.mino_y + i, self.mino_x + j)
                #print("remitted_mino_y: " + str(remitted_mino_y))
                #print("remitted_mino_x: " + str(remitted_mino_x))
                self.displayBuffer[remitted_mino_y][remitted_mino_x] |= self.mino_shape[self.mino_type][self.mino_angle][i][j]
	    
        #print(self.displayBuffer)
        
        send_str = ""
        #print("flag1")
        send_str = "0"
        for i in range(1, 21):
            for j in range(1, 11):
                send_str += str(self.displayBuffer[i][j])
        #print("send_str: ", end='')
        #print(send_str)
        encoded_send_str = send_str.encode()
        self.conn_this.send(encoded_send_str)
        
        #対戦プレイの場合、相手の画面にも送信する
        if not (self.conn_opponent == None):
            send_str = send_str[1:]
            send_str = "1" + send_str
            encoded_send_str = send_str.encode()
            self.conn_opponent.send(encoded_send_str)
        
    
    
    """
    receive_direction
    クライアントからミノの操作情報を受け取り、セルを更新しsendメソッドを呼び出すメソッド
    game_loopとは別スレッドで動く
    """
    def receive_direction(self, bufsize):
        while self.receive_flag:
            #r_ready_sockets, w_ready_sockets, e_ready_sockets = select.select([self.conn_this], [], [])
            try:
                b_msg = self.conn_this.recv(bufsize) #クライアントからデータを受信
                msg = b_msg.decode('utf-8') #デコード
                print('received msg:' + msg)
                
                if msg == '':
                    continue
                
                y_dir = int(msg[0:2])
                x_dir = int(msg[2:4])
                
                if (y_dir == 0) and (x_dir == 0):
                    if not (self.is_hit(self.mino_x, self.mino_y, self.mino_type, (self.mino_angle + 1) % MINO_ANGLE.MINO_ANGLE_MAX)):
                        self.mino_angle = (self.mino_angle + 1) % MINO_ANGLE.MINO_ANGLE_MAX
                else:
                    if not (self.is_hit(self.mino_x + x_dir, self.mino_y + y_dir, self.mino_type, self.mino_angle)):
                        self.mino_y += y_dir
                        self.mino_x += x_dir
                    
                        #print("self.mino_y: " + str(self.mino_y))
                        #print("self.mino_x: " + str(self.mino_x))
                
                self.send()
            finally:
                pass
        print("exit while in receive_direction")
        self.conn_this.close()
        
    
    
    """
    indexRemmiter
    リストのインデックスy, xを引数とし、それぞれがBoundを超えていればインデックスをBoundの端に設定して
    返すメソッド
    """
    def index_remitter(self, fieldy_max, fieldx_max):
        if((fieldy_max) < 0):
            fieldy_max = 0
        if((fieldy_max) > self.FIELD_HEIGHT - 1):
            fieldy_max = self.FIELD_HEIGHT - 1
        if((fieldx_max) < 0):
            fieldx_max = 0
        if((fieldx_max) > self.FIELD_WIDTH - 1):
            fieldx_max = self.FIELD_WIDTH - 1
            
        return fieldy_max, fieldx_max
    
    
    
    """
    is_hit
    現在落ちているミノがfieldに接触するかを判定する
    接触する場合true、接触しない場合false
    """
    def is_hit(self, mino_x, mino_y, mino_type, mino_angle):
        #print("is_hit called")
        for i in range(self.MINO_HEIGHT):
            for j in range(self.MINO_WIDTH):
                remitted_mino_y, remitted_mino_x = self.index_remitter(mino_y + i, mino_x + j)
                if((self.mino_shape[mino_type][mino_angle][i][j] == 1) and (self.field[remitted_mino_y][remitted_mino_x] == 1)):
                    return True
                
        return False
    
    
    
    """
    reset_mino
    ミノの座標、Type、Angleをリセットする
    TypeとAngleはランダム
    """
    def reset_mino(self):
        #print("reset_mino called")
        self.mino_x = 5
        self.mino_y = 0
        self.mino_type = random.randint(0, MINO_TYPE.MINO_TYPE_MAX-1)
        self.mino_angle = random.randint(0, MINO_ANGLE.MINO_ANGLE_MAX-1)
    
    
    
    """
    start
    3秒カウントしてからgame_loopを呼び出す
    game_loopから呼び出される
    """
    def start(self):
        t = math.floor(time.time())
        count = 3
        while count > 0:
            t_new = math.floor(time.time())
            if t != t_new:
                t = t_new
                print(count)
                count -= 1
        
        #game_loopメソッドを起動
        score = self.game_loop()
        if (self.mode == "alone"):
            print("score: " + str(score))
            s = "-your score: " + str(score)
            self.conn_this.send(s.encode())
            
            #self.thread1.join()
            
            self.receive_flag = False
            
            print("end")
        
        else:
            return score
    
    
    """
    get_count_erase_line
    """
    def get_count_erase_line(self):
        return self.count_erase_line
    
    
    
    """
    game_loop
    ミノの落下、ミノと壁の同化、完全行の削除を行うメソッド
    """
    def game_loop(self):
        
        #クライアントからの操作情報を受け付けるreceive_directionメソッドを別スレッドで起動
        self.thread1 = threading.Thread(target=self.receive_direction, args=(self.bufsize,))
        self.thread1.start()
        
        self.reset_mino()
        t = math.floor(time.time())
        while (True):
            #エポック秒を取得
            t_new = math.floor(time.time())
            if t != t_new:
                t = t_new
                
                #現在落ちているミノが床に当たったときの処理
                if (self.is_hit(self.mino_x, self.mino_y+1, self.mino_type, self.mino_angle)):
                    #現在落ちているミノをfieldと同化させる
                    for i in range(self.MINO_HEIGHT):
                        for j in range(self.MINO_WIDTH):
                            remitted_mino_y, remitted_mino_x = self.index_remitter(self.mino_y + i, self.mino_x + j)
                            self.field[remitted_mino_y][remitted_mino_x] |=  self.mino_shape[self.mino_type][self.mino_angle][i][j]
                
                    
                    #埋まった行を消す処理
                    for i in range(self.FIELD_HEIGHT-1):
                        line_fill = True
                        for j in range(1, self.FIELD_WIDTH-1):
                            if (self.field[i][j] == 0):
                                line_fill = False
                        
                        if line_fill:
                            self.count_erase_line += 1
                            for j in range(1, self.FIELD_WIDTH-1):
                                self.field[i][j] = 0
                            for j in range(i, 0, -1):
                                #print("j: " + str(j) + " ", end='')
                                #print(self.field[j], end='')
                                #print(" → ", end='')
                                #print("j-1: " + str(j-1) + " ", end='')
                                #print(self.field[j-1])
                                self.field[j] = copy.deepcopy(self.field[j-1])
                    
                    
                    self.reset_mino()
                    
                    #終了判定 次のミノがfieldと被ったら終了
                    if(self.is_hit(self.mino_x, self.mino_y + 1, self.mino_type, self.mino_angle)):
                        break
                        
                else:
                    self.mino_y += 1
                
                self.send()
        
        print("player.py: ゲーム終了")
        return self.count_erase_line
    
                
                
    """
    playerクラスのコンストラクタ
    mode: aloneで一人プレイ用サーバーとして起動する、この場合conn_thisとconn_opponentはNone
    mode: controlledで対戦用サーバーとして起動する、この場合game_managerから生成される必要があり
    conn_thisは自身のプレイヤーのディスクリプタ、conn_opponentは相手プレイヤーのディスクリプタが入る
    """
    def __init__(self, mode, conn_this=None, conn_opponent=None):
        print("player is created")
        
        self.field = [[0 for _ in range(self.FIELD_WIDTH)] for _ in range(self.FIELD_HEIGHT)]
        
        for i in range(self.FIELD_HEIGHT):
            self.field[i][0] = self.field[i][self.FIELD_WIDTH-1] = 1
            
        for i in range(self.FIELD_WIDTH):
            self.field[self.FIELD_HEIGHT-1][i] = 1
        
        
        self.mode = mode
        self.conn_this = conn_this
        self.conn_opponent = conn_opponent
        
        self.count_erase_line = 0
        
        self.thread1 = None
        
        self.receive_flag = True
        
        
        self.bufsize = 4096
        
        #単体で動く場合はサーバーソケットを生成して、game_loopメソッドを起動する
        if (mode == "alone"):
            
            host = '127.0.0.1'
            #host = '10.65.230.5'
            port = 50001
            backlog = 10
            
            #ソケットを作成
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("socket is created")
            
            try:
                #ソケットにIPアドレスとポート番号をbind
                server_sock.bind((host, port))
                print("socket bind")
                #クライアントからの接続を待機
                #backlog:サーバーにacceptされていないクライアントのキューの最大長
                server_sock.listen(backlog)
                print("socket listen")
                
                #通信用ソケットを取得
                self.conn_this, address = server_sock.accept()
            
            except Exception as e:
                print("Exception!")
                print(e)
                server_sock.close()
            
        


        
if __name__ == "__main__":
    p = player("alone")
    p.start()
