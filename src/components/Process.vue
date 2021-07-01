<template>
  <v-app>
    <div class="process-container">
      <div class="text-container">
        <h1><span style="color:orange;">UIクリエイターへようこそ！！</span></h1>
        <br>
        UIクリエイターはUIをWeb上で簡単に作成できるWebアプリケーションです。<br>
        やり方は以下を参考にしてください。<br><br><br><br><br><br>
        <v-row justify="center">
          <strong>①ウィンドウの幅と高さを調節します。<br></strong>
        </v-row>
        <v-row justify="center">
          <v-img
            :src="process1"
            max-width="50%"
          />
        </v-row>
        <br><br><br><br><br><br>
        <v-row justify="center">
          <strong>②ウィジェットを選択して追加します。<br></strong>
        </v-row>
        <v-row justify="center">
          <v-img
            :src="process2"
            max-width="50%"
          />
        </v-row>
        <br><br><br><br><br><br>
        <v-row justify="center">
          <strong>③いくつでも追加可能です。<br></strong>
        </v-row>
        <v-row justify="center">
          <v-img
            :src="process3"
            max-width="50%"
          />
        </v-row>
        <br><br><br><br><br><br>
        <v-row justify="center">
          <strong>④幅と高さと位置を調節します。<br></strong>
        </v-row>
        <v-row justify="center">
          <v-img
            :src="process4"
            max-width="50%"
          />
        </v-row>
        <br><br><br><br><br><br>
        <v-row justify="center">
          <strong>⑤出力してコードを確認します。<br></strong>
        </v-row>
        <v-row justify="center">
          <v-img
            :src="process5"
            max-width="50%"
          />
        </v-row>
        <br><br><br><br><br><br>
        <v-row justify="center">
          <strong>⑥ダウンロードしてお好きなように役立ててください。<br></strong>
        </v-row>
        <v-row justify="center">
          <v-img
            :src="process6"
            max-width="50%"
          />
        </v-row>
        <br><br><br><br><br><br>
        <v-row justify="center">
          <strong>⑦テンプレートも用意しています。<br></strong>
        </v-row>
        <v-row justify="center">
          <v-img
            :src="process7"
            max-width="50%"
          />
        </v-row>
        <br><br><br><br><br><br>
        <v-row justify="center">
          <strong>中身の処理を記述してちょっとしたツールの完成です。<br></strong>
        </v-row>
        <v-row justify="center">
          <strong>随時、拡張予定ですのでお楽しみに。</strong>
        </v-row>
        <br><br><br>
        <h2>やり方を覚えたら「WORKSPACE」へレッツゴー！！</h2>
      </div>
    </div>
  </v-app>
</template>

<script>
export default {
  name: 'Process',
  data() {
    return {
      process1: require("@/assets/process1.png"),
      process2: require("@/assets/process2.png"),
      process3: require("@/assets/process3.png"),
      process4: require("@/assets/process4.png"),
      process5: require("@/assets/process5.png"),
      process6: require("@/assets/process6.png"),
      process7: require("@/assets/process7.png"),
    }
  }
}
</script>

<style>
.process-container {
  background-image: linear-gradient(
    -45deg, 
    #ffaf4d 25%, 
    whitesmoke 25%, 
    whitesmoke 50%, 
    #ffaf4d  50%, 
    #ffaf4d 90%, 
    whitesmoke 5%, 
    whitesmoke
    );
  color: #4d4d4d;
  width: 100%;
  height: 600vh;
}

.text-container{
  background-color: rgba(255,255,255,.8);
  border-radius: .25em;
  box-shadow: 0 0 .25em rgba(0,0,0,.25);
  box-sizing: border-box;
  left: 50%;
  padding: 10vmin;
  text-align: center;
  top: 500px;
  transform: translate(0%, 2%);
}
</style>
