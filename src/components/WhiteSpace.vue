<!-- Inspiration from: -->
<!-- https://codepen.io/CapMousse/pen/EJaHk -->

<template>
  <canvas class="canvas"></canvas>
</template>

<script>
export default {
  data() {
    return {
      cols: 0,
      rows: 0,
      colors: [240, 255, 255, 255, 255, 255, 255, 255, 255],
    }
  },
  methods: {
    drawRectangle: function(x, y, color){
      this.context.beginPath();
      this.context.moveTo(x, y);
      this.context.lineTo(x, y + 12);
      this.context.lineTo(x + 12, y);
      this.context.lineTo(x + 12, y + 12);
      this.context.lineTo(x, y);
      this.context.lineTo(x + 12, y);
      this.context.lineTo(x, y + 12);
      this.context.lineTo(x + 12, y + 12);
      this.context.fillStyle = "rgb("+color+","+color+","+color+")";
      this.context.fill();
      this.context.closePath();
    },
    getColor: function(){
      return this.colors[(Math.floor(Math.random() * 9))];
    },
    drawBackground: function(){
      var x = this.cols;
      var y;
      while(x--){
        y = this.rows;
        while(y--){
          this.drawRectangle(x * 24, y * 24, this.getColor());
        }
      }
    },
    animate: function(){
      var me = this;
      var x = Math.floor(Math.random() * this.cols);
      var y = Math.floor(Math.random() * this.rows);
      me.drawRectangle(x * 48, y * 48, this.getColor());
      setTimeout(function(){
        me.animate.call(me);
      }, 7);
    },
  },
  mounted() {
    this.context = this.$el.getContext('2d');
    this.cols = Math.floor(document.body.clientWidth / 48);
    this.rows = Math.floor(document.body.clientHeight / 48) + 1;
    this.drawBackground();
    this.animate();
  }
}
</script>

<style>
.canvas {
  background-color: rgb(255, 255, 255);
  width: 100%;
  height: 100%;
}
</style>
