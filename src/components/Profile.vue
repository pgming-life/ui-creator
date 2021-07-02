<template>
  <v-app>
    <div class="profile-container">
      <div class="content">
        <br>
        <h2><span style="color:darkorange">UIクリエイター</span></h2>
        <br>
        <strong>
          こんちには。<br>
          本サイトは、ユーザー手動によるウィジェット配置によって<br>
          プログラム上の位置・サイズ調整を視覚的に行えることにより、<br>
          簡単にUIを作成してプログラムコードとして出力しダウンロードすることができます。<br>
          現在は、PythonGUIの一つであるTkinterを対象にしていますが、<br>
          今後とも扱うUIの数を増やしていく予定です。<br><br>
          本作品のオープンソース:<br>
          <a href="https://github.com/pgming-life/ui-creator" target="_blank" rel="noopener">https://github.com/pgming-life/ui-creator</a>
        </strong>
      </div>
      <WhiteSpace/>
    </div>
  </v-app>
</template>

<script>
import WhiteSpace from './WhiteSpace'

export default {
  name: 'Profile',
  components: {
    WhiteSpace,
  },
};
</script>

<style>
.profile-container {
  width: 100%;
  height: 100%;
}

.content {
  background-color: rgba(255,255,255,.2);
  border-radius: .25em;
  box-shadow: 0 0 .25em rgba(0,0,0,.25);
  box-sizing: content-box;
  width: 70%;
  left: 50%;
  padding: 5vmin;
  position: fixed;
  transform: translate(-50%, -10%);
}
</style>
