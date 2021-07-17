<template>
  <div class="text-center">
    <v-row>
      <v-col>
        <v-btn
          block
          :loading="output"
          :disabled="output"
          color="grey lighten-5"
          class="ma-2 orange--text"
          @click="loader='output'; showDisplay(); outputter();"
        >
          OUTPUT
          <v-icon>mdi-book-arrow-down</v-icon>
          <template v-slot:loader>
            <span class="custom-loader">
              <v-icon light>
                mdi-cached
              </v-icon>
            </span>
          </template>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn
          block
          :loading="download"
          :disabled="download"
          color="grey lighten-5"
          class="ma-2 orange--text"
          @click="loader='download'; downloader();"
        >
          DOWNLOAD<v-icon>mdi-cloud-download</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-col>
      <v-sheet
        min-height="90vh"
        rounded="md"
        v-if="show"
      >
        <Output
          :mainSize="[cacheMainSize[0], cacheMainSize[1]]"
          :labelStack="cacheLabelStack"
          :inputboxStack="cacheInputBoxStack"
          :listboxStack="cacheListBoxStack"
          :buttonStack="cacheButtonStack"
        />
      </v-sheet>
    </v-col>
  </div>
</template>

<script>
import Output from './Output';

export default {
  name: "Loader",
  components: {
    Output,
  },
  props: [
    'show',
    'mainSize',
    'labelStack',
    'inputboxStack',
    'listboxStack',
    'buttonStack',
  ],
  data() {
    return {
      loader: null,
      output: false,
      download: false,
      pyw: "",
      cacheMainSize: [0, 0],
      cacheLabelStack: [],
      cacheInputBoxStack: [],
      cacheListBoxStack: [],
      cacheButtonStack: [],
    }
  },
  watch: {
    loader() {
      const t = this.loader;
      this[t] = !this[t];
      setTimeout(() => (this[t] = false), 1000);
      this.loader = null;
    },
  },
  methods: {
    showDisplay: function() {
      this.$emit("showDisplay");
    },
    outputter: function() {
      this.cacheMainSize = this.mainSize;
      this.cacheLabelStack = this.labelStack;
      this.cacheInputBoxStack = this.inputboxStack;
      this.cacheListBoxStack = this.listboxStack;
      this.cacheButtonStack = this.buttonStack;
    },
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
    downloader: function() {
      this.pyw = '\ufeff' + '"""Tkinter.pyw"""\r\n';
      this.pyw += '\r\n';
      this.pyw += 'import tkinter as tk\r\n';
      this.pyw += 'import tkinter.ttk\r\n';
      this.pyw += 'import tkinter.font as f\r\n';
      this.pyw += 'import math\r\n';
      this.pyw += '\r\n';
      this.pyw += 'class GuiApplication(tk.Frame):\r\n';
      this.pyw += '    def __init__(self, master=None):\r\n';
      this.pyw += '        # window size\r\n';
      this.pyw += '        window_width = ' + this.mainSize[0] + '\r\n';
      this.pyw += '        window_height = ' + (this.mainSize[1] - 25) + '\r\n';
      this.pyw += '        \r\n';
      this.labelStack.forEach((rate, num) => {
        this.pyw += '        # label' + (num + 1) + '\r\n';
        this.pyw += '        self.label' + (num + 1) + '_height = ' + rate.labelHeight + '\r\n';
        this.pyw += '        self.label' + (num + 1) + '_x = ' + rate.labelLeft + '\r\n';
        this.pyw += '        self.label' + (num + 1) + '_y = ' + rate.labelTop + '\r\n';
        this.pyw += '        \r\n';
      });
      this.inputboxStack.forEach((rate, num) => {
        this.pyw += '        # inputbox' + (num + 1) + '\r\n';
        this.pyw += '        self.inputbox' + (num + 1) + '_width = ' + rate.inputboxWidth + '\r\n';
        this.pyw += '        self.inputbox' + (num + 1) + '_height = ' + rate.inputboxHeight + '\r\n';
        this.pyw += '        self.inputbox' + (num + 1) + '_x = ' + rate.inputboxLeft + '\r\n';
        this.pyw += '        self.inputbox' + (num + 1) + '_y = ' + rate.inputboxTop + '\r\n';
        this.pyw += '        \r\n';
      });
      this.listboxStack.forEach((rate, num) => {
        this.pyw += '        # listbox' + (num + 1) + '\r\n';
        this.pyw += '        self.listbox' + (num + 1) + '_width = ' + rate.listboxWidth + '\r\n';
        this.pyw += '        self.listbox' + (num + 1) + '_height = ' + rate.listboxHeight + '\r\n';
        this.pyw += '        self.listbox' + (num + 1) + '_x = ' + rate.listboxLeft + '\r\n';
        this.pyw += '        self.listbox' + (num + 1) + '_y = ' + rate.listboxTop + '\r\n';
        this.pyw += '        \r\n';
      });
      this.buttonStack.forEach((rate, num) => {
        this.pyw += '        # button' + (num + 1) + '\r\n';
        this.pyw += '        self.button' + (num + 1) + '_width = ' + rate.buttonWidth + '\r\n';
        this.pyw += '        self.button' + (num + 1) + '_height = ' + rate.buttonHeight + '\r\n';
        this.pyw += '        self.button' + (num + 1) + '_x = ' + rate.buttonLeft + '\r\n';
        this.pyw += '        self.button' + (num + 1) + '_y = ' + rate.buttonTop + '\r\n';
        this.pyw += '        \r\n';
      });
      this.pyw += '        super().__init__(\r\n';
      this.pyw += '            master,\r\n';
      this.pyw += '            width=window_width,\r\n';
      this.pyw += '            height=window_height,\r\n';
      this.pyw += '            )\r\n';
      this.pyw += '        self.master = master\r\n';
      this.pyw += '        self.master.title("Tkinter")\r\n';
      this.pyw += '        self.master.minsize(\r\n';
      this.pyw += '            window_width,\r\n';
      this.pyw += '            window_height,\r\n';
      this.pyw += '            )\r\n';
      this.pyw += '        self.pack()\r\n';
      this.pyw += '        \r\n';
      if(this.showFunc()) {
        this.pyw += '        self.create_widgets()\r\n';
        this.pyw += '        \r\n';
        this.pyw += '        \r\n';
        this.pyw += '    def create_widgets(self):\r\n';
      }
      this.labelStack.forEach((rate, num) => {
        this.pyw += '        # create label' + (num + 1) + '\r\n';
        this.pyw += '        self.label' + (num + 1) + '_font = f.Font(\r\n';
        this.pyw += "            family=u'MSゴシック',\r\n";
        this.pyw += '            size=math.floor(self.label' + (num + 1) + '_height*0.5),\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        self.label' + (num + 1) + ' = tk.Label(\r\n';
        this.pyw += '            text="Label' + (num + 1) + '",\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        self.label' + (num + 1) + '.configure(\r\n';
        this.pyw += '            font=self.label' + (num + 1) + '_font,\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        self.label' + (num + 1) + '.place(\r\n';
        this.pyw += '            x=self.label' + (num + 1) + '_x,\r\n';
        this.pyw += '            y=self.label' + (num + 1) + '_y,\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        \r\n';
      });
      this.inputboxStack.forEach((rate, num) => {
        this.pyw += '        # create inputbox' + (num + 1) + '\r\n';
        this.pyw += '        self.inputbox' + (num + 1) + '_font = f.Font(\r\n';
        this.pyw += "            family=u'MSゴシック',\r\n";
        this.pyw += '            size=math.floor(self.inputbox' + (num + 1) + '_height*0.5),\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        self.inputbox' + (num + 1) + ' = tk.Entry(self)\r\n';
        this.pyw += '        self.inputbox' + (num + 1) + '.configure(\r\n';
        this.pyw += '            font=self.inputbox' + (num + 1) + '_font,\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        self.inputbox' + (num + 1) + '.place(\r\n';
        this.pyw += '            width=self.inputbox' + (num + 1) + '_width,\r\n';
        this.pyw += '            height=self.inputbox' + (num + 1) + '_height,\r\n';
        this.pyw += '            x=self.inputbox' + (num + 1) + '_x,\r\n';
        this.pyw += '            y=self.inputbox' + (num + 1) + '_y,\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        \r\n';
      });
      this.listboxStack.forEach((rate, num) => {
        this.pyw += '        # create listbox' + (num + 1) + '\r\n';
        this.pyw += '        self.listbox' + (num + 1) + ' = tk.Listbox(self)\r\n';
        this.pyw += '        self.listbox' + (num + 1) + '.place(\r\n';
        this.pyw += '            width=self.listbox' + (num + 1) + '_width,\r\n';
        this.pyw += '            height=self.listbox' + (num + 1) + '_height,\r\n';
        this.pyw += '            x=self.listbox' + (num + 1) + '_x,\r\n';
        this.pyw += '            y=self.listbox' + (num + 1) + '_y,\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        data = ["ListBox' + (num + 1) + '", "...", "...", "..."]\r\n';
        this.pyw += '        for i in data:\r\n';
        this.pyw += '            self.listbox' + (num + 1) + '.insert(\r\n';
        this.pyw += '                tk.END,\r\n';
        this.pyw += '                "{}\\n".format(i)\r\n';
        this.pyw += '                )\r\n';
        this.pyw += '        \r\n';
      });
      this.buttonStack.forEach((rate, num) => {
        this.pyw += '        # create button' + (num + 1) + '\r\n';
        this.pyw += '        self.button' + (num + 1) + ' = tk.ttk.Button(\r\n';
        this.pyw += '            self,\r\n';
        this.pyw += '            text="Button' + (num + 1) + '",\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        self.button' + (num + 1) + '.place(\r\n';
        this.pyw += '            width=self.button' + (num + 1) + '_width,\r\n';
        this.pyw += '            height=self.button' + (num + 1) + '_height,\r\n';
        this.pyw += '            x=self.button' + (num + 1) + '_x,\r\n';
        this.pyw += '            y=self.button' + (num + 1) + '_y,\r\n';
        this.pyw += '            )\r\n';
        this.pyw += '        \r\n';
      });
      this.pyw += 'window = tk.Tk()\r\n';
      this.pyw += 'app = GuiApplication(master=window)\r\n';
      this.pyw += 'app.mainloop()\r\n';
      
      // download settings
      let blob = new Blob([this.pyw], { type: '.pyw' });
      let link = document.createElement('a');
      link.href = window.URL.createObjectURL(blob);
      link.download = 'Tkinter.pyw';
      link.click();
    },
  },
};
</script>

<style>
.custom-loader {
  animation: loader 1s infinite;
  display: flex;
}
@-moz-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-o-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
