<template>
  <div id="a">
    <!-- 使用子组件,使用-，不建议使用驼峰 -->
    <app-header></app-header>
    <app-navbar></app-navbar>
    <div class="main">

      <el-row>
        <el-col :span="4">
          <el-button @click="goword" style="background-color: unset;border-color: transparent ">关键字</el-button>
        </el-col>
        <el-col :span="4">
          <el-button style="background-color: unset;border-color: transparent "> 场景</el-button>
        </el-col>
        <!--        <el-col :span="4">-->
        <!--          <el-button @click="goimage" style="background-color: unset;border-color: transparent ">图像</el-button>-->
        <!--        </el-col>-->
      </el-row>
      <br>
      <br>
      <div id="ti">场景诗歌生成</div>
      <br>
      <br>
      <br>
      <!--   表单：-->
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item label="场景语句">
          <el-input v-model="formInline.message" placeholder="输入场景语句" clearable @keyup.native="inputChange($event)"
                    @keydown.native="inputChange($event)"/>
        </el-form-item>
        <el-form-item label="选择诗歌类型">
          <el-select v-model="formInline.checkmessage" placeholder="诗歌类型">
            <el-option label="五言律诗" value="5yls"></el-option>
            <el-option label="五言绝句" value="5yjj"></el-option>
            <el-option label="七言律诗" value="7yls"></el-option>
            <el-option label="七言绝句" value="7yjj"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit" style="background-color: unset;color:#000000">生成诗歌</el-button>
        </el-form-item>
        <br>
        <br>
        <el-form-item label="生成结果：" prop="desc">
          <el-input type="textarea" :rows="11" cols="35" v-model="result1" resize="none">666</el-input>
        </el-form-item>

      </el-form>

      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-button style="background-color: unset;color:#000000" @click="onCollect" icon="el-icon-star-off">收藏</el-button>
        &emsp; &emsp;&emsp;
        <!-- <el-button type="primary" icon="el-icon-edit" circle>再次生成</el-button>-->
      </el-form>

    </div>

  </div>
</template>

<script>
// 会导入./AppHeader下面的index.vue组件
import AppHeader from "./AppHeader"
import AppNavbar from "./AppNavbar"


export default {
  name: 'Products',
  data() {
    return {
      //被前端绑定了，会获得前端值
      formInline: {
        message: '',
        checkmessage: '5yls'
      },
      result1: '',
    }
  },

  methods: {
    goword() {
      this.$router.push({path: '/Products'})
    },
    goimage() {
      this.$router.push({path: '/Products3'})

    },
    //生成诗歌的方法：
    onSubmit() {
      console.log("123456")
      // 'http://127.0.0.1:8000/app1/getResult?q='   本地运行地址
      this.$http.get('http://120.79.64.45:5000/app1/getResult2', {
        params: {
          q: this.formInline.message,
          PoemType: this.formInline.checkmessage
        }
      }, {
        emulateJSON: true
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          if (res['error_num'] === 0) {
            this.result1 = res['result']
            console.log("成功")
          } else {
            this.$message.error('查询失败')
            console.log(res['msg'])
          }
        })


    },
    onCollect() {
      if (this.COMMON.USERNAME === '') {
        this.$confirm('你还没有登陆，是否登陆？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$router.push({path: '/Login'})
        }).catch(() => {

        })
      } else {
        if (this.result1 === '' || this.formInline.message === '') {
          this.$alert('收藏失败', '提示', {
            confirmButtonText: '确定',
            callback: action => {

            }
          })
        } else {
      // 'http://127.0.0.1:8000/app1/getResult?q='   本地运行地址
      this.$http.get('http://120.79.64.45:5000/app1/addcollect1', {
        params: {
          username: this.COMMON.USERNAME,
          poemcontent: this.result1,
          keyword: this.formInline.message
        }
      }, {
        emulateJSON: true
      })
        .then((response) => {

          let res = JSON.parse(response.bodyText)
          if (res['error_num'] === 0) {

            this.$alert('收藏成功', '提示', {
              confirmButtonText: '确定',
              callback: action => {

              }
            })
            console.log("收藏成功了")
          } else {
            this.$alert('收藏失败', '提示', {
              confirmButtonText: '确定',
              callback: action => {

              }
            })
          }
        })
        }
      }
    },
    inputChange(e) {
      const o = e.target;
      o.value = o.value.replace(/[^\u4E00-\u9FA5]/g, ''); // 清除除了中文以外的输入的字符
      this.formInline.message = o.value;
    },
  },
  components: {AppHeader, AppNavbar},    //指明使用的组件
  mounted() {

  }
}
</script>

<style scoped>
/* 头部样式 */
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
  padding: 0px;
  overflow-y: auto; /* 当内容过多时y轴出现滚动条 */
  /* background-color: red; */

}

#ti {
  font-size: 250%
}
#a{
  background-image: url('../assets/p9.jpg');
  background-repeat: round;
  position: fixed;
  width: 100%;
  height: 100vh;
  overflow: auto;
}

</style>

