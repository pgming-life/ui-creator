<template>
  <v-app>
    <v-main class="grey lighten-3">
      <v-container>
        <v-col>
          <v-row>
            <v-col>
              <v-select
                label="テンプレート選択"
                v-model="template"
                :items="items.templates"
                item-value="id"
                item-text="name"
              >
              </v-select>
            </v-col>
            <v-col v-if="selectedTemplate">
              <TemplateAccess
                @clearStack="clear"
                @catchMessages="apply"
              />
              ※全てリセットして適用します。
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-select
                label="ウィジェット選択"
                v-model="widget"
                :items="items.widgets"
                item-value="id"
                item-text="name"
              >
              </v-select>
            </v-col>
            <v-col>
              <v-btn
                v-if="selectedWidget"
                fab
                elevation="7"
                x-large
                color="#008099"
                @click="append(selectedWidget.id)"
              >
                <span style="color:white;">追加</span>
              </v-btn>
            </v-col>
            <v-col>
              <v-btn
                elevation="7"
                x-large
                color="orange"
                @click="clear"
              >
                <span style="color:white;">
                  リセット
                  <v-icon>mdi-cached</v-icon>
                </span>
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
        <v-col>
          <v-row>
            <v-col>
              <div class="container table-block">
                <div class="table-row">
                  <div>
                    <h4>Window:</h4>
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="mainWidth">:width
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="mainHeight">:height
                  </div>
                </div>
              </div>
            </v-col>
            <!-- add dynamic tags (components) -->
            <v-col
              v-for="(rate, num) in labelStack"
              :key="num"
            >
              <div class="container table-block">
                <div class="table-row">
                  <div>
                    <v-btn
                      block
                      x-small
                      elevation="2"
                      color="slategray"
                      @click="deleteLabel(num)"
                    >
                      x
                    </v-btn>
                  </div>
                  <div>
                    <h4>Label{{ num + 1 }}:</h4>
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.labelHeight">:fontsize
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.labelLeft">:x
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.labelTop">:y
                  </div>
                </div>
              </div>
            </v-col>
            <v-col
              v-for="(rate, num) in inputboxStack"
              :key="num"
            >
              <div class="container table-block">
                <div class="table-row">
                  <div>
                    <v-btn
                      block
                      x-small
                      elevation="2"
                      color="slategray"
                      @click="deleteInputBox(num)"
                    >
                      x
                    </v-btn>
                  </div>
                  <div>
                    <h4>InputBox{{ num + 1 }}:</h4>
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.inputboxWidth">:width
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.inputboxHeight">:height
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.inputboxLeft">:x
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.inputboxTop">:y
                  </div>
                </div>
              </div>
            </v-col>
            <v-col
              v-for="(rate, num) in listboxStack"
              :key="num"
            >
              <div class="container table-block">
                <div class="table-row">
                  <div>
                    <v-btn
                      block
                      x-small
                      elevation="2"
                      color="slategray"
                      @click="deleteListBox(num)"
                    >
                      x
                    </v-btn>
                  </div>
                  <div>
                    <h4>ListBox{{ num + 1 }}:</h4>
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.listboxWidth">:width
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.listboxHeight">:height
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.listboxLeft">:x
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.listboxTop">:y
                  </div>
                </div>
              </div>
            </v-col>
            <v-col
              v-for="(rate, num) in buttonStack"
              :key="num"
            >
              <div class="container table-block">
                <div class="table-row">
                  <div>
                    <v-btn
                      block
                      x-small
                      elevation="2"
                      color="slategray"
                      @click="deleteButton(num)"
                    >
                      x
                    </v-btn>
                  </div>
                  <div>
                    <h4>Button{{ num + 1 }}:</h4>
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.buttonWidth">:width
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.buttonHeight">:height
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.buttonLeft">:x
                  </div>
                  <div class="table-cell">
                    <input class="table-input" type="number" v-model.number="rate.buttonTop">:y
                  </div>
                </div>
              </div>
            </v-col>
          </v-row>
        </v-col>
      </v-container>
      <v-container>
        <v-col>
          <v-sheet
            min-height="90vh"
            rounded="md"
          >
            <MainWindow
              class="mainresizable"
              ref="mainresizableComponent"
              :dragSelector="mainDragSelector"
              :fit-parent="mainFit"
              :min-width="mainMinW | checkEmpty"
              :min-height="mainMinH | checkEmpty"
              :width="mainWidth"
              :height="mainHeight"
              :left="mainLeft"
              :top="mainTop"
              @mount="mainHandler"
              @resize:move="mainHandler"
              @resize:start="mainHandler"
              @resize:end="mainHandler"
              @drag:move="mainHandler"
              @drag:start="mainHandler"
              @drag:end="mainHandler"
            >
              <div class="block">
                <div class="drag-container-titlebar">Tkinter</div>
                <div class="table-container">
                  <!-- add dynamic tags (components) -->
                  <Label
                    v-for="(rate, num) in labelStack"
                    :key="num"
                    class="labelresizable"
                    ref="labelresizableComponent"
                    :dragSelector="rate.labelDragSelector"
                    :fit-parent="rate.labelFit"
                    :max-width="rate.labelMaxW | checkEmpty"
                    :min-width="rate.labelMinW | checkEmpty"
                    :min-height="rate.labelMinH | checkEmpty"
                    :width="rate.labelWidth"
                    :height="rate.labelHeight"
                    :left="rate.labelLeft"
                    :top="rate.labelTop"
                    @mount="labelHandler($event, num)"
                    @resize:move="labelHandler($event, num)"
                    @resize:start="labelHandler($event, num)"
                    @resize:end="labelHandler($event, num)"
                    @drag:move="labelHandler($event, num)"
                    @drag:start="labelHandler($event, num)"
                    @drag:end="labelHandler($event, num)"
                  >
                    <div class="drag-container-label" :style="{'font-size': rate.labelHeight / 1.6 + 'px'}">Label{{ num + 1 }}</div>
                  </Label>
                  <InputBox
                    v-for="(rate, num) in inputboxStack"
                    :key="num"
                    class="inputboxresizable"
                    ref="inputboxresizableComponent"
                    :dragSelector="rate.inputboxDragSelector"
                    :fit-parent="rate.inputboxFit"
                    :min-width="rate.inputboxMinW | checkEmpty"
                    :min-height="rate.inputboxMinH | checkEmpty"
                    :width="rate.inputboxWidth"
                    :height="rate.inputboxHeight"
                    :left="rate.inputboxLeft"
                    :top="rate.inputboxTop"
                    @mount="inputboxHandler($event, num)"
                    @resize:move="inputboxHandler($event, num)"
                    @resize:start="inputboxHandler($event, num)"
                    @resize:end="inputboxHandler($event, num)"
                    @drag:move="inputboxHandler($event, num)"
                    @drag:start="inputboxHandler($event, num)"
                    @drag:end="inputboxHandler($event, num)"
                  >
                    <div class="drag-container-inputbox" :style="{'font-size': rate.inputboxHeight / 1.6 + 'px'}">InputBox{{ num + 1 }}</div>
                  </InputBox>
                  <ListBox
                    v-for="(rate, num) in listboxStack"
                    :key="num"
                    class="listboxresizable"
                    ref="listboxresizableComponent"
                    :dragSelector="rate.listboxDragSelector"
                    :fit-parent="rate.listboxFit"
                    :min-width="rate.listboxMinW | checkEmpty"
                    :min-height="rate.listboxMinH | checkEmpty"
                    :width="rate.listboxWidth"
                    :height="rate.listboxHeight"
                    :left="rate.listboxLeft"
                    :top="rate.listboxTop"
                    @mount="listboxHandler($event, num)"
                    @resize:move="listboxHandler($event, num)"
                    @resize:start="listboxHandler($event, num)"
                    @resize:end="listboxHandler($event, num)"
                    @drag:move="listboxHandler($event, num)"
                    @drag:start="listboxHandler($event, num)"
                    @drag:end="listboxHandler($event, num)"
                  >
                    <div class="drag-container-listbox">ListBox{{ num + 1 }}</div>
                  </ListBox>
                  <Button
                    v-for="(rate, num) in buttonStack"
                    :key="num"
                    class="buttonresizable"
                    ref="buttonresizableComponent"
                    :dragSelector="rate.buttonDragSelector"
                    :fit-parent="rate.buttonFit"
                    :min-width="rate.buttonMinW | checkEmpty"
                    :min-height="rate.buttonMinH | checkEmpty"
                    :width="rate.buttonWidth"
                    :height="rate.buttonHeight"
                    :left="rate.buttonLeft"
                    :top="rate.buttonTop"
                    @mount="buttonHandler($event, num)"
                    @resize:move="buttonHandler($event, num)"
                    @resize:start="buttonHandler($event, num)"
                    @resize:end="buttonHandler($event, num)"
                    @drag:move="buttonHandler($event, num)"
                    @drag:start="buttonHandler($event, num)"
                    @drag:end="buttonHandler($event, num)"
                  >
                    <div class="drag-container-button">Button{{ num + 1 }}</div>
                  </Button>
                </div>
              </div>
            </MainWindow>
          </v-sheet>
        </v-col>
        <Loader
          @showDisplay="showOn"
          :show="show"
          :mainSize="[mainWidth, mainHeight]"
          :labelStack="labelStack"
          :inputboxStack="inputboxStack"
          :listboxStack="listboxStack"
          :buttonStack="buttonStack"
        />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Loader from './Loader';
import TemplateAccess from './TemplateAccess';
import MainWindow from './widgets/MainWindow';
import Label from './widgets/Label';
import InputBox from './widgets/InputBox';
import ListBox from './widgets/ListBox';
import Button from './widgets/Button';
// add widget components

export default {
  name: 'WorkSpace',
  components: {
    Loader,
    TemplateAccess,
    MainWindow,
    Label,
    InputBox,
    ListBox,
    Button,
    // add widget components
  },
  data() {
    return {
      show: false,
      labelStack: [],
      inputboxStack: [],
      listboxStack: [],
      buttonStack: [],
      template: "",
      widget: "",
      items: {
        templates: [
          { id: 0, name: 'テンプレート1'},
          { id: 1, name: 'テンプレート2'},
          { id: 2, name: 'テンプレート3'},
        ],
        widgets: [
          { id: 0, name: 'ラベル(tkinter.Label)'},
          { id: 1, name: 'インプットボックス(tkinter.Entry)'},
          { id: 2, name: 'リストボックス(tkinter.Listbox)'},
          { id: 3, name: 'ボタン(tkinter.Button)'},
        ],
      },
      mainDragSelector: ".drag-container-titlebar",
      mainWidth: 300,
      mainHeight: 300,
      mainMinW: 150,
      mainMinH: 150,
      mainLeft: 0,
      mainTop: 0,
      mainFit: true,
      labelDragSelector: ".drag-container-label",
      labelWidth: 80,
      labelHeight: 25,
      labelMaxW: 80,
      labelMinW: 80,
      labelMinH: 25,
      labelLeft: 0,
      labelTop: 0,
      labelFit: false,
      inputboxDragSelector: ".drag-container-inputbox",
      inputboxWidth: 80,
      inputboxHeight: 20,
      inputboxMinW: 80,
      inputboxMinH: 25,
      inputboxLeft: 0,
      inputboxTop: 0,
      inputboxFit: false,
      listboxDragSelector: ".drag-container-listbox",
      listboxWidth: 80,
      listboxHeight: 20,
      listboxMinW: 80,
      listboxMinH: 25,
      listboxLeft: 0,
      listboxTop: 0,
      listboxFit: false,
      buttonDragSelector: ".drag-container-button",
      buttonWidth: 80,
      buttonHeight: 20,
      buttonMinW: 80,
      buttonMinH: 25,
      buttonLeft: 0,
      buttonTop: 0,
      buttonFit: false,
    };
  },
  computed: {
    selectedTemplate: function() {
      return this.items.templates.find((i) => i.id === this.template)
    },
    selectedWidget: function() {
      return this.items.widgets.find((i) => i.id === this.widget)
    },
  },
  methods: {
    showOn: function() {
      this.show = true;
    },
    showOff: function() {
      this.show = false;
    },
    mainHandler(event) {
      this.showOff();
      this.mainWidth = Math.floor(event.width);
      this.mainHeight = Math.floor(event.height);
    },
    labelHandler(event, num) {
      this.showOff();
      this.labelStack[num].labelHeight = 	Math.floor(event.height);
      this.labelStack[num].labelLeft = Math.floor(event.left);
      this.labelStack[num].labelTop = Math.floor(event.top);
    },
    inputboxHandler(event, num) {
      this.showOff();
      this.inputboxStack[num].inputboxWidth = Math.floor(event.width);
      this.inputboxStack[num].inputboxHeight = Math.floor(event.height);
      this.inputboxStack[num].inputboxLeft = Math.floor(event.left);
      this.inputboxStack[num].inputboxTop = Math.floor(event.top);
    },
    listboxHandler(event, num) {
      this.showOff();
      this.listboxStack[num].listboxWidth = Math.floor(event.width);
      this.listboxStack[num].listboxHeight = Math.floor(event.height);
      this.listboxStack[num].listboxLeft = Math.floor(event.left);
      this.listboxStack[num].listboxTop = Math.floor(event.top);
    },
    buttonHandler(event, num) {
      this.showOff();
      this.buttonStack[num].buttonWidth = Math.floor(event.width);
      this.buttonStack[num].buttonHeight = Math.floor(event.height);
      this.buttonStack[num].buttonLeft = Math.floor(event.left);
      this.buttonStack[num].buttonTop = Math.floor(event.top);
    },
    apply: function(messages) {
      this.showOff();
      messages.forEach(rate => {
        if(rate.name_key == this.selectedTemplate.name) {
          if(rate.stack_key == "mainSize") {
            this.mainWidth = rate.width;
            this.mainHeight = rate.height;
          }
          if(rate.stack_key == "labelStack") {
            this.labelStack.push({
              labelDragSelector: this.labelDragSelector,
              labelWidth: rate.width,
              labelHeight: rate.height,
              labelMinW: this.labelMinW,
              labelMinH: this.labelMinH,
              labelLeft: rate.left,
              labelTop: rate.top,
              labelFit: this.labelFit,
            });
          }
          if(rate.stack_key == "inputboxStack") {
            this.inputboxStack.push({
              inputboxDragSelector: this.inputboxDragSelector,
              inputboxWidth: rate.width,
              inputboxHeight: rate.height,
              inputboxMinW: this.inputboxMinW,
              inputboxMinH: this.inputboxMinH,
              inputboxLeft: rate.left,
              inputboxTop: rate.top,
              inputboxFit: this.inputboxFit,
            });
          }
          if(rate.stack_key == "listboxStack") {
            this.listboxStack.push({
              listboxDragSelector: this.listboxDragSelector,
              listboxWidth: rate.width,
              listboxHeight: rate.height,
              listboxMinW: this.listboxMinW,
              listboxMinH: this.listboxMinH,
              listboxLeft: rate.left,
              listboxTop: rate.top,
              listboxFit: this.listboxFit,
            });
          }
          if(rate.stack_key == "buttonStack") {
            this.buttonStack.push({
              buttonDragSelector: this.buttonDragSelector,
              buttonWidth: rate.width,
              buttonHeight: rate.height,
              buttonMinW: this.buttonMinW,
              buttonMinH: this.buttonMinH,
              buttonLeft: rate.left,
              buttonTop: rate.top,
              buttonFit: this.buttonFit,
            });
          }
        }
      });
    },
    append: function(id) {
      this.showOff();
      if(id == 0) {
        this.labelStack.push({
          labelDragSelector: this.labelDragSelector,
          labelWidth: this.labelWidth,
          labelHeight: this.labelHeight,
          labelMinW: this.labelMinW,
          labelMinH: this.labelMinH,
          labelLeft: this.labelLeft,
          labelTop: this.labelTop,
          labelFit: this.labelFit,
        });
      }else if(id == 1) {
        this.inputboxStack.push({
          inputboxDragSelector: this.inputboxDragSelector,
          inputboxWidth: this.inputboxWidth,
          inputboxHeight: this.inputboxHeight,
          inputboxMinW: this.inputboxMinW,
          inputboxMinH: this.inputboxMinH,
          inputboxLeft: this.inputboxLeft,
          inputboxTop: this.inputboxTop,
          inputboxFit: this.inputboxFit,
        });
      }else if(id == 2) {
        this.listboxStack.push({
          listboxDragSelector: this.listboxDragSelector,
          listboxWidth: this.listboxWidth,
          listboxHeight: this.listboxHeight,
          listboxMinW: this.listboxMinW,
          listboxMinH: this.listboxMinH,
          listboxLeft: this.listboxLeft,
          listboxTop: this.listboxTop,
          listboxFit: this.listboxFit,
        });
      }else if(id == 3) {
        this.buttonStack.push({
          buttonDragSelector: this.buttonDragSelector,
          buttonWidth: this.buttonWidth,
          buttonHeight: this.buttonHeight,
          buttonMinW: this.buttonMinW,
          buttonMinH: this.buttonMinH,
          buttonLeft: this.buttonLeft,
          buttonTop: this.buttonTop,
          buttonFit: this.buttonFit,
        });
      }
    },
    clear: function() {
      this.showOff();
      this.mainWidth = 300;
      this.mainHeight = 300;
      this.mainLeft = 0;
      this.mainTop = 0;
      this.labelStack = [];
      this.inputboxStack = [];
      this.listboxStack = [];
      this.buttonStack = [];
    },
    deleteLabel: function(num) {
      this.showOff();
      this.labelStack.splice(num, 1);
    },
    deleteInputBox: function(num) {
      this.showOff();
      this.inputboxStack.splice(num, 1);
    },
    deleteListBox: function(num) {
      this.showOff();
      this.listboxStack.splice(num, 1);
    },
    deleteButton: function(num) {
      this.showOff();
      this.buttonStack.splice(num, 1);
    },
  },
  filters: {
    checkEmpty(value) {
      return typeof value !== "number" ? 0 : value;
    }
  }
};
</script>

<style scoped>
.block {
  width: 100%;
  height: 100%;
  background-color: whitesmoke;
}
</style>

<style>
.table-container {
  position: relative;
}

.mainresizable {
  border: 1px solid #008099;
}

.labelresizable {
  background-color: whitesmoke;
  border: 1px dashed slategray;
  border-right: 5px double slategray;
}

.inputboxresizable {
  background-color: white;
  border: 1px inset slategray;
}

.listboxresizable {
  background-color: white;
  border: 1px inset slategray;
}

.buttonresizable {
  background-color: rgb(233, 233, 233);;
  background-position: center;
  border: 1px solid slategray;
}

.drag-container-titlebar {
  width: 100%;
  height: 25px;
  background: #008099;
  color: white;
  cursor: pointer;
}

.drag-container-label {
  width: 100%;
  background: whitesmoke;
  cursor: pointer;
}

.drag-container-inputbox {
  width: 100%;
  background: white;
  cursor: pointer;
}

.drag-container-listbox {
  width: 100%;
  height: 100%;
  background: white;
  cursor: pointer;
}

.drag-container-button {
  width: 100%;
  height: 21px;
  background: rgb(233, 233, 233);
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  cursor: pointer;
}

.table-block {
  color: white;
  background-color: #008099;
  display: table;
}

.table-row {
  display: table-row;
  text-align: left;
}

.table-cell {
  width: 50%;
}

.table-input {
  background-color: white;
  border: 2px solid slategray;
  width: 55px;
}
</style>
