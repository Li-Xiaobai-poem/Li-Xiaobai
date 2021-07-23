<template>
  <div class="header">
    <img class="logo" src="@/assets/LiBai.png" width="25px"/>
    <span class="company">李小白</span>
    <el-button style="background-color:unset;color:white;border-color: transparent;float: right;" @click="exit">退出
    </el-button>
  </div>
</template>

<script>
export default {
  name: "index",
  methods: {
    exit() {
      this.$confirm('确认退出登陆？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.COMMON.USERNAME=""
        this.$router.push({path: '/Login'})
      }).catch(() => {

      })
    }
  }
}
</script>

<style scoped>
.logo {
  vertical-align: middle; /* 居中 */
  padding: 0px 10px 0px 40px; /* 上右下左 */
}

/* 文字 */
.company {
  position: absolute;
  color: white;
}
</style>
