<template>
  <div class="navbar">
    <el-menu :router='true' default-active="this.$router.path" class="el-menu-vertical-demo" background-color="#545c64"
             text-color="#fff" active-text-color="#ffd04b">
      <!-- 写诗 class就是对应的icon -->
      <el-menu-item index="/Products">
        <i class="el-icon-menu"></i>
        <span slot="title">生成诗歌</span>
      </el-menu-item>
      <!-- 发布作品 index下的左右 / 别忘记-->
      <el-menu-item index="/Publisher">
        <i class="el-icon-s-custom"></i>
        <span slot="title">发布作品
        </span>
      </el-menu-item>
      <!-- 个人中心 -->
      <el-menu-item index="/MyHome">
        <i class="el-icon-s-custom"></i>
        <span slot="title">个人中心
        </span>
      </el-menu-item>


      <!-- 论坛-->
      <el-menu-item index="/LunTan">
        <i class="el-icon-suitcase-1"></i>
        <span slot="title">论坛</span>
      </el-menu-item>

<!--      &lt;!&ndash; 退出 &ndash;&gt;-->
<!--      <el-menu-item index="/Login">-->
<!--        <i class="el-icon-user"></i>-->
<!--        <span slot="title">退出</span>-->
<!--      </el-menu-item>-->
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "index"
}
</script>

<style scoped>
/* 去掉右边框 */
.el-menu {
  border-right: none;
}
</style>
