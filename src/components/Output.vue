<template>
<div>
<pre>
"""Tkinter.pyw"""

import tkinter as tk
import tkinter.ttk
import tkinter.font as f
import math

# GUIアプリケーション
class GuiApplication(tk.Frame):
    # コンストラクタ
    def __init__(self, master=None):
        # ウィンドウサイズ
        window_width = {{ mainSize[0] }}
        window_height = {{ mainSize[1] }}
</pre>
<pre
  v-for="(rate, num) in labelStack"
  :key="`first-${num}`"
>
        # ラベル{{ num + 1 }}
        self.label{{ num + 1 }}_height = {{ rate.labelHeight }}
        self.label{{ num + 1 }}_x = {{ rate.labelLeft }}
        self.label{{ num + 1 }}_y = {{ rate.labelTop }}
</pre>
<pre
  v-for="(rate, num) in inputboxStack"
  :key="`first-${num}`"
>
        # インプットボックス{{ num + 1 }}
        self.inputbox{{ num + 1 }}_width = {{ rate.inputboxWidth }}
        self.inputbox{{ num + 1 }}_height = {{ rate.inputboxHeight }}
        self.inputbox{{ num + 1 }}_x = {{ rate.inputboxLeft }}
        self.inputbox{{ num + 1 }}_y = {{ rate.inputboxTop }}
</pre>
<pre
  v-for="(rate, num) in listboxStack"
  :key="`first-${num}`"
>
        # リストボックス{{ num + 1 }}
        self.listbox{{ num + 1 }}_width = {{ rate.listboxWidth }}
        self.listbox{{ num + 1 }}_height = {{ rate.listboxHeight }}
        self.listbox{{ num + 1 }}_x = {{ rate.listboxLeft }}
        self.listbox{{ num + 1 }}_y = {{ rate.listboxTop }}
</pre>
<pre
  v-for="(rate, num) in buttonStack"
  :key="`first-${num}`"
>
        # ボタン{{ num + 1 }}
        self.button{{ num + 1 }}_width = {{ rate.buttonWidth }}
        self.button{{ num + 1 }}_height = {{ rate.buttonHeight }}
        self.button{{ num + 1 }}_x = {{ rate.buttonLeft }}
        self.button{{ num + 1 }}_y = {{ rate.buttonTop }}
</pre>
<pre>
        # Frameクラスを継承
        super().__init__(
            master,
            width=window_width,
            height=window_height,
            )
        
        # 初期値代入
        self.master = master
        self.master.title("Tkinter")
        self.master.minsize(
            window_width,
            window_height,
            )
        self.pack()
</pre>
<pre
  v-for="(rate, num) in labelStack"
  :key="`second-${num}`"
>
        # ラベル{{ num + 1 }}作成
        self.label{{ num + 1 }}_font = f.Font(
            family=u'MSゴシック',
            size=math.floor(self.label{{ num + 1 }}_height*0.5),
            )
        self.label{{ num + 1 }} = tk.Label(
            text="Label{{ num + 1 }}",
            )
        self.label{{ num + 1 }}.configure(
            font=self.label{{ num + 1 }}_font,
            )
        self.label{{ num + 1 }}.place(
            x=self.label{{ num + 1 }}_x,
            y=self.label{{ num + 1 }}_y,
            )
</pre>
<pre
  v-for="(rate, num) in inputboxStack"
  :key="`second-${num}`"
>
        # インプットボックス{{ num + 1 }}作成
        self.inputbox{{ num + 1 }}_font = f.Font(
            family=u'MSゴシック',
            size=math.floor(self.inputbox{{ num + 1 }}_height*0.5),
            )
        self.inputbox{{ num + 1 }} = tk.Entry(self)
        self.inputbox{{ num + 1 }}.configure(
            font=self.inputbox{{ num + 1 }}_font,
            )
        self.inputbox{{ num + 1 }}.place(
            width=self.inputbox{{ num + 1 }}_width,
            height=self.inputbox{{ num + 1 }}_height,
            x=self.inputbox{{ num + 1 }}_x,
            y=self.inputbox{{ num + 1 }}_y,
            )
</pre>
<pre
  v-for="(rate, num) in listboxStack"
  :key="`second-${num}`"
>
        # リストボックス{{ num + 1 }}作成
        self.listbox{{ num + 1 }} = tk.Listbox(self)
        self.listbox{{ num + 1 }}.place(
            width=self.listbox{{ num + 1 }}_width,
            height=self.listbox{{ num + 1 }}_height,
            x=self.listbox{{ num + 1 }}_x,
            y=self.listbox{{ num + 1 }}_y,
            )
        data = ["ListBox{{ num + 1 }}", "...", "...", "..."]
        for i in data:
            self.listbox{{ num + 1 }}.insert(
                tk.END,
                "{}\n".format(i)
                )
</pre>
<pre
  v-for="(rate, num) in buttonStack"
  :key="`second-${num}`"
>
        # ボタン{{ num + 1 }}作成
        self.button{{ num + 1 }} = tk.ttk.Button(
            self,
            text="Button{{ num + 1 }}",
            )
        self.button{{ num + 1 }}.place(
            width=self.button{{ num + 1 }}_width,
            height=self.button{{ num + 1 }}_height,
            x=self.button{{ num + 1 }}_x,
            y=self.button{{ num + 1 }}_y,
            )
</pre>
<pre>
# アプリケーション起動
window = tk.Tk()
app = GuiApplication(master=window)
app.mainloop()
</pre>
</div>
</template>

<script>
export default {
  name: "Output",
  props: [
    'mainSize',
    'labelStack',
    'inputboxStack',
    'listboxStack',
    'buttonStack',
  ],
}
</script>

<style scoped>
pre {
  text-align: left;
  font-family: sans-serif;
}
</style>
