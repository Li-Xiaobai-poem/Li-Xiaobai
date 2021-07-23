<template>
  <div id="Publisher">
    <app-header></app-header>
    <app-navbar></app-navbar>
    <el-container class="main">
      <el-header style=" background-color: rgba(84,92,100,0.5);
          color: #333;
          text-align: center;
          line-height: 60px;">
        <el-row>
          <el-col :span="6" :offset="8">
            <div>发布作品</div>
          </el-col>
        </el-row>
      </el-header>

      <el-main>
        <el-form label-width="100px">
          <el-form-item label="标题" prop="keyword">
            <el-input type="text" v-model="keyword" placeholder="请输入标题"></el-input>
          </el-form-item>
          <el-form-item label="正文" prop="poecontent">
            <el-input type="textarea" :rows="5" v-model="poecontent"
                      placeholder="请输入正文"></el-input>
          </el-form-item>
          <el-form-item label="文字" prop="mywords">
            <el-input type="textarea" :rows="5" v-model.number="mywords" placeholder="请输入想说的话"></el-input>
          </el-form-item>
          <el-form-item style="width: 400px;margin: 0 auto">
            <el-button style="background-color: rgba(84,92,100,0.6);color:#000000" @click="submitForm()">提交</el-button>
            <el-button style="background-color: rgba(84,92,100,0.6);color:#000000" @click="resetForm()">重置</el-button>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import AppHeader from './AppHeader'
import AppNavbar from './AppNavbar'

export default {
  components: {AppHeader, AppNavbar},
  data() {
    return {
      keyword: '',
      poecontent: '',
      mywords: '',
      username: this.COMMON.USERNAME
    }
  },
  mounted: function () {
    this.COMMON.get_baseinformation(this, this.username)
  },
  methods: {
    submitForm() {
      console.log(this.username)
      if (this.username === '') {
        this.$confirm('你还没有登陆，是否现在登陆？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$router.push({path: '/Login'})
        }).catch(() => {

        })
      } else {
        if (this.keyword === '' || this.poecontent === '') {
          this.$alert('请输入标题和正文', '提示', {
            confirmButtonText: '确定',
            callback: action => {

            }
          })
        } else {
          this.$confirm('确定发布？', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
            this.publish_true()
          }).catch(() => {

          })
        }
      }
    },
    publish_true() {
      this.$http.get('http://120.79.64.45:5000/app1/relpublish', {
        params: {
          username: this.username,
          keyword: this.keyword,
          poecontent: this.poecontent,
          mywords: this.mywords
        }
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          this.$alert(res['msg'], '提示', {
            confirmButtonText: '确定',
            callback: action => {

            }
          })
        })
    },
    resetForm() {
      this.$confirm('确定重置所有内容？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.keyword = ''
        this.poecontent = ''
        this.mywords = ''
      }).catch(() => {

      })
    }
  }
}
</script>

<style scoped>

#Publisher {
  background-image: url('../assets/p7.jpg');
  background-repeat: round;
  position: fixed;
  width: 100%;
  height: 100vh;
  overflow: auto;
}

.el-header {
  /*padding-top: 20px;*/
  /*font-size: 14px;*/
  /*color: #929292;*/
  /*box-shadow: inset 0 -2px 0 0 rgba(0, 0, 0, 0.07);*/
  /*padding-bottom: 16px;*/
  position: relative;
  width: 100%;
}

.el-main {
  position: absolute;
  left: 0px;
  right: 0px;
  top: 60px;
  bottom: 0;
  overflow-y: scroll;
}

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

.navbar {
  position: absolute;
  width: 230px;
  top: 50px; /* 距离上面50像素 */
  left: 0px;
  bottom: 0px;
  overflow-y: auto; /* 当内容过多时y轴出现滚动条 */
  background-color: #545c64;
}

.header {
  position: absolute;
  line-height: 50px;
  top: 0px;
  left: 0px;
  right: 0px;
  background-color: #2d3a4b;
}
</style>
