<template>
  <div class="main">
    <el-row>
      <el-col :span="4">
        <el-button style="background-color: unset;  ">关键字</el-button>
      </el-col>
      <el-col :span="4">
        <el-button @click="goscene" style="background-color: unset; ">场景</el-button>
      </el-col>
      <!--      <el-col :span="4">-->
      <!--        <el-button @click="goimage" style="background-color: unset;border-color: transparent">图像</el-button>-->
      <!--      </el-col>-->
    </el-row>
    <br>
    <br>
    <div id="ti">关键字诗歌生成</div>
    <br>
    <br>
    <br>
    <!--   表单：-->
    <el-form :inline="true" :model="formInline" class="demo-form-inline">
      <el-form-item label="关键字">
        <el-input v-model="formInline.message" maxlength="1" placeholder="输入关键字（一个中文字符）"></el-input>
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
      <el-form-item prop="desc">
        <el-input type="textarea" :rows="11" cols="35" v-model="result1" resize="none">666</el-input>
      </el-form-item>

    </el-form>

    <el-form :inline="true" :model="formInline" class="demo-form-inline">
      <el-button @click="onCollect" icon="el-icon-star-off"
                 style="background-color: unset;color:#000000">收藏
      </el-button>
      &emsp; &emsp;&emsp;
      <!-- <el-button type="primary" icon="el-icon-edit" circle>再次生成</el-button>-->
    </el-form>

  </div>
</template>

<script>
//import {getPoem, addColloctions} from '../../api/api.js'
export default {
  name: "index",
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

    //生成诗歌的方法：
    onSubmit() {
      console.log("123456")
      // 'http://127.0.0.1:8000/app1/getResult?q='   本地运行地址
      this.$http.get('http://120.79.64.45:5000/app1/getResult', {
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
    goscene() {
      this.$router.push({path: '/Products2'})
    },
    goimage() {
      this.$router.push({path: '/Products3'})

    }


  }

}
</script>

<style scoped>
#ti {
  font-size: 250%
}
</style>
