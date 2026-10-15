import tkinter as tk
from tkinter import messagebox, ttk
import datetime

class ShutdownApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('定时关机程序')
        self.root.geometry('400x200')  # 调整窗口高度，因为去掉了公告输入框

        default_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        
        # 时间选择组件
        self.time_label = tk.Label(self.root, text='选择倒计时时长:')
        self.time_var = tk.StringVar()
        self.time_combobox = ttk.Combobox(self.root, 
            values=['1分钟', '3分钟', '5分钟', '10分钟', '20分钟', '30分钟'],
            textvariable=self.time_var,
            state='readonly')
        self.time_combobox.current(2)  # 默认选择5分钟
        
        # 执行按钮
        self.execute_btn = tk.Button(self.root, text='立即执行', 
            command=lambda: self.start_countdown(
                self.parse_selected_time(self.time_combobox.get())
            ))
        
        # 布局
        self.time_label.pack(pady=10)
        self.time_combobox.pack()
        self.execute_btn.pack(pady=20)
        
        # 底部署名
        self.sign_label = tk.Label(self.root, text="胡歌 今天就到这吧~", font=('黑体', 12, 'bold'))
        self.sign_label.pack(side='bottom', pady=10)
        
        # 全屏提示窗口
        self.alert_window = None
        self.announcement_var = tk.StringVar()
        # 设置公告内容
        announcement_text = "电脑就要关机了 请你保存好重要的文件哦 今天的工作就到这了 您辛苦了~ 明天继续加油努力哦！！！"
        self.announcement_var.set(announcement_text)

    def show_time_picker(self):
        top = tk.Toplevel()
        top.title('选择时间')
        
        now = datetime.datetime.now()
        
        # 日期选择
        cal = ttk.DateEntry(top)
        cal.set_date(now.date())
        cal.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        # 时间选择组件
        tk.Label(top, text='时:').grid(row=1, column=0, padx=5)
        hour_var = tk.StringVar(value=str(now.hour).zfill(2))
        ttk.Combobox(top, textvariable=hour_var, values=[str(i).zfill(2) for i in range(24)], width=5).grid(row=1, column=1)
        
        tk.Label(top, text='分:').grid(row=1, column=2, padx=5)
        min_var = tk.StringVar(value=str(now.minute).zfill(2))
        ttk.Combobox(top, textvariable=min_var, values=[str(i).zfill(2) for i in range(60)], width=5).grid(row=1, column=3)
        
        confirm_btn = tk.Button(top, text='确定', 
            command=lambda: self.set_time(
                datetime.datetime.combine(cal.get_date(), 
                datetime.time(int(hour_var.get()), int(min_var.get())))))
        confirm_btn.grid(row=2, column=0, columnspan=4, pady=10, sticky='ew')
        
        confirm_btn.pack(pady=5)

    def set_time(self, selected_time):
        if isinstance(selected_time, datetime.date):
            selected_time = datetime.datetime.combine(selected_time, datetime.time())
        # 关闭时间选择窗口
        selected_time = selected_time.replace(second=0, microsecond=0)
        self.time_entry.config(state='normal')
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, selected_time.strftime('%Y-%m-%d %H:%M'))
        self.time_entry.config(state='readonly')
        # 销毁时间选择窗口
        if self.time_entry.winfo_toplevel().winfo_children()[1]:
            self.time_entry.winfo_toplevel().winfo_children()[1].destroy()

    def parse_selected_time(self, time_str):
        if '秒' in time_str:
            return int(time_str.replace('秒', ''))
        return int(time_str.replace('分钟', '')) * 60

    def start_countdown(self, seconds):
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        self.show_fullscreen_alert(end_time)
        
    def show_fullscreen_alert(self, end_time):
        self.last_color_change = datetime.datetime.now()
        self.alert_window = tk.Toplevel(self.root)
        self.alert_window.attributes('-fullscreen', True)
        
        # 创建一个主框架，用于居中内容
        main_frame = tk.Frame(self.alert_window)
        # 使用place布局实现精准居中
        main_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # 直接显示公告内容
        announcement_label = tk.Label(main_frame, text=self.announcement_var.get(), font=('Arial', 36, 'bold'), fg='#FF4500')
        # 垂直排列公告和倒计时
        announcement_label.pack(pady=(0, 30))
        
        # 倒计时显示
        time_label = tk.Label(main_frame, text='剩余时间:', font=('Arial', 72, 'bold'))
        time_label.pack(pady=(0, 30))
        
        self.color_index = 0
        self.colors = ['#FFB6C1', '#87CEFA', '#98FB98', '#DDA0DD', '#FFD700']
        
        # 添加关闭按钮
        btn_frame = tk.Frame(main_frame)
        shutdown_btn = tk.Button(btn_frame, text='立即关机', font=('Arial', 24), bg='red',
                              command=self.shutdown_now)
        cancel_btn = tk.Button(btn_frame, text='取消关机', font=('Arial', 24), bg='green',
                             command=self.cancel_shutdown)
        shutdown_btn.pack(side='left', padx=20)
        cancel_btn.pack(side='right', padx=20)
        btn_frame.pack(pady=50)  # 调整按钮的垂直间距
        
        self.update_alert_time(time_label, end_time)
        
    def update_announcement_text(self):
        self.canvas.itemconfig(self.announcement_text, text=self.announcement_var.get())
    
    def start_scroll_animation(self):
        def scroll_text():
            self.canvas.move(self.announcement_text, -self.scroll_speed, 0)
            pos = self.canvas.coords(self.announcement_text)
            if pos[0] < -800:  # 当文字完全滚出画面时重置位置
                self.canvas.coords(self.announcement_text, 1000, 40)
            self.alert_window.after(50, scroll_text)
        scroll_text()

    def update_alert_time(self, label, end_time):
        remaining = end_time - datetime.datetime.now()
        if remaining.total_seconds() <= 60:
            announcement_text = "电脑还有一分钟就要关机了 请你保存好重要的文件哦\n今天的工作就到这了 您辛苦了~\n明天继续加油努力哦！！！"
            self.announcement_var.set(announcement_text)  # 设置公告内容
        
        if remaining.total_seconds() <= 0:
            label.config(text='关机时间到！')
            self.shutdown_now()
            self.alert_window.destroy()
            return
        
        mins, secs = divmod(int(remaining.total_seconds()), 60)
        hours, mins = divmod(mins, 60)
        label.config(text=f'{hours:02d}:{mins:02d}:{secs:02d}')
        label.after(1000, lambda: self.update_alert_time(label, end_time))
        if (datetime.datetime.now() - self.last_color_change).seconds >= 5:
            # Cycle the fullscreen warning window's background color.
            self.alert_window.config(bg=self.colors[self.color_index % len(self.colors)])
            self.color_index += 1
            self.last_color_change = datetime.datetime.now()

    def run(self):
        self.root.mainloop()

    def shutdown_now(self):
        import os
        os.system('shutdown /s /t 1')

    def cancel_shutdown(self):
        import os
        os.system('shutdown /a')
        self.alert_window.destroy()

if __name__ == '__main__':
    app = ShutdownApp()
    app.run()