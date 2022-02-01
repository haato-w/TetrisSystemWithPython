# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
import keyboard
import socket
import threading


class client_gui:
    
    #ウィンドウクローズボタンが押されたときに呼び出されるメソッド
    def on_closing(self, root):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            #self.sock.close()
            root.destroy()
        return
            
    
    #引数として方向を受け取り、サーバーに送信するメソッド
    #4桁の数字の文字列として送信する
    def send(self, dirc_y, dirc_x):
        if (dirc_y>=0):
            send_str_y = "0" + str(dirc_y)
        else:
            send_str_y = str(dirc_y)
        
        if (dirc_x>=0):
            send_str_x = "0" + str(dirc_x)
        else:
            send_str_x = str(dirc_x)
        
        send_str = send_str_y + send_str_x
        self.sock.send(send_str.encode())
        
    
    """
    #サーバーからメッセージを受け取り、GUIの色を変更するメソッド
    #別スレッドで動く
    def receive_direction(self, bufsize):
        
        while(True):
            displaybuffer = []
            
            #サーバーからのメッセージを受信
            recev_value = self.sock.recv(bufsize).decode()
            if recev_value == 'end':
                break
            
            #print("recev_value: ")
            #print(recev_value)
            
            #送られてきた値を displaybufferに変換
            for i in range(0, 20):
                displaybuffer.append(list(recev_value[i*10:(i+1)*10]))
            #print("displaybuffer: ", end='')
            #print(displaybuffer)
            
            #print(displaybuffer[0][2])
            
            #displaybufferの値をfieldcells(GUIの色)に反映
            print("refresh display")
            for i in range(0, 20):
                for j in range(0, 10):
                    if displaybuffer[i][j] == '0':
                        self.fieldcells[i][j].itemconfig("cell", fill="black")
                    else:
                        self.fieldcells[i][j].itemconfig("cell", fill="white")
    """
    
    def print_buffer(self):
        for i in range(0, 20):
            for j in range(0, 10):
                print(self.displaybuffer[i][j], end='')
            print('')
            
    
    #サーバーからメッセージを受け取り、GUIの色を変更するメソッド
    #別スレッドで動く
    def receive_direction(self, bufsize):
        
        while(True):
            displaybuffer = []
            
            #サーバーからのメッセージを受信
            recev_value = self.sock.recv(bufsize).decode()
            if recev_value == 'end':
                break
            
            #print("recev_value: ")
            #print(recev_value)
            
            
            player_num = recev_value[0]
            recev_value = recev_value[1:]
            
            #送られてきた値を displaybufferに変換
            for i in range(0, 20):
                displaybuffer.append(list(recev_value[i*10:(i+1)*10]))
            #print("displaybuffer: ", end='')
            #print(displaybuffer)
            
            #print(displaybuffer[0][2])
            #displaybufferの値をfieldcells(GUIの色)に反映
            print("refresh display")
            
            
            #送られてきた情報が自分の情報だった場合
            if (player_num == "0"):
                for i in range(0, 20):
                    for j in range(0, 10):
                        if displaybuffer[i][j] == '0':
                            self.fieldcells1[i][j].itemconfig("cell", fill="black")
                        else:
                            self.fieldcells1[i][j].itemconfig("cell", fill="white")
            
            #送られてきた情報が相手の情報だった場合
            elif (player_num == "1"):
                for i in range(0, 20):
                    for j in range(0, 10):
                        if displaybuffer[i][j] == '0':
                            self.fieldcells2[i][j].itemconfig("cell", fill="black")
                        else:
                            self.fieldcells2[i][j].itemconfig("cell", fill="white")
    
            elif (player_num == "-"):
                self.sock.close()
                print("".join(recev_value))
                break
    
    
    """
    client_guiのコンストラクタ
    """
    def __init__(self, mode):

        """
        GUIを生成
        """
        root = tk.Tk()
        root.title(u'canvas')
        
        
        if mode == "single":
            
            self.fieldcells1 = []
            
            root.geometry('200x400')
            root.configure(background='blue')
            
            #cell面の構築
            for i in range(20):
                tmp = []
                for j in range(10):
                    tmp.append(tk.Canvas(root, width = 20, height = 20, bg='red', highlightthickness=0))
                    tmp[j].create_rectangle(0, 0, 20, 20, fill = 'white', tag="cell")
                    tmp[j].grid(row=i, column=j, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.N+tk.E+tk.S+tk.W)  
                self.fieldcells1.append(tmp)
            
            """
            #セル色の変更
            self.x=4
            self.y=5
            self.fieldcells[self.x][self.y].itemconfig("cell", fill="black")
            #fieldcells[2][5].itemconfig("cell", fill="black")
            """
            
        elif mode == "multi":
            
            self.fieldcells1 = []
            self.fieldcells2 = []
            
            root.geometry('480x400')
            root.configure(background='blue')
            
            #cell面の構築
            for i in range(20):
                tmp = []
                for j in range(10):
                    tmp.append(tk.Canvas(root, width = 20, height = 20, bg='red', highlightthickness=0))
                    tmp[j].create_rectangle(0, 0, 20, 20, fill = 'white', tag="cell", outline='gray')
                    tmp[j].grid(row=i, column=j, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.N+tk.E+tk.S+tk.W)  
                self.fieldcells1.append(tmp)
                
            for i in range(20):
                for j in range(4):
                    space = tk.Canvas(root, width = 20, height = 20, bg='skyblue', highlightthickness=0)
                    space.grid(row=i, column=j+10, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.N+tk.E+tk.S+tk.W)
            
            for i in range(20):
                tmp = []
                for j in range(10):
                    tmp.append(tk.Canvas(root, width = 20, height = 20, bg='yellow', highlightthickness=0))
                    tmp[j].create_rectangle(0, 0, 20, 20, fill = 'white', tag="cell", outline='gray')
                    tmp[j].grid(row=i, column=j+14, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.N+tk.E+tk.S+tk.W)  
                self.fieldcells2.append(tmp)
        
        
        
        root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root))
        
        keyboard.on_press_key("r", lambda _:print("r"))
        
        keyboard.on_press_key("w", lambda _:self.send(0, 0))
        keyboard.on_press_key("d", lambda _:self.send(0, 1))
        keyboard.on_press_key("s", lambda _:self.send(1, 0))
        keyboard.on_press_key("a", lambda _:self.send(0, -1))
        
        
        """
        通信処理
        """
        
        host = '127.0.0.1'
        #host = '10.65.230.5'
        port = 50001
        bufsize = 4096

        #ソケットを生成
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        
        #サーバーから動く方向を受け取るメソッド receive_directionを別スレッドで起動する
        thread1 = threading.Thread(target=self.receive_direction, args=(bufsize,))
        thread1.start()
        
        
            
        root.mainloop()
        
        

if __name__ == "__main__":
    client_gui("single")


