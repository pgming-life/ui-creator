<template>
<div>
<pre>
"""Tkinter.pyw"""

import tkinter as tk
import tkinter.ttk
import tkinter.font as f
import math

class GuiApplication(tk.Frame):
    def __init__(self, master=None):
        # window size
        window_width = {{ mainSize[0] }}
        window_height = {{ mainSize[1] - 25 }}
</pre>
<pre
  v-for="(rate, num) in labelStack"
  :key="`first-${num}`"
>
        # label{{ num + 1 }}
        self.label{{ num + 1 }}_height = {{ rate.labelHeight }}
        self.label{{ num + 1 }}_x = {{ rate.labelLeft }}
        self.label{{ num + 1 }}_y = {{ rate.labelTop }}
</pre>
<pre
  v-for="(rate, num) in inputboxStack"
  :key="`first-${num}`"
>
        # inputbox{{ num + 1 }}
        self.inputbox{{ num + 1 }}_width = {{ rate.inputboxWidth }}
        self.inputbox{{ num + 1 }}_height = {{ rate.inputboxHeight }}
        self.inputbox{{ num + 1 }}_x = {{ rate.inputboxLeft }}
        self.inputbox{{ num + 1 }}_y = {{ rate.inputboxTop }}
</pre>
<pre
  v-for="(rate, num) in listboxStack"
  :key="`first-${num}`"
>
        # listbox{{ num + 1 }}
        self.listbox{{ num + 1 }}_width = {{ rate.listboxWidth }}
        self.listbox{{ num + 1 }}_height = {{ rate.listboxHeight }}
        self.listbox{{ num + 1 }}_x = {{ rate.listboxLeft }}
        self.listbox{{ num + 1 }}_y = {{ rate.listboxTop }}
</pre>
<pre
  v-for="(rate, num) in buttonStack"
  :key="`first-${num}`"
>
        # button{{ num + 1 }}
        self.button{{ num + 1 }}_width = {{ rate.buttonWidth }}
        self.button{{ num + 1 }}_height = {{ rate.buttonHeight }}
        self.button{{ num + 1 }}_x = {{ rate.buttonLeft }}
        self.button{{ num + 1 }}_y = {{ rate.buttonTop }}
</pre>
<pre>
        super().__init__(
            master,
            width=window_width,
            height=window_height,
            )
        self.master = master
        self.master.title("Tkinter")
        self.master.minsize(
            window_width,
            window_height,
            )
        self.pack()
</pre>
<pre
  v-if="showFunc"
>
        self.create_widgets()


    def create_widgets(self):
<pre
  v-for="(rate, num) in labelStack"
  :key="`second-${num}`"
>
        # create label{{ num + 1 }}
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
        # create inputbox{{ num + 1 }}
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
        # create listbox{{ num + 1 }}
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
        # create button{{ num + 1 }}
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
</pre>
<pre>
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
  computed: {
    showFunc: function() {
      if(
        this.labelStack.length == 0 &&
        this.inputboxStack.length == 0 &&
        this.listboxStack.length == 0 &&
        this.buttonStack.length == 0
      ) {
        return false
      } else {
        return true
      }
    },
  },
}
</script>

<style scoped>
pre {
  text-align: left;
  font-family: sans-serif;
}
</style>
