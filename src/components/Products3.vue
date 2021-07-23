<template>
  <div>

    <app-header></app-header>
    <app-navbar></app-navbar>
    <el-row>
      <el-col :span="4">
        <el-button @click="goword">关键字</el-button>
      </el-col>
      <el-col :span="4">
        <el-button @click="goscene">场景</el-button>
      </el-col>
      <el-col :span="4">
        <el-button>图像</el-button>
      </el-col>
    </el-row>
    <!--外层大容器-->
    <div class="main">
      <br>
      <br>
      <div id="ti">图像诗歌生成</div>
      <br>
      <br>
      <br>
      <!--   表单：-->
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <!--        <el-form-item label="关键字">-->
        <!--          <el-input v-model="formInline.message" maxlength="1" placeholder="输入关键字（一个中文字符）" clearable-->
        <!--                    @keyup.native="inputChange($event)" @keydown.native="inputChange($event)"/>-->
        <!--        </el-form-item>-->


        <el-form-item label="选择诗歌类型">
          <el-select v-model="formInline.checkmessage" placeholder="诗歌类型">
            <el-option label="五言律诗" value="5yls"></el-option>
            <el-option label="五言绝句" value="5yjj"></el-option>
            <el-option label="七言律诗" value="7yls"></el-option>
            <el-option label="七言绝句" value="7yjj"></el-option>
          </el-select>
        </el-form-item>


        <el-upload
          class="upload-demo"
          action="http://127.0.0.1:8000/app1/imagewrite"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :file-list="fileList"
          list-type="picture">
          <el-button size="small" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>


        <br>
        <br>
        <el-form-item label="生成结果：" prop="desc">
          <el-input type="textarea" :rows="11" cols="35" v-model="result1" resize="none">666</el-input>
        </el-form-item>

      </el-form>

      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-button type="primary" @click="onCollect" icon="el-icon-star-off">收藏</el-button>
        &emsp; &emsp;&emsp;
        <!-- <el-button type="primary" icon="el-icon-edit" circle>再次生成</el-button>-->
      </el-form>

    </div>


  </div>
</template>

<script>
import AppHeader from "./AppHeader"
import AppNavbar from "./AppNavbar"

export default {
  name: "Products2",

  components: {AppHeader, AppNavbar},

  methods: {
    goword() {
      this.$router.push({path: '/Products'})
    },
    goscene() {
      this.$router.push({path: '/Products2'})

    }


  }
  ,
  data: {
    formInline: {

      checkmessage: '5yls'
    },
    result1: '',
  }
}

</script>

<style scoped>
.header {
  position: absolute;
  line-height: 50px;
  top: 0px;
  left: 0px;
  right: 0px;
  background-color: #2d3a4b;
}

/* 左侧样式 */
.navbar {
  position: absolute;
  width: 230px;
  top: 50px; /* 距离上面50像素 */
  left: 0px;
  bottom: 0px;
  overflow-y: auto; /* 当内容过多时y轴出现滚动条 */
  background-color: #545c64;
}

/* 主区域 */
.main {
  position: absolute;
  top: 50px;
  left: 230px;
  bottom: 0px;
  right: 0px; /* 距离右边0像素 */
  padding: 10px;
  overflow-y: auto; /* 当内容过多时y轴出现滚动条 */
  /* background-color: red; */
}
</style>
